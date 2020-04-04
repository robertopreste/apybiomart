#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import os
import pytest

from click.testing import CliRunner

from apybiomart import cli


def test_cli_datasets_default():
    """Test the available datasets returned by apybiomart datasets for the
    default mart (ENSEMBL_MART_ENSEMBL)."""
    runner = CliRunner()
    result = runner.invoke(cli.main, ["datasets"])
    assert result.exit_code == 0
    assert "Dataset ID" in result.output
    assert "ggallus_gene_ensembl" in result.output
    assert "ENSEMBL_MART_ENSEMBL" in result.output


def test_cli_datasets_save():
    """Test the saved datasets returned by apybiomart datasets for the
    default mart (ENSEMBL_MART_ENSEMBL)."""
    runner = CliRunner()
    result = runner.invoke(cli.main, ["datasets", "--save"])
    try:
        assert result.exit_code == 0
        assert os.path.isfile("apybiomart_datasets.csv")
    finally:
        os.remove("apybiomart_datasets.csv")


def test_cli_datasets_output():
    """Test the saved datasets returned by apybiomart datasets with a given
    filename for the default mart (ENSEMBL_MART_ENSEMBL)."""
    runner = CliRunner()
    result = runner.invoke(cli.main, ["datasets", "--save",
                                      "--output", "tested.csv"])
    try:
        assert result.exit_code == 0
        assert os.path.isfile("tested.csv")
    finally:
        os.remove("tested.csv")


def test_cli_datasets_mouse():
    """Test the available datasets returned by apybiomart datasets for the
    ENSEMBL_MART_MOUSE mart."""
    runner = CliRunner()
    result = runner.invoke(cli.main,
                           ["datasets",
                            "--mart", "ENSEMBL_MART_MOUSE"])
    assert result.exit_code == 0
    assert "Dataset ID" in result.output
    assert "mmnzohlltj_gene_ensembl" in result.output
    assert "ENSEMBL_MART_MOUSE" in result.output
