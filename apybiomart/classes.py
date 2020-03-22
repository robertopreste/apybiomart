#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import io
from typing import Optional, Dict, Any, Tuple, Generator, List, Union
from xml.etree import ElementTree as ET

import asyncio
import aiohttp
import requests
import pandas as pd


class _BiomartException(Exception):
    """Basic exception class for BioMart exceptions."""
    pass


class _Server:
    """Basic server class used to call BioMart using sync or async calls.

    Attributes:
        host: URL to connect to
        save: save results to a CSV file [default: False]
    """

    def __init__(self,
                 host: str = "http://www.ensembl.org/biomart/martservice",
                 save: bool = False):
        self.host = host
        self.save = save
        if not self._check_connection():
            raise _BiomartException("No internet connection available!")

    @staticmethod
    def _check_connection() -> bool:
        """Check for a functioning internet connection.

        Returns:
            bool
        """
        url = "https://httpstat.us/200"
        timeout = 5
        try:
            _ = requests.get(url, timeout=timeout)
            return True
        except requests.exceptions.RequestException as e:
            pass
        return False

    def get_sync(self,
                 **params: Optional[str]):
        """Synchronous call to BioMart.

        Keyword Args:
            params: keyword arguments for the requests call

        Returns:
            request call to self.host with given params
        """
        resp = requests.get(self.host, params=params)

        return resp

    async def get_async(self,
                        **params: Optional[str]):
        """Asynchronous call to BioMart.

        Keyword Args:
            params: keyword arguments for the async call

        Returns:
            asynchronous call to self.host with given params
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(self.host, params=params) as resp:
                return await resp.text()


class MartServer(_Server):
    """Class used to retrieve and list available marts."""

    def __init__(self, save: bool = False):
        super().__init__(save=save)

    def find_marts(self) -> pd.DataFrame:
        """Return the list of available marts as a dataframe.

        Returns:
            pd.DataFrame
        """
        df = pd.DataFrame.from_records(self._fetch_marts(),
                                       columns=["name", "display_name"])
        df.columns = ["Mart_ID", "Mart_name"]
        df.replace(pd.np.nan, "", inplace=True)
        if self.save:
            df.to_csv("apybiomart_marts.csv", index=False)

        return df

    def _fetch_marts(self) -> Dict[str, Tuple[Any]]:
        """Retrieve the available marts from BioMart.

        Call BioMart to retrieve the available marts and return the
        internal dict used to parse them by self.list_marts().

        Returns:
            dictionary from parsed xml
        """
        resp = self.get_sync(type="registry")
        xml = ET.fromstring(resp.content)
        marts = list(zip(*self._mart_from_xml(xml)))

        return {"name": marts[0],
                "display_name": marts[1]}

    @staticmethod
    def _mart_from_xml(xml):
        """Extract mart information from XML.

        Parse the xml to extract name and display name of each mart.

        Args:
            xml: ElementTree retrieved from Biomart

        Returns:
            generator for each node in the xml
        """
        for child in xml.findall("MartURLLocation"):
            yield (child.attrib["name"],
                   child.attrib["displayName"])


class DatasetServer(_Server):
    """Class used to retrieve and list available datasets for a mart.

    Attributes:
        mart: BioMart mart name
    """

    def __init__(self, mart: str, save: bool = False):
        super().__init__(save=save)
        self.mart = mart

    def find_datasets(self) -> pd.DataFrame:
        """Return the list of available datasets for a specific mart as a
        dataframe."""
        df = pd.read_csv(self._fetch_datasets(),
                         sep="\t",
                         # TODO: look for proper names in Biomart documentation
                         names=["type", "name", "display_name", "unknown",
                                "version", "unknown3", "unknown4",
                                "virtual_schema", "unknown5"],
                         usecols=["name", "display_name"])
        df["mart"] = self.mart
        df.columns = ["Dataset_ID", "Dataset_name", "Mart_ID"]
        df.replace(pd.np.nan, "", inplace=True)
        if self.save:
            df.to_csv("apybiomart_datasets.csv", index=False)

        return df

    def _fetch_datasets(self) -> io.StringIO:
        """Retrieve available datasets for a mart.

        Call BioMart to retrieve the available datasets for a specific
        mart and return the internal string used to parse them by
        self.list_datasets().

        Returns:
            io.StringIO element from response text
        """
        resp = self.get_sync(type="datasets", mart=self.mart)

        return io.StringIO(resp.text)


class AttributesServer(_Server):
    """Class used to retrieve and list available attributes for a dataset.

    Attributes:
        dataset: BioMart dataset name
    """

    def __init__(self, dataset: str, save: bool = False):
        super().__init__(save=save)
        self.dataset = dataset

    def find_attributes(self) -> pd.DataFrame:
        """Return the list of available attributes for a specific dataset as
        a dataframe."""
        df = pd.DataFrame.from_records(self._fetch_attributes(),
                                       columns=["name",
                                                "display_name",
                                                "description"])
        df["dataset"] = self.dataset
        df.columns = ["Attribute_ID", "Attribute_name",
                      "Attribute_description", "Dataset_ID"]
        df.replace(pd.np.nan, "", inplace=True)
        if self.save:
            df.to_csv("apybiomart_attributes.csv", index=False)

        return df

    def _fetch_attributes(self) -> Dict[str, Tuple[Any]]:
        """Retrieve available attributes for a dataset.

        Call BioMart to retrieve the available attributes for a specific
        dataset and return the internal dict used to parse them by
        self.list_attributes().

        Returns:
            dictionary from parsed xml
        """
        resp = self.get_sync(type="configuration", dataset=self.dataset)
        xml = ET.fromstring(resp.content)
        attribs = list(zip(*self._attributes_from_xml(xml)))

        return {"name": attribs[0],
                "display_name": attribs[1],
                "description": attribs[2]}

    @staticmethod
    def _attributes_from_xml(xml) -> Generator[str, Any, Any]:
        """Extract attributes information from XML.

        Parse the xml to extract name, display name and description
        of each attribute.

        Args:
            xml: ElementTree retrieved from Biomart

        Returns:
            generator for each node in the xml
        """
        for page in xml.iter("AttributePage"):
            for desc in page.iter("AttributeDescription"):
                attrib = desc.attrib

                yield (attrib["internalName"],
                       attrib.get("displayName", ""),
                       attrib.get("description", ""))


class FiltersServer(_Server):
    """Class used to retrieve and list available filters for a dataset.

    Attributes:
        dataset: BioMart dataset name
    """

    def __init__(self, dataset: str, save: bool = False):
        super().__init__(save=save)
        self.dataset = dataset

    def find_filters(self) -> pd.DataFrame:
        """Return the list of available filters for a specific dataset as
        a dataframe."""
        df = pd.DataFrame.from_records(self._fetch_filters(),
                                       columns=["name",
                                                "type",
                                                "description"])
        df["dataset"] = self.dataset
        df.columns = ["Filter_ID", "Filter_type",
                      "Filter_description", "Dataset_ID"]
        df.replace(pd.np.nan, "", inplace=True)
        if self.save:
            df.to_csv("apybiomart_filters.csv", index=False)

        return df

    def _fetch_filters(self) -> Dict[str, Tuple[Any]]:
        """Retrieve available filters for a dataset.

        Call BioMart to retrieve the available filters for a specific
        dataset and return the internal dict used to parse them by
        self.list_filters().

        Returns:
            dictionary from parsed xml
        """
        resp = self.get_sync(type="configuration", dataset=self.dataset)
        xml = ET.fromstring(resp.content)
        filters = list(zip(*self._filters_from_xml(xml)))

        return {"name": filters[0],
                "type": filters[1],
                "description": filters[2]}

    @staticmethod
    def _filters_from_xml(xml) -> Generator[str, Any, Any]:
        """Extract filters information from XML.

        Parse the xml to extract name, type and description of each
        filter.

        Args:
            xml: ElementTree retrieved from Biomart

        Returns:
            generator for each node in the xml
        """
        for node in xml.iter("FilterDescription"):
            filt = node.attrib
            yield (filt["internalName"],
                   filt.get("type", ""),
                   filt.get("description", ""))


class Query(_Server):
    """Class used to perform either synchronous or asynchronous queries on
    BioMart.

    Attributes:
        attributes: list of attributes to include
        filters: dict of filter name : value to filter results
        dataset: BioMart dataset name
    """

    def __init__(self,
                 attributes: List[str],
                 filters: Dict[str, Union[str, int, list, tuple, bool]],
                 dataset: str,
                 save: bool = False):
        super().__init__(save=save)
        self.attributes = attributes
        self.filters = filters
        self.dataset = dataset

    def query(self) -> pd.DataFrame:
        """Perform synchronous query.

        Return the result of the query based on the given attributes,
        filters and optional dataset using Server.get_sync(), as a pandas
        DataFrame.
        """
        # Setup query element.
        root = ET.Element("Query")
        root.set("virtualSchemaName", "default")
        root.set("formatter", "TSV")
        root.set("header", "1")
        root.set("datasetConfigVersion", "0.6")
        # Add dataset element.
        dataset = ET.SubElement(root, "Dataset")
        dataset.set("name", self.dataset)
        dataset.set("interface", "default")

        # Add attribute elements.
        for name in self.attributes:
            try:
                self._add_attr_node(dataset, name)
            except KeyError:
                raise _BiomartException(
                    "Unknown attribute {}, check dataset attributes "
                    "for a list of valid attributes.".format(name))

        if self.filters is not None:
            # Add filter elements.
            for name, value in self.filters.items():
                try:
                    self._add_filter_node(dataset, name, value)
                except KeyError:
                    raise _BiomartException(
                        "Unknown filter {}, check dataset filters "
                        "for a list of valid filters.".format(name))

        resp = self.get_sync(query=str(ET.tostring(root), "utf-8"))

        if "Query ERROR" in resp.text:
            raise _BiomartException(resp.text)

        try:
            result = pd.read_csv(io.StringIO(resp.text), sep="\t")
        # Type error is raised of a data type is not understood by pandas
        except TypeError as err:
            raise ValueError("Non valid data type is used in dtypes")
        result.replace(pd.np.nan, "", inplace=True)

        if self.save:
            result.to_csv("apybiomart_query.csv", index=False)

        return result

    async def aquery(self) -> pd.DataFrame:
        """Perform asynchronous query.

        Return the result of the query based on the given attributes,
        filters and optional dataset using Server.get_async(), as a pandas
        DataFrame.
        """
        # Setup query element.
        root = ET.Element("Query")
        root.set("virtualSchemaName", "default")
        root.set("formatter", "TSV")
        root.set("header", "1")
        root.set("datasetConfigVersion", "0.6")
        # Add dataset element.
        dataset = ET.SubElement(root, "Dataset")
        dataset.set("name", self.dataset)
        dataset.set("interface", "default")

        # Add attribute elements.
        for name in self.attributes:
            try:
                self._add_attr_node(dataset, name)
            except KeyError:
                raise _BiomartException(
                    "Unknown attribute {}, check dataset attributes "
                    "for a list of valid attributes.".format(name))

        if self.filters is not None:
            # Add filter elements.
            for name, value in self.filters.items():
                try:
                    self._add_filter_node(dataset, name, value)
                except KeyError:
                    raise _BiomartException(
                        "Unknown filter {}, check dataset filters "
                        "for a list of valid filters.".format(name))

        resp = await self.get_async(query=str(ET.tostring(root), "utf-8"))

        if "Query ERROR" in resp:
            raise _BiomartException(resp)

        try:
            result = pd.read_csv(io.StringIO(resp), sep="\t")
        # Type error is raised of a data type is not understood by pandas
        except TypeError as err:
            raise ValueError("Non valid data type is used in dtypes")
        result.replace(pd.np.nan, "", inplace=True)

        if self.save:
            result.to_csv("apybiomart_aquery.csv", index=False)

        return result

    @staticmethod
    def _add_attr_node(root, attr: str):
        """Add the given attribute name to the dataset ElementTree sub-element.

        Args:
            root: dataset sub-element root node
            attr: attribute name
        """
        attr_el = ET.SubElement(root, "Attribute")
        attr_el.set("name", attr)

    @staticmethod
    def _add_filter_node(root,
                         name: str,
                         value: Union[str, int, list, tuple, bool]):
        """Add the given filter name and value to the dataset ElementTree
        sub-element.

        Args:
            root: dataset sub-element root node
            name: filter name
            value: filter value
        """
        filter_el = ET.SubElement(root, "Filter")
        filter_el.set("name", name)

        # TODO
        # Set filter value depending on type.
        # Boolean case
        if isinstance(value, bool):
            if value is True:
                filter_el.set("excluded", "0")
            else:
                filter_el.set("excluded", "1")
        # List case
        elif isinstance(value, list) or isinstance(value, tuple):
            filter_el.set("value", ",".join(map(str, value)))
        # String case
        elif isinstance(value, str):
            if value.lower() in ("included", "only"):
                filter_el.set("excluded", "0")
            elif value.lower() == "excluded":
                filter_el.set("excluded", "1")
            else:
                filter_el.set("value", value)
        # Mostly int case
        else:
            filter_el.set("value", str(value))
