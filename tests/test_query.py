#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import pytest
from pandas.testing import assert_frame_equal
from apybiomart import query


def test_query_default(df_query_ensembl_hsapiens_gene_chrom_2):
    """
    Test the query results for the default dataset (hsapiens_gene_ensembl).
    """
    expect = (df_query_ensembl_hsapiens_gene_chrom_2
              # .sort_values(by="name", axis=0)
              .reset_index(drop=True))
    result = (query(attributes=["ensembl_gene_id", "external_gene_name"],
                    filters={"chromosome_name": "2"})
              # .sort_values(by="name", axis=0)
              .reset_index(drop=True))

    assert_frame_equal(result, expect)


def test_query_ensembl(df_query_ensembl_hsapiens_gene_chrom_2):
    """
    Test the query results for the hsapiens_gene_ensembl dataset.
    """
    expect = (df_query_ensembl_hsapiens_gene_chrom_2
              # .sort_values(by="name", axis=0)
              .reset_index(drop=True))
    result = (query(attributes=["ensembl_gene_id", "external_gene_name"],
                    filters={"chromosome_name": "2"},
                    dataset="hsapiens_gene_ensembl")
              # .sort_values(by="name", axis=0)
              .reset_index(drop=True))

    assert_frame_equal(result, expect)
