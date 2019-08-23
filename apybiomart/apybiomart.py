#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import pandas as pd
from typing import List, Dict, Union
from .classes import MartServer, DatasetServer, AttributesServer, \
    FiltersServer, Query


def find_marts() -> pd.DataFrame:
    """Retrieve and list available marts."""
    server = MartServer()
    return server.find_marts()


def find_datasets(mart: str = "ENSEMBL_MART_ENSEMBL") -> pd.DataFrame:
    """Retrieve and list available datasets for a given mart.

    Args:
        mart: BioMart mart name (default: "ENSEMBL_MART_ENSEMBL")
    """
    server = DatasetServer(mart)
    return server.find_datasets()


def find_attributes(dataset: str = "hsapiens_gene_ensembl") -> pd.DataFrame:
    """Retrieve and list available attributes for a given mart.

    Args:
        dataset: BioMart dataset name (default: "hsapiens_gene_ensembl")
    """
    server = AttributesServer(dataset)
    return server.find_attributes()


def find_filters(dataset: str = "hsapiens_gene_ensembl") -> pd.DataFrame:
    """Retrieve and list available filters for a given mart.

    Args:
        dataset: BioMart dataset name (default: "hsapiens_gene_ensembl")
    """
    server = FiltersServer(dataset)
    return server.find_filters()


def query(attributes: List[str],
          filters: Dict[str, Union[str, int, list, tuple, bool]],
          dataset: str = "hsapiens_gene_ensembl") -> pd.DataFrame:
    """Launch synchronous query using the given attributes, filters and dataset.

    Args:
        attributes: list of attributes to include
        filters: dict of filter name : value to filter results
        dataset: BioMart dataset name (default: "hsapiens_gene_ensembl")
    """
    server = Query(attributes, filters, dataset)
    return server.query()


async def aquery(attributes: List[str],
                 filters: Dict[str, Union[str, int, list, tuple, bool]],
                 dataset: str = "hsapiens_gene_ensembl") -> pd.DataFrame:
    """Launch asynchronous query using the given attributes, filters and dataset.

    Args:
        attributes: list of attributes to include
        filters: dict of filter name : value to filter results
        dataset: BioMart dataset name (default: "hsapiens_gene_ensembl")
    """
    server = Query(attributes, filters, dataset)
    return await server.aquery()
