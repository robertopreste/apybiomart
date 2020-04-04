#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import click
import pandas as pd

from apybiomart.apybiomart import find_datasets


@click.command("datasets")
@click.option("--mart", default="ENSEMBL_MART_ENSEMBL", type=str,
              help="BioMart mart name", show_default=True)
@click.option("--save", "-s", default=False, is_flag=True,
              help="Save results to a CSV file", show_default=True)
@click.option("--output", "-o", default="apybiomart_datasets.csv", type=str,
              help="Output filename if saving results", show_default=True)
def cli_datasets(mart, save, output):
    """Retrieve and list available datasets for a given mart."""
    pd.set_option("max_rows", 999)
    datasets = find_datasets(mart, save=save, output=output)
    datasets.columns = [col.replace("_", " ") for col in datasets.columns]
    click.echo(datasets)
    return 0
