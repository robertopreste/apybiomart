#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import pytest
from pandas.testing import assert_frame_equal
from apybiomart import list_datasets


def test_list_datasets_default(df_datasets_ensembl):
    """
    Test the available datasets returned by list_datasets() for the
    default mart (ENSEMBL_MART_ENSEMBL).
    """
    expect = (df_datasets_ensembl
              .sort_values(by="name", axis=0)
              .reset_index(drop=True))
    result = (list_datasets()
              .sort_values(by="name", axis=0)
              .reset_index(drop=True))

    assert_frame_equal(result, expect)


def test_list_datasets_ensembl(df_datasets_ensembl):
    """
    Test the available datasets returned by list_datasets() for the
    ENSEMBL_MART_ENSEMBL mart.
    """
    expect = (df_datasets_ensembl
              .sort_values(by="name", axis=0)
              .reset_index(drop=True))
    result = (list_datasets("ENSEMBL_MART_ENSEMBL")
              .sort_values(by="name", axis=0)
              .reset_index(drop=True))

    assert_frame_equal(result, expect)


def test_list_datasets_mouse(df_datasets_mouse):
    """
    Test the available datasets returned by list_datasets() for the
    ENSEMBL_MART_MOUSE mart.
    """
    expect = (df_datasets_mouse
              .sort_values(by="name", axis=0)
              .reset_index(drop=True))
    result = (list_datasets("ENSEMBL_MART_MOUSE")
              .sort_values(by="name", axis=0)
              .reset_index(drop=True))

    assert_frame_equal(result, expect)


def test_list_datasets_sequence(df_datasets_sequence):
    """
    Test the available datasets returned by list_datasets() for the
    ENSEMBL_MART_SEQUENCE mart.
    """
    expect = (df_datasets_sequence
              .sort_values(by="name", axis=0)
              .reset_index(drop=True))
    result = (list_datasets("ENSEMBL_MART_SEQUENCE")
              .sort_values(by="name", axis=0)
              .reset_index(drop=True))

    assert_frame_equal(result, expect)


def test_list_datasets_ontology(df_datasets_ontology):
    """
    Test the available datasets returned by list_datasets() for the
    ENSEMBL_MART_ONTOLOGY mart.
    """
    expect = (df_datasets_ontology
              .sort_values(by="name", axis=0)
              .reset_index(drop=True))
    result = (list_datasets("ENSEMBL_MART_ONTOLOGY")
              .sort_values(by="name", axis=0)
              .reset_index(drop=True))

    assert_frame_equal(result, expect)


def test_list_datasets_genomic(df_datasets_genomic):
    """
    Test the available datasets returned by list_datasets() for the
    ENSEMBL_MART_GENOMIC mart.
    """
    expect = (df_datasets_genomic
              .sort_values(by="name", axis=0)
              .reset_index(drop=True))
    result = (list_datasets("ENSEMBL_MART_GENOMIC")
              .sort_values(by="name", axis=0)
              .reset_index(drop=True))

    assert_frame_equal(result, expect)


def test_list_datasets_snp(df_datasets_snp):
    """
    Test the available datasets returned by list_datasets() for the
    ENSEMBL_MART_SNP mart.
    """
    expect = (df_datasets_snp
              .sort_values(by="name", axis=0)
              .reset_index(drop=True))
    result = (list_datasets("ENSEMBL_MART_SNP")
              .sort_values(by="name", axis=0)
              .reset_index(drop=True))

    assert_frame_equal(result, expect)


def test_list_datasets_funcgen(df_datasets_funcgen):
    """
    Test the available datasets returned by list_datasets() for the
    ENSEMBL_MART_FUNCGEN mart.
    """
    expect = (df_datasets_funcgen
              .sort_values(by="name", axis=0)
              .reset_index(drop=True))
    result = (list_datasets("ENSEMBL_MART_FUNCGEN")
              .sort_values(by="name", axis=0)
              .reset_index(drop=True))

    assert_frame_equal(result, expect)
