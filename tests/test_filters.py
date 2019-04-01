#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import pytest
from pandas.testing import assert_frame_equal
from apybiomart import list_filters


def test_list_filters_default(df_filters_ensembl_hsapiens_gene):
    """
    Test the available filters returned by list_filters() for the
    default dataset (hsapiens_gene_ensembl).
    """
    expect = (df_filters_ensembl_hsapiens_gene
              .sort_values(by="name", axis=0)
              .reset_index(drop=True))
    result = (list_filters()
              .sort_values(by="name", axis=0)
              .reset_index(drop=True))

    assert_frame_equal(result, expect)


def test_list_filters_ensembl(df_filters_ensembl_hsapiens_gene):
    """
    Test the available filters returned by list_filters() for the
    hsapiens_gene_ensembl dataset.
    """
    expect = (df_filters_ensembl_hsapiens_gene
              .sort_values(by="name", axis=0)
              .reset_index(drop=True))
    result = (list_filters("hsapiens_gene_ensembl")
              .sort_values(by="name", axis=0)
              .reset_index(drop=True))

    assert_frame_equal(result, expect)


def test_list_filters_mouse(df_filters_mouse_mlpj_gene):
    """
    Test the available filters returned by list_filters() for the
    mlpj_gene_ensembl dataset.
    """
    expect = (df_filters_mouse_mlpj_gene
              .sort_values(by="name", axis=0)
              .reset_index(drop=True))
    result = (list_filters("mlpj_gene_ensembl")
              .sort_values(by="name", axis=0)
              .reset_index(drop=True))

    assert_frame_equal(result, expect)


def test_list_filters_sequence(df_filters_sequence_cdingo_genomic):
    """
    Test the available filters returned by list_filters() for the
    cdingo_genomic_sequence dataset.
    """
    expect = (df_filters_sequence_cdingo_genomic
              .sort_values(by="name", axis=0)
              .reset_index(drop=True))
    result = (list_filters("cdingo_genomic_sequence")
              .sort_values(by="name", axis=0)
              .reset_index(drop=True))

    assert_frame_equal(result, expect)


def test_list_filters_ontology(df_filters_ontology_closure_eco):
    """
    Test the available filters returned by list_filters() for the
    closure_ECO dataset.
    """
    expect = (df_filters_ontology_closure_eco
              .sort_values(by="name", axis=0)
              .reset_index(drop=True))
    result = (list_filters("closure_ECO")
              .sort_values(by="name", axis=0)
              .reset_index(drop=True))

    assert_frame_equal(result, expect)


def test_list_filters_genomic(df_filters_genomic_hsapiens_encode):
    """
    Test the available filters returned by list_filters() for the
    hsapiens_encode dataset.
    """
    expect = (df_filters_genomic_hsapiens_encode
              .sort_values(by="name", axis=0)
              .reset_index(drop=True))
    result = (list_filters("hsapiens_encode")
              .sort_values(by="name", axis=0)
              .reset_index(drop=True))

    assert_frame_equal(result, expect)


def test_list_filters_snp(df_filters_snp_chircus_snp):
    """
    Test the available filters returned by list_filters() for the
    chircus_snp dataset.
    """
    expect = (df_filters_snp_chircus_snp
              .sort_values(by="name", axis=0)
              .reset_index(drop=True))
    result = (list_filters("chircus_snp")
              .sort_values(by="name", axis=0)
              .reset_index(drop=True))

    assert_frame_equal(result, expect)


def test_list_filters_funcgen(df_filters_funcgen_hsapiens_peak):
    """
    Test the available filters returned by list_filters() for the
    hsapiens_peak dataset.
    """
    expect = (df_filters_funcgen_hsapiens_peak
              .sort_values(by="name", axis=0)
              .reset_index(drop=True))
    result = (list_filters("hsapiens_peak")
              .sort_values(by="name", axis=0)
              .reset_index(drop=True))

    assert_frame_equal(result, expect)
