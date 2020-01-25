#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import click
import pandas as pd

from apybiomart.apybiomart import find_attributes


@click.command("attributes")
@click.option("--dataset", default="hsapiens_gene_ensembl", type=str,
              help="BioMart dataset name (default: 'hsapiens_gene_ensembl')")
def cli_attributes(dataset):
    """Retrieve and list available attributes for a given mart."""
    pd.set_option("max_rows", 999)
    attributes = find_attributes(dataset)
    attributes.columns = [col.replace("_", " ") for col in attributes.columns]
    click.echo(attributes)
    return 0
