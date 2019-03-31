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
    expect = (df_marts
              .sort_values(by="name", axis=0)
              .reset_index(drop=True))
    result = (list_marts()
              .sort_values(by="name", axis=0)
              .reset_index(drop=True))

    assert_frame_equal(result, expect)


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
