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
def df_datasets_ensembl() -> pd.DataFrame:
    """
    Dataframe with available datasets for the default mart
    (ENSEMBL_MART_ENSEMBL).
    :return: pd.DataFrame
    """
    df = pd.read_pickle(os.path.join(DATADIR, "list_datasets_ensembl.pkl"))
    return df


@pytest.fixture
def df_datasets_mouse() -> pd.DataFrame:
    """
    Dataframe with available datasets for the ENSEMBL_MART_MOUSE mart.
    :return: pd.DataFrame
    """
    df = pd.read_pickle(os.path.join(DATADIR, "list_datasets_mouse.pkl"))
    return df


@pytest.fixture
def df_datasets_sequence() -> pd.DataFrame:
    """
    Dataframe with available datasets for the ENSEMBL_MART_SEQUENCE mart.
    :return: pd.DataFrame
    """
    df = pd.read_pickle(os.path.join(DATADIR, "list_datasets_sequence.pkl"))
    return df


@pytest.fixture
def df_datasets_ontology() -> pd.DataFrame:
    """
    Dataframe with available datasets for the ENSEMBL_MART_ONTOLOGY mart.
    :return: pd.DataFrame
    """
    df = pd.read_pickle(os.path.join(DATADIR, "list_datasets_ontology.pkl"))
    return df


@pytest.fixture
def df_datasets_genomic() -> pd.DataFrame:
    """
    Dataframe with available datasets for the ENSEMBL_MART_GENOMIC mart.
    :return: pd.DataFrame
    """
    df = pd.read_pickle(os.path.join(DATADIR, "list_datasets_genomic.pkl"))
    return df


@pytest.fixture
def df_datasets_snp() -> pd.DataFrame:
    """
    Dataframe with available datasets for the ENSEMBL_MART_SNP mart.
    :return: pd.DataFrame
    """
    df = pd.read_pickle(os.path.join(DATADIR, "list_datasets_snp.pkl"))
    return df


@pytest.fixture
def df_datasets_funcgen() -> pd.DataFrame:
    """
    Dataframe with available datasets for the ENSEMBL_MART_FUNCGEN mart.
    :return: pd.DataFrame
    """
    df = pd.read_pickle(os.path.join(DATADIR, "list_datasets_funcgen.pkl"))
    return df
