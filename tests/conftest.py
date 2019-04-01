#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import pytest
import pickle
import os
import pandas as pd

DATADIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data")


# marts

@pytest.fixture
def df_marts() -> pd.DataFrame:
    """
    Dataframe with available marts from Biomart.
    :return: pd.DataFrame
    """
    df = pd.read_pickle(os.path.join(DATADIR, "marts.pkl"))
    return df


# datasets

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


# attributes

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
    dataset.
    :return: pd.DataFrame
    """
    df = pd.read_pickle(os.path.join(DATADIR,
                                     "attributes_cdingo_genomic_sequence.pkl"))
    return df


@pytest.fixture
def df_attributes_ontology_closure_eco() -> pd.DataFrame:
    """
    Dataframe with available attributes for the closure_ECO dataset.
    :return: pd.DataFrame
    """
    df = pd.read_pickle(os.path.join(DATADIR,
                                     "attributes_closure_ECO.pkl"))
    return df


@pytest.fixture
def df_attributes_genomic_hsapiens_encode() -> pd.DataFrame:
    """
    Dataframe with available attributes for the hsapiens_encode dataset.
    :return: pd.DataFrame
    """
    df = pd.read_pickle(os.path.join(DATADIR,
                                     "attributes_hsapiens_encode.pkl"))
    return df


@pytest.fixture
def df_attributes_snp_chircus_snp() -> pd.DataFrame:
    """
    Dataframe with available attributes for the chircus_snp dataset.
    :return: pd.DataFrame
    """
    df = pd.read_pickle(os.path.join(DATADIR,
                                     "attributes_chircus_snp.pkl"))
    return df


@pytest.fixture
def df_attributes_funcgen_hsapiens_peak() -> pd.DataFrame:
    """
    Dataframe with available attributes for the hsapiens_peak dataset.
    :return: pd.DataFrame
    """
    df = pd.read_pickle(os.path.join(DATADIR,
                                     "attributes_hsapiens_peak.pkl"))
    return df


# filters

@pytest.fixture
def df_filters_ensembl_hsapiens_gene() -> pd.DataFrame:
    """
    Dataframe with available filters for the hsapiens_gene_ensembl
    dataset.
    :return: pd.DataFrame
    """
    df = pd.read_pickle(os.path.join(DATADIR,
                                     "filters_hsapiens_gene_ensembl.pkl"))
    return df


@pytest.fixture
def df_filters_mouse_mlpj_gene() -> pd.DataFrame:
    """
    Dataframe with available filters for the mlpj_gene_ensembl dataset.
    :return: pd.DataFrame
    """
    df = pd.read_pickle(os.path.join(DATADIR,
                                     "filters_mlpj_gene_ensembl.pkl"))
    return df


@pytest.fixture
def df_filters_sequence_cdingo_genomic() -> pd.DataFrame:
    """
    Dataframe with available filters for the cdingo_genomic_sequence
    dataset.
    :return: pd.DataFrame
    """
    df = pd.read_pickle(os.path.join(DATADIR,
                                     "filters_cdingo_genomic_sequence.pkl"))
    return df


@pytest.fixture
def df_filters_ontology_closure_eco() -> pd.DataFrame:
    """
    Dataframe with available filters for the closure_ECO dataset.
    :return: pd.DataFrame
    """
    df = pd.read_pickle(os.path.join(DATADIR,
                                     "filters_closure_ECO.pkl"))
    return df


@pytest.fixture
def df_filters_genomic_hsapiens_encode() -> pd.DataFrame:
    """
    Dataframe with available filters for the hsapiens_encode dataset.
    :return: pd.DataFrame
    """
    df = pd.read_pickle(os.path.join(DATADIR,
                                     "filters_hsapiens_encode.pkl"))
    return df


@pytest.fixture
def df_filters_snp_chircus_snp() -> pd.DataFrame:
    """
    Dataframe with available filters for the chircus_snp dataset.
    :return: pd.DataFrame
    """
    df = pd.read_pickle(os.path.join(DATADIR,
                                     "filters_chircus_snp.pkl"))
    return df


@pytest.fixture
def df_filters_funcgen_hsapiens_peak() -> pd.DataFrame:
    """
    Dataframe with available filters for the hsapiens_peak dataset.
    :return: pd.DataFrame
    """
    df = pd.read_pickle(os.path.join(DATADIR,
                                     "filters_hsapiens_peak.pkl"))
    return df


# query

@pytest.fixture
def df_query_ensembl_hsapiens_gene_chrom_1() -> pd.DataFrame:
    """
    Dataframe with the expected query result for chromosome 1 of the
    hsapiens_gene_ensembl dataset.
    :return: pd.DataFrame
    """
    df = pd.read_pickle(os.path.join(DATADIR,
                                     "query_hsapiens_gene_chrom_1.pkl"))
    return df


@pytest.fixture
def df_query_ensembl_hsapiens_gene_chrom_2() -> pd.DataFrame:
    """
    Dataframe with the expected query result for chromosome 2 of the
    hsapiens_gene_ensembl dataset.
    :return: pd.DataFrame
    """
    df = pd.read_pickle(os.path.join(DATADIR,
                                     "query_hsapiens_gene_chrom_2.pkl"))
    return df


@pytest.fixture
def df_query_ensembl_hsapiens_gene_chrom_3() -> pd.DataFrame:
    """
    Dataframe with the expected query result for chromosome 3 of the
    hsapiens_gene_ensembl dataset.
    :return: pd.DataFrame
    """
    df = pd.read_pickle(os.path.join(DATADIR,
                                     "query_hsapiens_gene_chrom_3.pkl"))
    return df
