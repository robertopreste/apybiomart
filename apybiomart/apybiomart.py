#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
from typing import Optional
from .classes import MartServer, DatasetServer


def list_marts():
    server = MartServer()
    return server.list_marts()


def list_datasets(mart: Optional[str] = "ENSEMBL_MART_ENSEMBL"):
    server = DatasetServer(mart)
    return server.list_datasets()
