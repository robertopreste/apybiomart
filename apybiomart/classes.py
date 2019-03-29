#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import asyncio
import aiohttp
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
        return pd.DataFrame.from_records(self._fetch_marts())
    
    def _fetch_marts(self):
        resp = self.get_sync(type="registry")
        xml = ET.fromstring(resp.content)
        # TODO: will need to change this double call to xml.findall()
        names = [self._mart_name_from_xml(child)
                 for child in xml.findall("MartURLLocation")]
        displays = [self._mart_display_from_xml(child)
                    for child in xml.findall("MartURLLocation")]

        return {"name": names, "display_name": displays}

    def _mart_name_from_xml(self, node):
        return node.attrib["name"]

    def _mart_display_from_xml(self, node):
        return node.attrib["displayName"]
        

class DatasetServer(Server): 
    def __init__(self):
        super().__init__()
        pass





