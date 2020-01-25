#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import click
import pandas as pd

from apybiomart.apybiomart import find_datasets


@click.command("datasets")
@click.option("--mart", default="ENSEMBL_MART_ENSEMBL", type=str,
              help="BioMart mart name (default: 'ENSEMBL_MART_ENSEMBL')")
def cli_datasets(mart):
    """Retrieve and list available datasets for a given mart."""
    pd.set_option("max_rows", 999)
    datasets = find_datasets(mart)
    datasets.columns = [col.replace("_", " ") for col in datasets.columns]
    click.echo(datasets)
    return 0
