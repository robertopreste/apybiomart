#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import pandas as pd
from typing import List, Dict, Union
from .classes import MartServer, DatasetServer, AttributesServer, \
    FiltersServer, Query


def find_marts(save: bool = False) -> pd.DataFrame:
    """Retrieve and list available marts.

    Args:
        save: save results to a CSV file [default: False]
    """
    server = MartServer(save=save)
    return server.find_marts()


def find_datasets(mart: str = "ENSEMBL_MART_ENSEMBL",
                  save: bool = False) -> pd.DataFrame:
    """Retrieve and list available datasets for a given mart.

    Args:
        mart: BioMart mart name (default: "ENSEMBL_MART_ENSEMBL")
        save: save results to a CSV file [default: False]
    """
    server = DatasetServer(mart, save=save)
    return server.find_datasets()


def find_attributes(dataset: str = "hsapiens_gene_ensembl",
                    save: bool = False) -> pd.DataFrame:
    """Retrieve and list available attributes for a given mart.

    Args:
        dataset: BioMart dataset name (default: "hsapiens_gene_ensembl")
        save: save results to a CSV file [default: False]
    """
    server = AttributesServer(dataset, save=save)
    return server.find_attributes()


def find_filters(dataset: str = "hsapiens_gene_ensembl",
                 save: bool = False) -> pd.DataFrame:
    """Retrieve and list available filters for a given mart.

    Args:
        dataset: BioMart dataset name (default: "hsapiens_gene_ensembl")
        save: save results to a CSV file [default: False]
    """
    server = FiltersServer(dataset, save=save)
    return server.find_filters()


def query(attributes: List[str],
          filters: Dict[str, Union[str, int, list, tuple, bool]],
          dataset: str = "hsapiens_gene_ensembl",
          save: bool = False) -> pd.DataFrame:
    """Launch synchronous query using the given attributes, filters and dataset.

    Args:
        attributes: list of attributes to include
        filters: dict of filter name : value to filter results
        dataset: BioMart dataset name (default: "hsapiens_gene_ensembl")
        save: save results to a CSV file [default: False]
    """
    server = Query(attributes, filters, dataset, save=save)
    return server.query()


async def aquery(attributes: List[str],
                 filters: Dict[str, Union[str, int, list, tuple, bool]],
                 dataset: str = "hsapiens_gene_ensembl",
                 save: bool = False) -> pd.DataFrame:
    """Launch asynchronous query using the given attributes, filters and dataset.

    Args:
        attributes: list of attributes to include
        filters: dict of filter name : value to filter results
        dataset: BioMart dataset name (default: "hsapiens_gene_ensembl")
        save: save results to a CSV file [default: False]
    """
    server = Query(attributes, filters, dataset, save=save)
    return await server.aquery()
