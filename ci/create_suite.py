#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import os

import asyncio
import click

import apybiomart as apy
from apybiomart.tests.conftest import DATADIR


def create_marts():
    """Create and store the pickled marts dataframe."""
    df = apy.find_marts()
    df.to_pickle(os.path.join(DATADIR, "marts.pkl"))


def create_datasets():
    """Create and store the pickled datasets dataframes."""
    df1 = apy.find_datasets("ENSEMBL_MART_ENSEMBL")
    df1.to_pickle(os.path.join(DATADIR, "datasets_ensembl.pkl"))
    df2 = apy.find_datasets("ENSEMBL_MART_MOUSE")
    df2.to_pickle(os.path.join(DATADIR, "datasets_mouse.pkl"))
    df3 = apy.find_datasets("ENSEMBL_MART_SEQUENCE")
    df3.to_pickle(os.path.join(DATADIR, "datasets_sequence.pkl"))
    df4 = apy.find_datasets("ENSEMBL_MART_ONTOLOGY")
    df4.to_pickle(os.path.join(DATADIR, "datasets_ontology.pkl"))
    df5 = apy.find_datasets("ENSEMBL_MART_GENOMIC")
    df5.to_pickle(os.path.join(DATADIR, "datasets_genomic.pkl"))
    df6 = apy.find_datasets("ENSEMBL_MART_SNP")
    df6.to_pickle(os.path.join(DATADIR, "datasets_snp.pkl"))
    df7 = apy.find_datasets("ENSEMBL_MART_FUNCGEN")
    df7.to_pickle(os.path.join(DATADIR, "datasets_funcgen.pkl"))


def create_attributes():
    """Create and store the pickled attributes dataframes."""
    df1 = apy.find_attributes("hsapiens_gene_ensembl")
    df1.to_pickle(os.path.join(DATADIR,
                               "attributes_hsapiens_gene_ensembl.pkl"))
    df4 = apy.find_attributes("closure_ECO")
    df4.to_pickle(os.path.join(DATADIR, "attributes_closure_ECO.pkl"))
    df5 = apy.find_attributes("hsapiens_encode")
    df5.to_pickle(os.path.join(DATADIR, "attributes_hsapiens_encode.pkl"))
    df6 = apy.find_attributes("chircus_snp")
    df6.to_pickle(os.path.join(DATADIR, "attributes_chircus_snp.pkl"))
    df7 = apy.find_attributes("hsapiens_peak")
    df7.to_pickle(os.path.join(DATADIR, "attributes_hsapiens_peak.pkl"))


def create_filters():
    """Create and store the pickled filters dataframes."""
    df1 = apy.find_filters("hsapiens_gene_ensembl")
    df1.to_pickle(os.path.join(DATADIR, "filters_hsapiens_gene_ensembl.pkl"))
    df4 = apy.find_filters("closure_ECO")
    df4.to_pickle(os.path.join(DATADIR, "filters_closure_ECO.pkl"))
    df5 = apy.find_filters("hsapiens_encode")
    df5.to_pickle(os.path.join(DATADIR, "filters_hsapiens_encode.pkl"))
    df6 = apy.find_filters("chircus_snp")
    df6.to_pickle(os.path.join(DATADIR, "filters_chircus_snp.pkl"))
    df7 = apy.find_filters("hsapiens_peak")
    df7.to_pickle(os.path.join(DATADIR, "filters_hsapiens_peak.pkl"))


def create_queries():
    """Create and store the pickled queries dataframes."""
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


def create_all():
    click.echo("Downloading and saving marts data... ", nl=False)
    create_marts()
    click.echo("Done.")
    click.echo("Downloading and saving datasets data... ", nl=False)
    create_datasets()
    click.echo("Done.")
    click.echo("Downloading and saving attributes data... ", nl=False)
    create_attributes()
    click.echo("Done.")
    click.echo("Downloading and saving filters data... ", nl=False)
    create_filters()
    click.echo("Done.")
    click.echo("Downloading and saving queries data... ", nl=False)
    create_queries()
    click.echo("Done.")
