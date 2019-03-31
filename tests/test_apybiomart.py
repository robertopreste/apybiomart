#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import pytest
from pandas.testing import assert_frame_equal
from apybiomart import list_marts, list_datasets


def test_list_marts(df_marts):
    """
    Test the available marts returned by list_marts().
    """
    expect = df_marts
    result = list_marts()

    assert_frame_equal(result.reset_index(drop=True),
                       expect.reset_index(drop=True),
                       check_like=True)


def test_list_datasets_default(df_datasets_ensembl_head):
    """
    Test the available datasets returned by list_datasets() for the
    default mart (ENSEMBL_MART_ENSEMBL).
    """
    expect = df_datasets_ensembl_head
    result = list_datasets()

    assert_frame_equal(result.reset_index(drop=True),
                       expect.reset_index(drop=True),
                       check_like=True)


def test_list_datasets_ensembl(df_datasets_ensembl_head):
    """
    Test the available datasets returned by list_datasets() for the
    ENSEMBL_MART_ENSEMBL mart.
    """
    expect = df_datasets_ensembl_head
    result = list_datasets("ENSEMBL_MART_ENSEMBL")

    assert_frame_equal(result.reset_index(drop=True),
                       expect.reset_index(drop=True),
                       check_like=True)
