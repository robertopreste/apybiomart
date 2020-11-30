#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import os

import numpy as np
import pandas as pd
from pandas.testing import assert_frame_equal
import pytest  # noqa

from apybiomart import query


def test_query_default(df_query_ensembl_hsapiens_gene_chrom_2):
    """Test the query results for the default dataset
    (hsapiens_gene_ensembl)."""
    expect = (df_query_ensembl_hsapiens_gene_chrom_2
              .reset_index(drop=True))
    result = (query(attributes=["ensembl_gene_id", "external_gene_name"],
                    filters={"chromosome_name": "2"})
              .reset_index(drop=True))

    assert_frame_equal(result, expect)


def test_query_save(df_query_ensembl_hsapiens_gene_chrom_2):
    """Test the saved query results for the default dataset
    (hsapiens_gene_ensembl)."""
    expect = (df_query_ensembl_hsapiens_gene_chrom_2
              .reset_index(drop=True))
    _ = query(attributes=["ensembl_gene_id", "external_gene_name"],
              filters={"chromosome_name": "2"},
              save=True)
    saved = pd.read_csv("apybiomart_query.csv")
    result = (saved
              .replace(np.nan, "")
              .reset_index(drop=True))

    try:
        assert_frame_equal(result, expect)
    finally:
        os.remove("apybiomart_query.csv")


def test_query_output(df_query_ensembl_hsapiens_gene_chrom_2):
    """Test the saved query results with a given filename for the default
    dataset (hsapiens_gene_ensembl)."""
    expect = (df_query_ensembl_hsapiens_gene_chrom_2
              .reset_index(drop=True))
    _ = query(attributes=["ensembl_gene_id", "external_gene_name"],
              filters={"chromosome_name": "2"},
              save=True, output="tested.csv")
    saved = pd.read_csv("tested.csv")
    result = (saved
              .replace(np.nan, "")
              .reset_index(drop=True))

    try:
        assert_frame_equal(result, expect)
    finally:
        os.remove("tested.csv")


def test_query_default_int(df_query_ensembl_hsapiens_gene_chrom_2):
    """Test the query results for the default dataset (hsapiens_gene_ensembl)
    with int filters parameter."""
    expect = (df_query_ensembl_hsapiens_gene_chrom_2
              .reset_index(drop=True))
    result = (query(attributes=["ensembl_gene_id", "external_gene_name"],
                    filters={"chromosome_name": 2})
              .reset_index(drop=True))

    assert_frame_equal(result, expect)


def test_query_ensembl(df_query_ensembl_hsapiens_gene_chrom_2):
    """Test the query results for the hsapiens_gene_ensembl dataset."""
    expect = (df_query_ensembl_hsapiens_gene_chrom_2
              .reset_index(drop=True))
    result = (query(attributes=["ensembl_gene_id", "external_gene_name"],
                    filters={"chromosome_name": "2"},
                    dataset="hsapiens_gene_ensembl")
              .reset_index(drop=True))

    assert_frame_equal(result, expect)


def test_query_ensembl_int(df_query_ensembl_hsapiens_gene_chrom_2):
    """
    Test the query results for the hsapiens_gene_ensembl dataset with
    int filters parameter."""
    expect = (df_query_ensembl_hsapiens_gene_chrom_2
              .reset_index(drop=True))
    result = (query(attributes=["ensembl_gene_id", "external_gene_name"],
                    filters={"chromosome_name": 2},
                    dataset="hsapiens_gene_ensembl")
              .reset_index(drop=True))

    assert_frame_equal(result, expect)
