#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import pytest
import asyncio
from pandas.testing import assert_frame_equal
from apybiomart import aquery


def test_aquery_default(df_query_ensembl_hsapiens_gene_chrom_2):
    """
    Test the async query results for the default dataset
    (hsapiens_gene_ensembl).
    """
    expect = (df_query_ensembl_hsapiens_gene_chrom_2
              # .sort_values(by="name", axis=0)
              .reset_index(drop=True))

    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(
        aquery(attributes=["ensembl_gene_id", "external_gene_name"],
               filters={"chromosome_name": "2"})
    ).reset_index(drop=True)

    assert_frame_equal(result, expect)


def test_aquery_ensembl(df_query_ensembl_hsapiens_gene_chrom_2):
    """
    Test the async query results for the hsapiens_gene_ensembl dataset.
    """
    expect = (df_query_ensembl_hsapiens_gene_chrom_2
              # .sort_values(by="name", axis=0)
              .reset_index(drop=True))

    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(
        aquery(attributes=["ensembl_gene_id", "external_gene_name"],
               filters={"chromosome_name": "2"},
               dataset="hsapiens_gene_ensembl")
    ).reset_index(drop=True)

    assert_frame_equal(result, expect)


def test_aquery_ensembl_multi(df_query_ensembl_hsapiens_gene_chrom_1,
                              df_query_ensembl_hsapiens_gene_chrom_2,
                              df_query_ensembl_hsapiens_gene_chrom_3):
    """
    Test the async query results for multiple queries run in a loop for
    the hsapiens_gene_ensembl dataset.
    """
    expect1 = (df_query_ensembl_hsapiens_gene_chrom_1
               .reset_index(drop=True))
    expect2 = (df_query_ensembl_hsapiens_gene_chrom_2
               .reset_index(drop=True))
    expect3 = (df_query_ensembl_hsapiens_gene_chrom_3
               .reset_index(drop=True))

    loop = asyncio.get_event_loop()
    tasks = [aquery(attributes=["ensembl_gene_id", "external_gene_name"],
                    filters={"chromosome_name": "1"},
                    dataset="hsapiens_gene_ensembl"),
             aquery(attributes=["ensembl_gene_id", "external_gene_name"],
                    filters={"chromosome_name": "2"},
                    dataset="hsapiens_gene_ensembl"),
             aquery(attributes=["ensembl_gene_id", "external_gene_name"],
                    filters={"chromosome_name": "3"},
                    dataset="hsapiens_gene_ensembl")]
    result1, result2, result3 = loop.run_until_complete(asyncio.gather(*tasks))

    assert_frame_equal(result1, expect1)
    assert_frame_equal(result2, expect2)
    assert_frame_equal(result3, expect3)

