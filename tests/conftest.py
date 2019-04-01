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
    df = pd.read_pickle(os.path.join(DATADIR, "marts.pkl"))
    return df


@pytest.fixture
def df_datasets_ensembl() -> pd.DataFrame:
    """
    Dataframe with available datasets for the default mart
    (ENSEMBL_MART_ENSEMBL).
    :return: pd.DataFrame
    """
    df = pd.read_pickle(os.path.join(DATADIR, "datasets_ensembl.pkl"))
    return df


@pytest.fixture
def df_datasets_mouse() -> pd.DataFrame:
    """
    Dataframe with available datasets for the ENSEMBL_MART_MOUSE mart.
    :return: pd.DataFrame
    """
    df = pd.read_pickle(os.path.join(DATADIR, "datasets_mouse.pkl"))
    return df


@pytest.fixture
def df_datasets_sequence() -> pd.DataFrame:
    """
    Dataframe with available datasets for the ENSEMBL_MART_SEQUENCE mart.
    :return: pd.DataFrame
    """
    df = pd.read_pickle(os.path.join(DATADIR, "datasets_sequence.pkl"))
    return df


@pytest.fixture
def df_datasets_ontology() -> pd.DataFrame:
    """
    Dataframe with available datasets for the ENSEMBL_MART_ONTOLOGY mart.
    :return: pd.DataFrame
    """
    df = pd.read_pickle(os.path.join(DATADIR, "datasets_ontology.pkl"))
    return df


@pytest.fixture
def df_datasets_genomic() -> pd.DataFrame:
    """
    Dataframe with available datasets for the ENSEMBL_MART_GENOMIC mart.
    :return: pd.DataFrame
    """
    df = pd.read_pickle(os.path.join(DATADIR, "datasets_genomic.pkl"))
    return df


@pytest.fixture
def df_datasets_snp() -> pd.DataFrame:
    """
    Dataframe with available datasets for the ENSEMBL_MART_SNP mart.
    :return: pd.DataFrame
    """
    df = pd.read_pickle(os.path.join(DATADIR, "datasets_snp.pkl"))
    return df


@pytest.fixture
def df_datasets_funcgen() -> pd.DataFrame:
    """
    Dataframe with available datasets for the ENSEMBL_MART_FUNCGEN mart.
    :return: pd.DataFrame
    """
    df = pd.read_pickle(os.path.join(DATADIR, "datasets_funcgen.pkl"))
    return df


@pytest.fixture
def df_attributes_ensembl_hsapiens_gene() -> pd.DataFrame:
    """
    Dataframe with available attributes for the hsapiens_gene_ensembl
    dataset.
    :return: pd.DataFrame
    """
    df = pd.read_pickle(os.path.join(DATADIR,
                                     "attributes_hsapiens_gene_ensembl.pkl"))
    return df


@pytest.fixture
def df_attributes_mouse_mlpj_gene() -> pd.DataFrame:
    """
    Dataframe with available attributes for the mlpj_gene_ensembl dataset.
    :return: pd.DataFrame
    """
    df = pd.read_pickle(os.path.join(DATADIR,
                                     "attributes_mlpj_gene_ensembl.pkl"))
    return df


@pytest.fixture
def df_attributes_sequence_cdingo_genomic() -> pd.DataFrame:
    """
    Dataframe with available attributes for the cdingo_genomic_sequence
    dataset
    :return: pd.DataFrame
    """
    df = pd.read_pickle(os.path.join(DATADIR,
                                     "attributes_cdingo_genomic_sequence.pkl"))
    return df
