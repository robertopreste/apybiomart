#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import os

import numpy as np
import pandas as pd
from pandas.testing import assert_frame_equal
import pytest  # noqa

from apybiomart import find_attributes


def test_find_attributes_default(df_attributes_ensembl_hsapiens_gene):
    """Test the available attributes returned by find_attributes() for the
    default dataset (hsapiens_gene_ensembl)."""
    expect = (df_attributes_ensembl_hsapiens_gene
              .sort_values(by="Attribute_ID", axis=0)
              .reset_index(drop=True))
    result = (find_attributes()
              .sort_values(by="Attribute_ID", axis=0)
              .reset_index(drop=True))

    assert_frame_equal(result, expect)


def test_find_attributes_save(df_attributes_ensembl_hsapiens_gene):
    """Test the available attributes returned by find_attributes(save=True)
    for the default dataset (hsapiens_gene_ensembl)."""
    expect = (df_attributes_ensembl_hsapiens_gene
              .sort_values(by="Attribute_ID", axis=0)
              .reset_index(drop=True))
    _ = find_attributes(save=True)
    saved = pd.read_csv("apybiomart_attributes.csv")
    result = (saved
              .replace(np.nan, "")
              .sort_values(by="Attribute_ID", axis=0)
              .reset_index(drop=True))

    try:
        assert_frame_equal(result, expect)
    finally:
        os.remove("apybiomart_attributes.csv")


def test_find_attributes_output(df_attributes_ensembl_hsapiens_gene):
    """Test the available attributes returned by find_attributes with a given
    filename for the default dataset (hsapiens_gene_ensembl)."""
    expect = (df_attributes_ensembl_hsapiens_gene
              .sort_values(by="Attribute_ID", axis=0)
              .reset_index(drop=True))
    _ = find_attributes(save=True, output="tested.csv")
    saved = pd.read_csv("tested.csv")
    result = (saved
              .replace(np.nan, "")
              .sort_values(by="Attribute_ID", axis=0)
              .reset_index(drop=True))

    try:
        assert_frame_equal(result, expect)
    finally:
        os.remove("tested.csv")


def test_find_attributes_ensembl(df_attributes_ensembl_hsapiens_gene):
    """Test the available attributes returned by find_attributes() for the
    hsapiens_gene_ensembl dataset."""
    expect = (df_attributes_ensembl_hsapiens_gene
              .sort_values(by="Attribute_ID", axis=0)
              .reset_index(drop=True))
    result = (find_attributes("hsapiens_gene_ensembl")
              .sort_values(by="Attribute_ID", axis=0)
              .reset_index(drop=True))

    assert_frame_equal(result, expect)


def test_find_attributes_ontology(df_attributes_ontology_closure_eco):
    """Test the available attributes returned by find_attributes() for the
    closure_ECO dataset."""
    expect = (df_attributes_ontology_closure_eco
              .sort_values(by="Attribute_ID", axis=0)
              .reset_index(drop=True))
    result = (find_attributes("closure_ECO")
              .sort_values(by="Attribute_ID", axis=0)
              .reset_index(drop=True))

    assert_frame_equal(result, expect)


def test_find_attributes_genomic(df_attributes_genomic_hsapiens_encode):
    """Test the available attributes returned by find_attributes() for the
    hsapiens_encode dataset."""
    expect = (df_attributes_genomic_hsapiens_encode
              .sort_values(by="Attribute_ID", axis=0)
              .reset_index(drop=True))
    result = (find_attributes("hsapiens_encode")
              .sort_values(by="Attribute_ID", axis=0)
              .reset_index(drop=True))

    assert_frame_equal(result, expect)


def test_find_attributes_snp(df_attributes_snp_chircus_snp):
    """Test the available attributes returned by find_attributes() for the
    chircus_snp dataset."""
    expect = (df_attributes_snp_chircus_snp
              .sort_values(by="Attribute_ID", axis=0)
              .reset_index(drop=True))
    result = (find_attributes("chircus_snp")
              .sort_values(by="Attribute_ID", axis=0)
              .reset_index(drop=True))

    assert_frame_equal(result, expect)


def test_find_attributes_funcgen(df_attributes_funcgen_hsapiens_peak):
    """Test the available attributes returned by find_attributes() for the
    hsapiens_peak dataset."""
    expect = (df_attributes_funcgen_hsapiens_peak
              .sort_values(by="Attribute_ID", axis=0)
              .reset_index(drop=True))
    result = (find_attributes("hsapiens_peak")
              .sort_values(by="Attribute_ID", axis=0)
              .reset_index(drop=True))

    assert_frame_equal(result, expect)
