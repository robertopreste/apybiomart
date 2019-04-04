#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import asyncio
import aiohttp
import io
import requests
import pandas as pd
from xml.etree import ElementTree as ET
from typing import Optional, Dict, Any, Tuple, Generator, List, Union


class BiomartException(Exception):
    """Basic exception class for biomart exceptions."""
    pass


class Server:
    """
    Basic server class used to call BioMart using sync or async calls.
    """

    def __init__(self,
                 host: str = "http://www.ensembl.org/biomart/martservice"):
        self.host = host

    def get_sync(self,
                 **params: Optional[Dict[str, Any]]):
        """
        Syncronous call to BioMart.
        :param Optional[Dict[str, Any]] params: keyword arguments for the
        requests call
        :return:
        """
        resp = requests.get(self.host, params=params)

        return resp

    async def get_async(self,
                        **params: Optional[Dict[str, Any]]):
        """
        Asyncronous call to BioMart.
        :param Optional[Dict[str, Any]] params: keyword arguments for the
        async call
        :return:
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(self.host, params=params) as resp:
                return await resp.text()


class MartServer(Server):
    """
    Class used to retrieve and list available marts.
    """

    def __init__(self):
        super().__init__()

    def list_marts(self) -> pd.DataFrame:
        """
        Return the list of available marts as a dataframe.
        :return: pd.DataFrame
        """
        return pd.DataFrame.from_records(self._fetch_marts(),
                                         columns=["name",
                                                  "display_name"])
    
    def _fetch_marts(self) -> Dict[str, Tuple[Any]]:
        """
        Retrieve the available marts from BioMart.

        Call BioMart to retrieve the available marts and return the
        internal dict used to parse them by self.list_marts().
        :return: Dict[str, Tuple[Any]]
        """
        resp = self.get_sync(type="registry")
        xml = ET.fromstring(resp.content)
        marts = list(zip(*self._mart_from_xml(xml)))

        return {"name": marts[0],
                "display_name": marts[1]}

    @staticmethod
    def _mart_from_xml(xml):
        """
        Extract mart information from XML.

        Parse the xml to extract name and display name of each mart.
        :param xml: ElementTree retrieved from Biomart
        :return: Generator[str, str]
        """
        for child in xml.findall("MartURLLocation"):
            yield (child.attrib["name"],
                   child.attrib["displayName"])


class DatasetServer(Server):
    """
    Class used to retrieve and list available datasets for a mart.
    """

    def __init__(self, mart: str):
        super().__init__()
        self.mart = mart

    def list_datasets(self) -> pd.DataFrame:
        """
        Return the list of available datasets for a specific mart as a
        dataframe.
        :return: pd.DataFrame
        """
        df = pd.read_csv(self._fetch_datasets(),
                         sep="\t",
                         # TODO: look for proper names in Biomart documentation
                         names=["type", "name", "display_name", "unknown",
                                "unknown2", "unknown3", "unknown4",
                                "virtual_schema", "unknown5"],
                         usecols=["name", "display_name"])
        df["mart"] = self.mart

        return df

    def _fetch_datasets(self) -> io.StringIO:
        """
        Retrieve available datasets for a mart.

        Call BioMart to retrieve the available datasets for a specific
        mart and return the internal string used to parse them by
        self.list_datasets().
        :return: io.StringIO
        """
        resp = self.get_sync(type="datasets", mart=self.mart)
        
        return io.StringIO(resp.text)


class AttributesServer(Server):
    """
    Class used to retrieve and list available attributes for a dataset.
    """

    def __init__(self, dataset: str):
        super().__init__()
        self.dataset = dataset

    def list_attributes(self) -> pd.DataFrame:
        """
        Return the list of available attributes for a specific dataset as
        a dataframe.
        :return: pd.DataFrame
        """
        df = pd.DataFrame.from_records(self._fetch_attributes(),
                                       columns=["name",
                                                "display_name",
                                                "description"])
        df["dataset"] = self.dataset

        return df

    def _fetch_attributes(self) -> Dict[str, Tuple[Any]]:
        """
        Retrieve available attributes for a dataset.

        Call BioMart to retrieve the available attributes for a specific
        dataset and return the internal dict used to parse them by
        self.list_attributes().
        :return: Dict[str, Tuple[Any]]
        """
        resp = self.get_sync(type="configuration", dataset=self.dataset)
        xml = ET.fromstring(resp.content)
        attribs = list(zip(*self._attributes_from_xml(xml)))

        return {"name": attribs[0],
                "display_name": attribs[1],
                "description": attribs[2]}

    @staticmethod
    def _attributes_from_xml(xml) -> Generator[str, Any, Any]:
        """
        Extract attributes information from XML.

        Parse the xml to extract name, display name and description
        of each attribute.
        :param xml: ElementTree retrieved from Biomart
        :return: Generator[str, Any, Any]
        """
        for page in xml.iter("AttributePage"):
            for desc in page.iter("AttributeDescription"):
                attrib = desc.attrib

                yield (attrib["internalName"],
                       attrib.get("displayName", ""),
                       attrib.get("description", ""))


class FiltersServer(Server):
    """
    Class used to retrieve and list available filters for a dataset.
    """

    def __init__(self, dataset: str):
        super().__init__()
        self.dataset = dataset

    def list_filters(self) -> pd.DataFrame:
        """
        Return the list of available filters for a specific dataset as
        a dataframe.
        :return: pd.DataFrame
        """
        df = pd.DataFrame.from_records(self._fetch_filters(),
                                       columns=["name",
                                                "type",
                                                "description"])
        df["dataset"] = self.dataset

        return df

    def _fetch_filters(self) -> Dict[str, Tuple[Any]]:
        """
        Retrieve available filters for a dataset.

        Call BioMart to retrieve the available filters for a specific
        dataset and return the internal dict used to parse them by
        self.list_filters().
        :return: Dict[str, Tuple[Any]]
        """
        resp = self.get_sync(type="configuration", dataset=self.dataset)
        xml = ET.fromstring(resp.content)
        filters = list(zip(*self._filters_from_xml(xml)))

        return {"name": filters[0],
                "type": filters[1],
                "description": filters[2]}

    @staticmethod
    def _filters_from_xml(xml) -> Generator[str, Any, Any]:
        """
        Extract filters information from XML.

        Parse the xml to extract name, type and description of each
        filter.
        :param xml: ElementTree retrieved from Biomart
        :return: Generator[str, Any, Any]
        """
        for node in xml.iter("FilterDescription"):
            filt = node.attrib
            yield (filt["internalName"],
                   filt.get("type", ""),
                   filt.get("description", ""))


class Query(Server):
    """
    Class used to perform either synchronous or asynchronous queries on
    BioMart.
    """

    def __init__(self,
                 attributes: List[str],
                 filters: Dict[str, Union[str, List]],
                 dataset: str):
        super().__init__()
        self.attributes = attributes
        self.filters = filters
        self.dataset = dataset

    def query(self) -> pd.DataFrame:
        """
        Perform synchronous query.

        Return the result of the query based on the given attributes,
        filters and optional dataset using Server.get_sync().
        :return: pd.DataFrame
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
                raise BiomartException(
                    "Unknown attribute {}, check dataset attributes "
                    "for a list of valid attributes.".format(name))

        if self.filters is not None:
            # Add filter elements.
            for name, value in self.filters.items():
                try:
                    self._add_filter_node(dataset, name, value)
                except KeyError:
                    raise BiomartException(
                        "Unknown filter {}, check dataset filters "
                        "for a list of valid filters.".format(name))

        resp = self.get_sync(query=str(ET.tostring(root), "utf-8"))

        if "Query ERROR" in resp.text:
            raise BiomartException(resp.text)

        try:
            result = pd.read_csv(io.StringIO(resp.text), sep="\t")
        # Type error is raised of a data type is not understood by pandas
        except TypeError as err:
            raise ValueError("Non valid data type is used in dtypes")

        return result

    async def aquery(self) -> pd.DataFrame:
        """
        Perform asynchronous query.

        Return the result of the query based on the given attributes,
        filters and optional dataset using Server.get_async().
        :return: pd.DataFrame
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
                raise BiomartException(
                    "Unknown attribute {}, check dataset attributes "
                    "for a list of valid attributes.".format(name))

        if self.filters is not None:
            # Add filter elements.
            for name, value in self.filters.items():
                try:
                    self._add_filter_node(dataset, name, value)
                except KeyError:
                    raise BiomartException(
                        "Unknown filter {}, check dataset filters "
                        "for a list of valid filters.".format(name))

        resp = await self.get_async(query=str(ET.tostring(root), "utf-8"))

        if "Query ERROR" in resp:
            raise BiomartException(resp)

        try:
            result = pd.read_csv(io.StringIO(resp), sep="\t")
        # Type error is raised of a data type is not understood by pandas
        except TypeError as err:
            raise ValueError("Non valid data type is used in dtypes")

        return result

    @staticmethod
    def _add_attr_node(root, attr: str):
        """
        Add the given attribute name to the dataset ElementTree sub-element.
        :param root: dataset sub-element root node
        :param str attr: attribute name
        :return:
        """
        attr_el = ET.SubElement(root, "Attribute")
        attr_el.set("name", attr)

    @staticmethod
    def _add_filter_node(root, name: str, value: str):
        """
        Add the given filter name and value to the dataset ElementTree
        sub-element.
        :param root: dataset sub-element root node
        :param str name: filter name
        :param str value: filter value
        :return:
        """
        filter_el = ET.SubElement(root, "Filter")
        filter_el.set("name", name)

        # TODO
        # Set filter value depending on type.
        if isinstance(value, list) or isinstance(value, tuple):
            # List case.
            filter_el.set("value", ",".join(map(str, value)))
        # if name.type == "boolean":
        # Boolean case.
        elif value is True or value.lower() in {"included", "only"}:
            filter_el.set("excluded", "0")
        elif value is False or value.lower() == "excluded":
            filter_el.set("excluded", "1")
        # else:
        #     raise ValueError("Invalid value for boolean filter ({})"
        #                      .format(value))
        elif isinstance(value, list) or isinstance(value, tuple):
            # List case.
            filter_el.set("value", ",".join(map(str, value)))
        else:
            # Default case.
            filter_el.set("value", str(value))
