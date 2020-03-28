#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import os
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


def test_cli_marts_save():
    """Test the available marts saved by apybiomart marts."""
    runner = CliRunner()
    result = runner.invoke(cli.main, ["marts", "--save"])
    try:
        assert result.exit_code == 0
        assert os.path.isfile("apybiomart_marts.csv")
    finally:
        os.remove("apybiomart_marts.csv")


def test_cli_marts_output():
    """Test the available marts saved by apybiomart marts with a given
    filename."""
    runner = CliRunner()
    result = runner.invoke(cli.main, ["marts", "--save",
                                      "--output", "tested.csv"])
    try:
        assert result.exit_code == 0
        assert os.path.isfile("tested.csv")
    finally:
        os.remove("tested.csv")
