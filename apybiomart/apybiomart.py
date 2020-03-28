#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import pandas as pd
from typing import List, Dict, Union
from .classes import MartServer, DatasetServer, AttributesServer, \
    FiltersServer, Query


def find_marts(save: bool = False,
               output: str = "apybiomart_marts.csv") -> pd.DataFrame:
    """Retrieve and list available marts.

    Args:
        save: save results to a CSV file [default: False]
        output: output filename if saving results
            [default: 'apybiomart_marts.csv']
    """
    server = MartServer(save=save, output=output)
    return server.find_marts()


def find_datasets(mart: str = "ENSEMBL_MART_ENSEMBL",
                  save: bool = False,
                  output: str = "apybiomart_datasets.csv") -> pd.DataFrame:
    """Retrieve and list available datasets for a given mart.

    Args:
        mart: BioMart mart name (default: "ENSEMBL_MART_ENSEMBL")
        save: save results to a CSV file [default: False]
        output: output filename if saving results
            [default: 'apybiomart_datasets.csv']
    """
    server = DatasetServer(mart, save=save, output=output)
    return server.find_datasets()


def find_attributes(dataset: str = "hsapiens_gene_ensembl",
                    save: bool = False,
                    output: str = "apybiomart_attributes.csv") -> pd.DataFrame:
    """Retrieve and list available attributes for a given mart.

    Args:
        dataset: BioMart dataset name (default: "hsapiens_gene_ensembl")
        save: save results to a CSV file [default: False]
        output: output filename if saving results
            [default: 'apybiomart_attributes.csv']
    """
    server = AttributesServer(dataset, save=save, output=output)
    return server.find_attributes()


def find_filters(dataset: str = "hsapiens_gene_ensembl",
                 save: bool = False,
                 output: str = "apybiomart_filters.csv") -> pd.DataFrame:
    """Retrieve and list available filters for a given mart.

    Args:
        dataset: BioMart dataset name (default: "hsapiens_gene_ensembl")
        save: save results to a CSV file [default: False]
        output: output filename if saving results
            [default: 'apybiomart_filters.csv']
    """
    server = FiltersServer(dataset, save=save, output=output)
    return server.find_filters()


def query(attributes: List[str],
          filters: Dict[str, Union[str, int, list, tuple, bool]],
          dataset: str = "hsapiens_gene_ensembl",
          save: bool = False,
          output: str = "apybiomart_query.csv") -> pd.DataFrame:
    """Launch synchronous query using the given attributes, filters and dataset.

    Args:
        attributes: list of attributes to include
        filters: dict of filter name : value to filter results
        dataset: BioMart dataset name (default: "hsapiens_gene_ensembl")
        save: save results to a CSV file [default: False]
        output: output filename if saving results
            [default: 'apybiomart_query.csv']
    """
    server = Query(attributes, filters, dataset, save=save, output=output)
    return server.query()


async def aquery(attributes: List[str],
                 filters: Dict[str, Union[str, int, list, tuple, bool]],
                 dataset: str = "hsapiens_gene_ensembl",
                 save: bool = False,
                 output: str = "apybiomart_aquery.csv") -> pd.DataFrame:
    """Launch asynchronous query using the given attributes, filters and dataset.

    Args:
        attributes: list of attributes to include
        filters: dict of filter name : value to filter results
        dataset: BioMart dataset name (default: "hsapiens_gene_ensembl")
        save: save results to a CSV file [default: False]
        output: output filename if saving results
            [default: 'apybiomart_aquery.csv']
    """
    server = Query(attributes, filters, dataset, save=save, output=output)
    return await server.aquery()
