#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import sys

import click

from apybiomart.commands.attributes import cli_attributes
from apybiomart.commands.datasets import cli_datasets
from apybiomart.commands.filters import cli_filters
from apybiomart.commands.marts import cli_marts


@click.group()
@click.version_option()
def main():
    """Async pythonic interface to BioMart."""
    pass


main.add_command(cli_marts)
main.add_command(cli_datasets)
main.add_command(cli_attributes)
main.add_command(cli_filters)


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
