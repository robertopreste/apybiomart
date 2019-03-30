#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import asyncio
import aiohttp
import io
import requests
import pandas as pd
import xml.etree.ElementTree as ET
from typing import Optional, Dict, Any


class Server:
    def __init__(self,
                 host: str = "http://www.ensembl.org/biomart/martservice"):
        self.host = host

    def get_sync(self,
                 **params: Optional[Dict[str, Any]]):
        """
        Syncronous call.
        :param Optional[Dict[str, Any]] params: keyword arguments for the requests call
        :return:
        """
        resp = requests.get(self.host, params=params)

        return resp


class MartServer(Server):
    def __init__(self):
        super().__init__()

    def list_marts(self):
        return pd.DataFrame.from_records(self._fetch_marts(),
                                         columns=["name",
                                                  "display_name"])
    
    def _fetch_marts(self):
        resp = self.get_sync(type="registry")
        xml = ET.fromstring(resp.content)
        marts = list(zip(*self._mart_from_xml(xml)))

        return {"name": marts[0],
                "display_name": marts[1]}

    def _mart_from_xml(self, xml):
        for child in xml.findall("MartURLLocation"):
            yield (child.attrib["name"],
                   child.attrib["displayName"])


class DatasetServer(Server): 
    def __init__(self, mart: str):
        super().__init__()
        self.mart = mart

    def list_datasets(self):
        df = pd.read_csv(self._fetch_datasets(),
                         sep="\t",
                         names=["type", "name", "display_name", "unknown",
                                "unknown2", "unknown3", "unknown4",
                                "virtual_schema", "unknown5"],
                         usecols=["name", "display_name"])
        df["mart"] = self.mart

        return df

    def _fetch_datasets(self):
        resp = self.get_sync(type="datasets", mart=self.mart)
        
        return io.StringIO(resp.text)


class AttributesServer(Server):
    def __init__(self, dataset: str):
        super().__init__()
        self.dataset = dataset

    def list_attributes(self):
        return pd.DataFrame.from_records(self._fetch_attributes(),
                                         columns=["name",
                                                  "display_name",
                                                  "description"])

    def _fetch_attributes(self):
        resp = self.get_sync(type="configuration", dataset=self.dataset)
        xml = ET.fromstring(resp.content)
        attribs = list(zip(*self._attributes_from_xml(xml)))

        return {"name": attribs[0],
                "display_name": attribs[1],
                "description": attribs[2]}

    def _attributes_from_xml(self, xml):
        for page in xml.iter("AttributePage"):
            for desc in page.iter("AttributeDescription"):
                attrib = desc.attrib

                yield (attrib["internalName"],
                       attrib.get("displayName", ""),
                       attrib.get("description", ""))


class FiltersServer(Server):
    def __init__(self, dataset: str):
        super().__init__()
        self.dataset = dataset

    def list_filters(self):
        return pd.DataFrame.from_records(self._fetch_filters(),
                                         columns=["name", "type", "description"])

    def _fetch_filters(self):
        resp = self.get_sync(type="configuration", dataset=self.dataset)
        xml = ET.fromstring(resp.content)
        filters = list(zip(*self._filters_from_xml(xml)))

        return {"name": filters[0],
                "type": filters[1],
                "description": filters[2]}

    def _filters_from_xml(self, xml):
        for node in xml.iter("FilterDescription"):
            filt = node.attrib
            yield (filt["internalName"],
                   filt.get("type", ""),
                   filt.get("description", ""))


