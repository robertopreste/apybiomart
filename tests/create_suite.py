#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import asyncio
import os
import pandas as pd
import apybiomart as apy

DATADIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data")


def create_marts():
    """Create and store the pickled marts dataframe.
    :return:
    """
    df = apy.list_marts()
    df.to_pickle(os.path.join(DATADIR, "marts.pkl"))
    return


def create_datasets():
    """Create and store the pickled datasets dataframes.
    :return:
    """
    df1 = apy.list_datasets("ENSEMBL_MART_ENSEMBL")
    df1.to_pickle(os.path.join(DATADIR, "datasets_ensembl.pkl"))
    df2 = apy.list_datasets("ENSEMBL_MART_MOUSE")
    df2.to_pickle(os.path.join(DATADIR, "datasets_mouse.pkl"))
    df3 = apy.list_datasets("ENSEMBL_MART_SEQUENCE")
    df3.to_pickle(os.path.join(DATADIR, "datasets_sequence.pkl"))
    df4 = apy.list_datasets("ENSEMBL_MART_ONTOLOGY")
    df4.to_pickle(os.path.join(DATADIR, "datasets_ontology.pkl"))
    df5 = apy.list_datasets("ENSEMBL_MART_GENOMIC")
    df5.to_pickle(os.path.join(DATADIR, "datasets_genomic.pkl"))
    df6 = apy.list_datasets("ENSEMBL_MART_SNP")
    df6.to_pickle(os.path.join(DATADIR, "datasets_snp.pkl"))
    df7 = apy.list_datasets("ENSEMBL_MART_FUNCGEN")
    df7.to_pickle(os.path.join(DATADIR, "datasets_funcgen.pkl"))
    return


def create_attributes():
    """Create and store the pickled attributes dataframes.
    :return:
    """
    df1 = apy.list_attributes("hsapiens_gene_ensembl")
    df1.to_pickle(os.path.join(DATADIR,
                               "attributes_hsapiens_gene_ensembl.pkl"))
    df2 = apy.list_attributes("mlpj_gene_ensembl")
    df2.to_pickle(os.path.join(DATADIR, "attributes_mlpj_gene_ensembl.pkl"))
    df3 = apy.list_attributes("cdingo_genomic_sequence")
    df3.to_pickle(os.path.join(DATADIR,
                               "attributes_cdingo_genomic_sequence.pkl"))
    df4 = apy.list_attributes("closure_ECO")
    df4.to_pickle(os.path.join(DATADIR, "attributes_closure_ECO.pkl"))
    df5 = apy.list_attributes("hsapiens_encode")
    df5.to_pickle(os.path.join(DATADIR, "attributes_hsapiens_encode.pkl"))
    df6 = apy.list_attributes("chircus_snp")
    df6.to_pickle(os.path.join(DATADIR, "attributes_chircus_snp.pkl"))
    df7 = apy.list_attributes("hsapiens_peak")
    df7.to_pickle(os.path.join(DATADIR, "attributes_hsapiens_peak.pkl"))
    return


def create_filters():
    """Create and store the pickled filters dataframes.
    :return:
    """
    df1 = apy.list_filters("hsapiens_gene_ensembl")
    df1.to_pickle(os.path.join(DATADIR, "filters_hsapiens_gene_ensembl.pkl"))
    df2 = apy.list_filters("mlpj_gene_ensembl")
    df2.to_pickle(os.path.join(DATADIR, "filters_mlpj_gene_ensembl.pkl"))
    df3 = apy.list_filters("cdingo_genomic_sequence")
    df3.to_pickle(os.path.join(DATADIR, "filters_cdingo_genomic_sequence.pkl"))
    df4 = apy.list_filters("closure_ECO")
    df4.to_pickle(os.path.join(DATADIR, "filters_closure_ECO.pkl"))
    df5 = apy.list_filters("hsapiens_encode")
    df5.to_pickle(os.path.join(DATADIR, "filters_hsapiens_encode.pkl"))
    df6 = apy.list_filters("chircus_snp")
    df6.to_pickle(os.path.join(DATADIR, "filters_chircus_snp.pkl"))
    df7 = apy.list_filters("hsapiens_peak")
    df7.to_pickle(os.path.join(DATADIR, "filters_hsapiens_peak.pkl"))
    return


def create_queries():
    """Create and store the pickled queries dataframes.
    :return:
    """
    df1 = apy.query(attributes=["ensembl_gene_id", "external_gene_name"],
                    filters={"chromosome_name": "1"},
                    dataset="hsapiens_gene_ensembl")
    df1.to_pickle(os.path.join(DATADIR, "query_hsapiens_gene_chrom_1.pkl"))
    df2 = apy.query(attributes=["ensembl_gene_id", "external_gene_name"],
                    filters={"chromosome_name": "2"},
                    dataset="hsapiens_gene_ensembl")
    df2.to_pickle(os.path.join(DATADIR, "query_hsapiens_gene_chrom_2.pkl"))
    df3 = apy.query(attributes=["ensembl_gene_id", "external_gene_name"],
                    filters={"chromosome_name": "3"},
                    dataset="hsapiens_gene_ensembl")
    df3.to_pickle(os.path.join(DATADIR, "query_hsapiens_gene_chrom_3.pkl"))
    df4 = apy.query(attributes=["ensembl_gene_id", "external_gene_name"],
                    filters={"chromosome_name": "1"},
                    dataset="maj_gene_ensembl")
    df4.to_pickle(os.path.join(DATADIR, "query_maj_gene_chrom_1.pkl"))
    return


def main():
    print("Downloading and saving marts data... ", end="")
    create_marts()
    print("Done.")
    print("Downloading and saving datasets data... ", end="")
    create_datasets()
    print("Done.")
    print("Downloading and saving attributes data... ", end="")
    create_attributes()
    print("Done.")
    print("Downloading and saving filters data... ", end="")
    create_filters()
    print("Done.")
    print("Downloading and saving queries data... ", end="")
    create_queries()
    print("Done.")


if __name__ == '__main__':
    main()
