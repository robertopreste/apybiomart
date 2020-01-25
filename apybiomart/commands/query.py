#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import click
import pandas as pd

from apybiomart.apybiomart import query

@click.command("query")
@click.argument("attributes")
def cli_query():
    """Launch synchronous query using the given attributes, filters and dataset."""
