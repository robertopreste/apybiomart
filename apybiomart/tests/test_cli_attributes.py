#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import os
import pytest

from click.testing import CliRunner

from apybiomart import cli


def test_cli_attributes_default():
    """Test the available attributes returned by apybiomart attributes for the
    default dataset (hsapiens_gene_ensembl)."""
    runner = CliRunner()
    result = runner.invoke(cli.main, ["attributes"])
    assert result.exit_code == 0
    assert "Attribute ID" in result.output
    assert "ensembl_gene_id" in result.output
    assert "hsapiens_gene_ensembl" in result.output


def test_cli_attributes_save():
    """Test the saved attributes returned by apybiomart attributes for the
    default dataset (hsapiens_gene_ensembl)."""
    runner = CliRunner()
    result = runner.invoke(cli.main, ["attributes", "--save"])
    try:
        assert result.exit_code == 0
        assert os.path.isfile("apybiomart_attributes.csv")
    finally:
        os.remove("apybiomart_attributes.csv")


def test_cli_attributes_output():
    """Test the saved attributes returned by apybiomart attributes with a
    given filename for the default dataset (hsapiens_gene_ensembl)."""
    runner = CliRunner()
    result = runner.invoke(cli.main, ["attributes", "--save",
                                      "--output", "tested.csv"])
    try:
        assert result.exit_code == 0
        assert os.path.isfile("tested.csv")
    finally:
        os.remove("tested.csv")


def test_cli_attributes_ontology():
    """Test the available attributes returned by apybiomart attributes for the
    closure_ECO dataset."""
    runner = CliRunner()
    result = runner.invoke(cli.main,
                           ["attributes",
                            "--dataset", "closure_ECO"])
    assert result.exit_code == 0
    assert "Attribute ID" in result.output
    assert "subsets_305" in result.output
    assert "closure_ECO" in result.output
