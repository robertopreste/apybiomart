#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import os

import pandas as pd
from pandas.testing import assert_frame_equal
import pytest  # noqa

from apybiomart import find_marts


def test_find_marts(df_marts):
    """Test the available marts returned by find_marts()."""
    expect = (df_marts
              .sort_values(by="Mart_ID", axis=0)
              .reset_index(drop=True))
    result = (find_marts()
              .sort_values(by="Mart_ID", axis=0)
              .reset_index(drop=True))

    assert_frame_equal(result, expect)


def test_find_marts_save(df_marts):
    """Test the available marts returned by find_marts(save=True)."""
    expect = (df_marts
              .sort_values(by="Mart_ID", axis=0)
              .reset_index(drop=True))
    _ = find_marts(save=True)
    saved = pd.read_csv("apybiomart_marts.csv")
    result = (saved
              .replace(pd.np.nan, "")
              .sort_values(by="Mart_ID", axis=0)
              .reset_index(drop=True))

    try:
        assert_frame_equal(result, expect)
    finally:
        os.remove("apybiomart_marts.csv")


def test_find_marts_output(df_marts):
    """Test the available marts returned by find_marts with a given
    filename."""
    expect = (df_marts
              .sort_values(by="Mart_ID", axis=0)
              .reset_index(drop=True))
    _ = find_marts(save=True, output="tested.csv")
    saved = pd.read_csv("tested.csv")
    result = (saved
              .replace(pd.np.nan, "")
              .sort_values(by="Mart_ID", axis=0)
              .reset_index(drop=True))

    try:
        assert_frame_equal(result, expect)
    finally:
        os.remove("tested.csv")
