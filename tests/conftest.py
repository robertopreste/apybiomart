#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import pytest
import pickle
import os
import pandas as pd

DATADIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data")


@pytest.fixture
def df_marts() -> pd.DataFrame:
    """
    Dataframe with available marts from Biomart.
    :return: pd.DataFrame
    """
    df = pd.read_pickle(os.path.join(DATADIR, "list_marts.pkl"))
    return df


@pytest.fixture
def df_datasets_ensembl_head() -> pd.DataFrame:
    """
    Dataframe with available datasets for the default mart
    (ENSEMBL_MART_ENSEMBL).
    :return: pd.DataFrame
    """
    df = pd.read_pickle(os.path.join(DATADIR, "list_datasets_ensembl.pkl"))
    return df


