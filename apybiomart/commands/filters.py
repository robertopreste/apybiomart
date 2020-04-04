#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import click
import pandas as pd

from apybiomart.apybiomart import find_filters


@click.command("filters")
@click.option("--dataset", default="hsapiens_gene_ensembl", type=str,
              help="BioMart dataset name", show_default=True)
@click.option("--save", "-s", default=False, is_flag=True,
              help="Save results to a CSV file", show_default=True)
@click.option("--output", "-o", default="apybiomart_filters.csv", type=str,
              help="Output filename if saving results", show_default=True)
def cli_filters(dataset, save, output):
    """Retrieve and list available filters for a given mart."""
    pd.set_option("max_rows", 999)
    filters = find_filters(dataset, save=save, output=output)
    filters.columns = [col.replace("_", " ") for col in filters.columns]
    click.echo(filters)
    return 0
