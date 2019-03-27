#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import pandas as pd
from xml.etree import ElementTree as ET
from io import StringIO
from typing import Optional, Tuple, Dict, List, Any
from .base import ServerBase, BiomartException, DEFAULT_SCHEMA


class Dataset(ServerBase):
    """
    Class representing a biomart dataset.

    This class is responsible for handling queries to biomart datasets. 
    Queries can select a subset of attributes and can be filtered
    using any available filters. A list of valid attributes is available in
    the attributes property. If no attributes are given, a set of default
    attributes is used. A list of valid filters is available in the filters
    property. The type of value that can be specified for a given filter
    depends on the filter as some filters accept single values, whilst others
    can take lists of values.

    Args:
        name (str): Id of the dataset.
        display_name (str): Display name of the dataset.
        host (str): Url of host to connect to.
        path (str): Path on the host to access to the biomart service.
        port (int): Port to use for the connection.
        virtual_schema (str): The virtual schema of the dataset.

    Examples:
        Directly connecting to a dataset:
            >>> dataset = Dataset(name='hsapiens_gene_ensembl',
            >>>                   host='http://www.ensembl.org')

        Querying the dataset:
            >>> dataset.query(attributes=['ensembl_gene_id',
            >>>                           'external_gene_name'],
            >>>               filters={'chromosome_name': ['1', '2']})

        Listing available attributes:
            >>> dataset.attributes
            >>> dataset.list_attributes()

        Listing available filters:
            >>> dataset.filters
            >>> dataset.list_filters()
    """

    def __init__(self,
                 name: str,
                 display_name: str = "",
                 host: Optional[str] = None,
                 path: Optional[str] = None,
                 port: Optional[int] = None,
                 virtual_schema: str = DEFAULT_SCHEMA):
        super().__init__(host=host, path=path, port=port)

        self._name = name
        self._display_name = display_name
        self._virtual_schema = virtual_schema

        self._filters = None
        self._attributes = None
        self._default_attributes = None

    @property
    def name(self):
        """Name of the dataset (used as dataset id)."""
        return self._name

    @property
    def display_name(self):
        """Display name of the dataset."""
        return self._display_name

    @property
    def filters(self):
        """List of filters available for the dataset."""
        if self._filters is None:
            self._filters, self._attributes = self._fetch_configuration()
        return self._filters

    @property
    def attributes(self):
        """List of attributes available for the dataset (cached)."""
        if self._attributes is None:
            self._filters, self._attributes = self._fetch_configuration()
        return self._attributes

    @property
    def default_attributes(self):
        """List of default attributes for the dataset."""
        if self._default_attributes is None:
            self._default_attributes = {
                name: attr
                for name, attr in self.attributes.items()
                if attr.default is True
            }
        return self._default_attributes

    def list_attributes(self) -> pd.DataFrame:
        """
        List available attributes in a readable DataFrame format.
        :return: pd.DataFrame
        """

        def _row_gen(attributes: Dict):
            for attr in attributes.values():
                yield (attr.name, attr.display_name, attr.description)

        attr_df = pd.DataFrame.from_records(_row_gen(self.attributes),
                                            columns=["name", "display_name",
                                                     "description"])

        return attr_df

    def list_filters(self) -> pd.DataFrame:
        """
        List available filters in a readable DataFrame format.
        :return: pd.DataFrame
        """

        def _row_gen(filters: Dict):
            for filt in filters.values():
                yield (filt.name, filt.type, filt.description)

        filt_df = pd.DataFrame.from_records(_row_gen(self.filters),
                                            columns=["name", "type",
                                                     "description"])

        return filt_df

    def _fetch_configuration(self) -> Tuple[Dict, Dict]:
        # Get datasets using biomart.
        response = self.get(type="configuration", dataset=self._name)

        # Check response for problems.
        if "Problem retrieving configuration" in response.text:
            raise BiomartException("Failed to retrieve dataset configuration, "
                                   "check the dataset name and schema.")

        # Get filters and attributes from xml.
        xml = ET.fromstring(response.content)

        filters = {f.name: f for f in self._filters_from_xml(xml)}
        attributes = {a.name: a for a in self._attributes_from_xml(xml)}

        return filters, attributes

    @staticmethod
    def _filters_from_xml(xml):
        for node in xml.iter("FilterDescription"):
            attrib = node.attrib
            yield Filter(name=attrib["internalName"],
                         type=attrib.get("type", ""))

    @staticmethod
    def _attributes_from_xml(xml):
        for page_index, page in enumerate(xml.iter("AttributePage")):
            for desc in page.iter("AttributeDescription"):
                attrib = desc.attrib

                # Default attributes can only be from the first page.
                default = (page_index == 0 and
                           attrib.get("default", "") == "true")

                yield Attribute(name=attrib["internalName"],
                                display_name=attrib.get("displayName", ""),
                                description=attrib.get("description", ""),
                                default=default)

    def query(self,
              attributes: List[str] = None,
              filters: Dict[str, Any] = None,
              only_unique: bool = True,
              use_attr_names: bool = False,
              dtypes: Dict[str, Any] = None
              ) -> pd.DataFrame:
        """
        Queries the dataset to retrieve the contained data.
        :param List[str] attributes: names of attributes to fetch in the query.
        Attribute names must correspond to valid attributes. See the attributes
        property for a list of valid attributes.
        :param Dict[str, Any] filters: dictionary of filters to filter the
        dataset by. Filter names and values must correspond to valid filters
        and filter values. See the filters property for a list of valid
        filters.
        :param bool only_unique: whether to return only rows containing unique
        values or to include duplicate rows (default: True)
        :param bool use_attr_names: whether to use the attribute names as
        column names in the result of the attribute display names
        (default: False)
        :param Dict[str, Any] dtypes: dictionary specifying the data type for
        each attribute
        :return: pd.DataFrame
        """
        # Example query from Ensembl biomart:
        #
        # <?xml version="1.0" encoding="UTF-8"?>
        # <!DOCTYPE Query>
        # <Query  virtualSchemaName = "default" formatter = "TSV" header = "0"
        #  uniqueRows = "0" count = "" datasetConfigVersion = "0.6" >
        #   <Dataset name = "hsapiens_gene_ensembl" interface = "default" >
        #       <Filter name = "chromosome_name" value = "1,2"/>
        #       <Filter name = "end" value = "10000000"/>
        #       <Filter name = "start" value = "1"/>
        #       <Attribute name = "ensembl_gene_id" />
        #       <Attribute name = "ensembl_transcript_id" />
        #   </Dataset>
        # </Query>

        # Setup query element.
        root = ET.Element("Query")
        root.set("virtualSchemaName", self._virtual_schema)
        root.set("formatter", "TSV")
        root.set("header", "1")
        # root.set("uniqueRows", native_str(int(only_unique)))
        root.set("uniqueRows", str(int(only_unique)))
        root.set("datasetConfigVersion", "0.6")

        # Add dataset element.
        dataset = ET.SubElement(root, "Dataset")
        dataset.set("name", self.name)
        dataset.set("interface", "default")

        # Default to default attributes if none requested.
        if attributes is None:
            attributes = list(self.default_attributes.keys())

        # Add attribute elements.
        for name in attributes:
            try:
                attr = self.attributes[name]
                self._add_attr_node(dataset, attr)
            except KeyError:
                raise BiomartException(
                    "Unknown attribute {}, check dataset attributes "
                    "for a list of valid attributes.".format(name))

        if filters is not None:
            # Add filter elements.
            for name, value in filters.items():
                try:
                    filter_ = self.filters[name]
                    self._add_filter_node(dataset, filter_, value)
                except KeyError:
                    raise BiomartException(
                        "Unknown filter {}, check dataset filters "
                        "for a list of valid filters.".format(name))

        # Fetch response.
        response = self.get(query=ET.tostring(root))

        # Raise exception if an error occurred.
        if "Query ERROR" in response.text:
            raise BiomartException(response.text)

        # Parse results into a DataFrame.
        try:
            result = pd.read_csv(StringIO(response.text),
                                 sep="\t",
                                 dtype=dtypes)
        # Type error is raised of a data type is not understood by pandas
        except TypeError as err:
            raise ValueError("Non valid data type is used in dtypes")

        if use_attr_names:
            # Rename columns with attribute names instead of display names.
            column_map = {
                self.attributes[attr].display_name: attr
                for attr in attributes
            }
            result.rename(columns=column_map, inplace=True)

        return result

    @staticmethod
    def _add_attr_node(root, attr):
        attr_el = ET.SubElement(root, "Attribute")
        attr_el.set("name", attr.name)

    @staticmethod
    def _add_filter_node(root, filter_, value):
        """Adds filter xml node to root."""
        filter_el = ET.SubElement(root, "Filter")
        filter_el.set("name", filter_.name)

        # Set filter value depending on type.
        if filter_.type == "boolean":
            # Boolean case.
            if value is True or value.lower() in {"included", "only"}:
                filter_el.set("excluded", "0")
            elif value is False or value.lower() == "excluded":
                filter_el.set("excluded", "1")
            else:
                raise ValueError("Invalid value for boolean filter ({})"
                                 .format(value))
        elif isinstance(value, list) or isinstance(value, tuple):
            # List case.
            filter_el.set("value", ",".join(map(str, value)))
        else:
            # Default case.
            filter_el.set("value", str(value))

    def __repr__(self):
        return ("<biomart.Dataset name={!r}, display_name={!r}>"
                .format(self._name, self._display_name))


class Attribute:
    """
    Biomart dataset attribute.

    Attributes:
        name (str): Attribute name.
        display_name (str): Attribute display name.
        description (str): Attribute description.
        default (bool): Whether the attribute is a default attribute of the
        corresponding datasets (default: False).
    """

    def __init__(self,
                 name: str,
                 display_name: str = "",
                 description: str = "",
                 default: bool = False):
        self._name = name
        self._display_name = display_name
        self._description = description
        self._default = default

    @property
    def name(self):
        """Name of the attribute."""
        return self._name

    @property
    def display_name(self):
        """Display name of the attribute."""
        return self._display_name

    @property
    def description(self):
        """Description of the attribute."""
        return self._description

    @property
    def default(self):
        """Whether this is a default attribute."""
        return self._default

    def __repr__(self):
        return (("<biomart.Attribute name={!r},"
                 " display_name={!r}, description={!r}>")
                .format(self._name, self._display_name, self._description))


class Filter(object):
    """
    Biomart dataset filter.

    Attributes:
        name (str): Filter name.
        type (str): Type of the filter (boolean, int, etc.).
        description (str): Filter description.
    """

    def __init__(self,
                 name: str,
                 type: str,
                 description: str = ""):
        self._name = name
        self._type = type
        self._description = description

    @property
    def name(self):
        """Filter name."""
        return self._name

    @property
    def type(self):
        """Filter type."""
        return self._type

    @property
    def description(self):
        """Filter description."""
        return self._description

    def __repr__(self):
        return ("<biomart.Filter name={!r}, type={!r}>"
                .format(self.name, self.type))

