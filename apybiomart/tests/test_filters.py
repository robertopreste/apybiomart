#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import os

import pandas as pd
from pandas.testing import assert_frame_equal
import pytest  # noqa

from apybiomart import find_filters


def test_find_filters_default(df_filters_ensembl_hsapiens_gene):
    """Test the available filters returned by find_filters() for the
    default dataset (hsapiens_gene_ensembl)."""
    expect = (df_filters_ensembl_hsapiens_gene
              .sort_values(by="Filter_ID", axis=0)
              .reset_index(drop=True))
    result = (find_filters()
              .sort_values(by="Filter_ID", axis=0)
              .reset_index(drop=True))

    assert_frame_equal(result, expect)


def test_find_filters_save(df_filters_ensembl_hsapiens_gene):
    """Test the available filters returned by find_filters(save=True) for the
    default dataset (hsapiens_gene_ensembl)."""
    expect = (df_filters_ensembl_hsapiens_gene
              .sort_values(by="Filter_ID", axis=0)
              .reset_index(drop=True))
    _ = find_filters(save=True)
    saved = pd.read_csv("apybiomart_filters.csv")
    result = (saved
              .replace(pd.np.nan, "")
              .sort_values(by="Filter_ID", axis=0)
              .reset_index(drop=True))

    try:
        assert_frame_equal(result, expect)
    finally:
        os.remove("apybiomart_filters.csv")


def test_find_filters_output(df_filters_ensembl_hsapiens_gene):
    """Test the available filters returned by find_filters with a given
    filename for the default dataset (hsapiens_gene_ensembl)."""
    expect = (df_filters_ensembl_hsapiens_gene
              .sort_values(by="Filter_ID", axis=0)
              .reset_index(drop=True))
    _ = find_filters(save=True, output="tested.csv")
    saved = pd.read_csv("tested.csv")
    result = (saved
              .replace(pd.np.nan, "")
              .sort_values(by="Filter_ID", axis=0)
              .reset_index(drop=True))

    try:
        assert_frame_equal(result, expect)
    finally:
        os.remove("tested.csv")


def test_find_filters_ensembl(df_filters_ensembl_hsapiens_gene):
    """Test the available filters returned by find_filters() for the
    hsapiens_gene_ensembl dataset."""
    expect = (df_filters_ensembl_hsapiens_gene
              .sort_values(by="Filter_ID", axis=0)
              .reset_index(drop=True))
    result = (find_filters("hsapiens_gene_ensembl")
              .sort_values(by="Filter_ID", axis=0)
              .reset_index(drop=True))

    assert_frame_equal(result, expect)


def test_find_filters_ontology(df_filters_ontology_closure_eco):
    """Test the available filters returned by find_filters() for the
    closure_ECO dataset."""
    expect = (df_filters_ontology_closure_eco
              .sort_values(by="Filter_ID", axis=0)
              .reset_index(drop=True))
    result = (find_filters("closure_ECO")
              .sort_values(by="Filter_ID", axis=0)
              .reset_index(drop=True))

    assert_frame_equal(result, expect)


def test_find_filters_genomic(df_filters_genomic_hsapiens_encode):
    """Test the available filters returned by find_filters() for the
    hsapiens_encode dataset."""
    expect = (df_filters_genomic_hsapiens_encode
              .sort_values(by="Filter_ID", axis=0)
              .reset_index(drop=True))
    result = (find_filters("hsapiens_encode")
              .sort_values(by="Filter_ID", axis=0)
              .reset_index(drop=True))

    assert_frame_equal(result, expect)


def test_find_filters_snp(df_filters_snp_chircus_snp):
    """Test the available filters returned by find_filters() for the
    chircus_snp dataset."""
    expect = (df_filters_snp_chircus_snp
              .sort_values(by="Filter_ID", axis=0)
              .reset_index(drop=True))
    result = (find_filters("chircus_snp")
              .sort_values(by="Filter_ID", axis=0)
              .reset_index(drop=True))

    assert_frame_equal(result, expect)


def test_find_filters_funcgen(df_filters_funcgen_hsapiens_peak):
    """Test the available filters returned by find_filters() for the
    hsapiens_peak dataset."""
    expect = (df_filters_funcgen_hsapiens_peak
              .sort_values(by="Filter_ID", axis=0)
              .reset_index(drop=True))
    result = (find_filters("hsapiens_peak")
              .sort_values(by="Filter_ID", axis=0)
              .reset_index(drop=True))

    assert_frame_equal(result, expect)
