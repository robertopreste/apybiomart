#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
from typing import Optional, List, Dict, Union
from .classes import MartServer, DatasetServer, AttributesServer, \
    FiltersServer, Query


def list_marts():
    server = MartServer()
    return server.list_marts()


def list_datasets(mart: Optional[str] = "ENSEMBL_MART_ENSEMBL"):
    server = DatasetServer(mart)
    return server.list_datasets()


def list_attributes(dataset: Optional[str] = "hsapiens_gene_ensembl"):
    server = AttributesServer(dataset)
    return server.list_attributes()


def list_filters(dataset: Optional[str] = "hsapiens_gene_ensembl"):
    server = FiltersServer(dataset)
    return server.list_filters()


def query(attributes: List[str],
          filters: Dict[str, Union[str, List]],
          dataset: Optional[str] = "hsapiens_gene_ensembl"):
    server = Query(attributes, filters, dataset)
    return server.query()


async def aquery(attributes: List[str],
                 filters: Dict[str, Union[str, List]],
                 dataset: Optional[str] = "hsapiens_gene_ensembl"):
    server = Query(attributes, filters, dataset)
    return await server.aquery()
