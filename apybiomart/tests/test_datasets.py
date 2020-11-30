#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import os

import numpy as np
import pandas as pd
from pandas.testing import assert_frame_equal
import pytest  # noqa

from apybiomart import find_datasets


def test_find_datasets_default(df_datasets_ensembl):
    """Test the available datasets returned by find_datasets() for the
    default mart (ENSEMBL_MART_ENSEMBL)."""
    expect = (df_datasets_ensembl
              .sort_values(by="Dataset_ID", axis=0)
              .reset_index(drop=True))
    result = (find_datasets()
              .sort_values(by="Dataset_ID", axis=0)
              .reset_index(drop=True))

    assert_frame_equal(result, expect)


def test_find_datasets_save(df_datasets_ensembl):
    """Test the available datasets returned by find_datasets(save=True) for
    the default mart (ENSEMBL_MART_ENSEMBL)."""
    expect = (df_datasets_ensembl
              .sort_values(by="Dataset_ID", axis=0)
              .reset_index(drop=True))
    _ = find_datasets(save=True)
    saved = pd.read_csv("apybiomart_datasets.csv")
    result = (saved
              .replace(np.nan, "")
              .sort_values(by="Dataset_ID", axis=0)
              .reset_index(drop=True))

    try:
        assert_frame_equal(result, expect)
    finally:
        os.remove("apybiomart_datasets.csv")


def test_find_datasets_output(df_datasets_ensembl):
    """Test the available datasets returned by find_datasets with a given
    filename for the default mart (ENSEMBL_MART_ENSEMBL)."""
    expect = (df_datasets_ensembl
              .sort_values(by="Dataset_ID", axis=0)
              .reset_index(drop=True))
    _ = find_datasets(save=True, output="tested.csv")
    saved = pd.read_csv("tested.csv")
    result = (saved
              .replace(np.nan, "")
              .sort_values(by="Dataset_ID", axis=0)
              .reset_index(drop=True))

    try:
        assert_frame_equal(result, expect)
    finally:
        os.remove("tested.csv")


def test_find_datasets_ensembl(df_datasets_ensembl):
    """Test the available datasets returned by find_datasets() for the
    ENSEMBL_MART_ENSEMBL mart."""
    expect = (df_datasets_ensembl
              .sort_values(by="Dataset_ID", axis=0)
              .reset_index(drop=True))
    result = (find_datasets("ENSEMBL_MART_ENSEMBL")
              .sort_values(by="Dataset_ID", axis=0)
              .reset_index(drop=True))

    assert_frame_equal(result, expect)


def test_find_datasets_mouse(df_datasets_mouse):
    """Test the available datasets returned by find_datasets() for the
    ENSEMBL_MART_MOUSE mart."""
    expect = (df_datasets_mouse
              .sort_values(by="Dataset_ID", axis=0)
              .reset_index(drop=True))
    result = (find_datasets("ENSEMBL_MART_MOUSE")
              .sort_values(by="Dataset_ID", axis=0)
              .reset_index(drop=True))

    assert_frame_equal(result, expect)


def test_find_datasets_sequence(df_datasets_sequence):
    """Test the available datasets returned by find_datasets() for the
    ENSEMBL_MART_SEQUENCE mart."""
    expect = (df_datasets_sequence
              .sort_values(by="Dataset_ID", axis=0)
              .reset_index(drop=True))
    result = (find_datasets("ENSEMBL_MART_SEQUENCE")
              .sort_values(by="Dataset_ID", axis=0)
              .reset_index(drop=True))

    assert_frame_equal(result, expect)


def test_find_datasets_ontology(df_datasets_ontology):
    """Test the available datasets returned by find_datasets() for the
    ENSEMBL_MART_ONTOLOGY mart."""
    expect = (df_datasets_ontology
              .sort_values(by="Dataset_ID", axis=0)
              .reset_index(drop=True))
    result = (find_datasets("ENSEMBL_MART_ONTOLOGY")
              .sort_values(by="Dataset_ID", axis=0)
              .reset_index(drop=True))

    assert_frame_equal(result, expect)


def test_find_datasets_genomic(df_datasets_genomic):
    """Test the available datasets returned by find_datasets() for the
    ENSEMBL_MART_GENOMIC mart."""
    expect = (df_datasets_genomic
              .sort_values(by="Dataset_ID", axis=0)
              .reset_index(drop=True))
    result = (find_datasets("ENSEMBL_MART_GENOMIC")
              .sort_values(by="Dataset_ID", axis=0)
              .reset_index(drop=True))

    assert_frame_equal(result, expect)


def test_find_datasets_snp(df_datasets_snp):
    """Test the available datasets returned by find_datasets() for the
    ENSEMBL_MART_SNP mart."""
    expect = (df_datasets_snp
              .sort_values(by="Dataset_ID", axis=0)
              .reset_index(drop=True))
    result = (find_datasets("ENSEMBL_MART_SNP")
              .sort_values(by="Dataset_ID", axis=0)
              .reset_index(drop=True))

    assert_frame_equal(result, expect)


def test_find_datasets_funcgen(df_datasets_funcgen):
    """Test the available datasets returned by find_datasets() for the
    ENSEMBL_MART_FUNCGEN mart."""
    expect = (df_datasets_funcgen
              .sort_values(by="Dataset_ID", axis=0)
              .reset_index(drop=True))
    result = (find_datasets("ENSEMBL_MART_FUNCGEN")
              .sort_values(by="Dataset_ID", axis=0)
              .reset_index(drop=True))

    assert_frame_equal(result, expect)
