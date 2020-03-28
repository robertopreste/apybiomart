#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import click
import pandas as pd

from apybiomart.apybiomart import find_marts


@click.command("marts")
@click.option("--save", "-s", default=False, is_flag=True,
              help="Save results to a CSV file", show_default=True)
@click.option("--output", "-o", default="apybiomart_marts.csv", type=str,
              help="Output filename if saving results", show_default=True)
def cli_marts(save, output):
    """Retrieve and list available marts."""
    pd.set_option("max_rows", 999)
    marts = find_marts(save=save, output=output)
    marts.columns = [col.replace("_", " ") for col in marts.columns]
    click.echo(marts)
    return 0
