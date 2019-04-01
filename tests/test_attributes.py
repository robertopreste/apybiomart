#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import pytest
from pandas.testing import assert_frame_equal
from apybiomart import list_attributes


def test_list_attributes_default(df_attributes_ensembl_hsapiens_gene):
    """
    Test the available attributes returned by list_attributes() for the
    default dataset (hsapiens_gene_ensembl).
    """
    expect = (df_attributes_ensembl_hsapiens_gene
              .sort_values(by="name", axis=0)
              .reset_index(drop=True))
    result = (list_attributes()
              .sort_values(by="name", axis=0)
              .reset_index(drop=True))

    assert_frame_equal(result, expect)


def test_list_attributes_ensembl(df_attributes_ensembl_hsapiens_gene):
    """
    Test the available attributes returned by list_attributes() for the
    hsapiens_gene_ensembl dataset.
    """
    expect = (df_attributes_ensembl_hsapiens_gene
              .sort_values(by="name", axis=0)
              .reset_index(drop=True))
    result = (list_attributes("hsapiens_gene_ensembl")
              .sort_values(by="name", axis=0)
              .reset_index(drop=True))

    assert_frame_equal(result, expect)


def test_list_attributes_mouse(df_attributes_mouse_mlpj_gene):
    """
    Test the available attributes returned by list_attributes() for the
    mlpj_gene_ensembl dataset.
    """
    expect = (df_attributes_mouse_mlpj_gene
              .sort_values(by="name", axis=0)
              .reset_index(drop=True))
    result = (list_attributes("mlpj_gene_ensembl")
              .sort_values(by="name", axis=0)
              .reset_index(drop=True))

    assert_frame_equal(result, expect)


def test_list_attributes_sequence(df_attributes_sequence_cdingo_genomic):
    """
    Test the available attributes returned by list_attributes() for the
    cdingo_genomic_sequence dataset.
    """
    expect = (df_attributes_sequence_cdingo_genomic
              .sort_values(by="name", axis=0)
              .reset_index(drop=True))
    result = (list_attributes("cdingo_genomic_sequence")
              .sort_values(by="name", axis=0)
              .reset_index(drop=True))

    assert_frame_equal(result, expect)


def test_list_attributes_ontology(df_attributes_ontology_closure_eco):
    """
    Test the available attributes returned by list_attributes() for the
    closure_ECO dataset.
    """
    expect = (df_attributes_ontology_closure_eco
              .sort_values(by="name", axis=0)
              .reset_index(drop=True))
    result = (list_attributes("closure_ECO")
              .sort_values(by="name", axis=0)
              .reset_index(drop=True))

    assert_frame_equal(result, expect)


def test_list_attributes_genomic(df_attributes_genomic_hsapiens_encode):
    """
    Test the available attributes returned by list_attributes() for the
    hsapiens_encode dataset.
    """
    expect = (df_attributes_genomic_hsapiens_encode
              .sort_values(by="name", axis=0)
              .reset_index(drop=True))
    result = (list_attributes("hsapiens_encode")
              .sort_values(by="name", axis=0)
              .reset_index(drop=True))

    assert_frame_equal(result, expect)


def test_list_attributes_snp(df_attributes_snp_chircus_snp):
    """
    Test the available attributes returned by list_attributes() for the
    chircus_snp dataset.
    """
    expect = (df_attributes_snp_chircus_snp
              .sort_values(by="name", axis=0)
              .reset_index(drop=True))
    result = (list_attributes("chircus_snp")
              .sort_values(by="name", axis=0)
              .reset_index(drop=True))

    assert_frame_equal(result, expect)


def test_list_attributes_funcgen(df_attributes_funcgen_hsapiens_peak):
    """
    Test the available attributes returned by list_attributes() for the
    hsapiens_peak dataset.
    """
    expect = (df_attributes_funcgen_hsapiens_peak
              .sort_values(by="name", axis=0)
              .reset_index(drop=True))
    result = (list_attributes("hsapiens_peak")
              .sort_values(by="name", axis=0)
              .reset_index(drop=True))

    assert_frame_equal(result, expect)
