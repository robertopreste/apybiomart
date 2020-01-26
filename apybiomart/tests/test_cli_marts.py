#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import pytest
from click.testing import CliRunner

from apybiomart import cli


def test_cli_marts():
    """Test the available marts returned by apybiomart marts."""
    runner = CliRunner()
    result = runner.invoke(cli.main, ["marts"])
    assert result.exit_code == 0
    assert "Mart ID" in result.output
    assert "ENSEMBL_MART_ENSEMBL" in result.output
    assert "Ensembl Genes 99" in result.output
