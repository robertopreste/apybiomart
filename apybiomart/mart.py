#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import pandas as pd
from io import StringIO
from typing import Optional, Dict, Any
from .base import ServerBase, DEFAULT_SCHEMA
from .dataset import Dataset


class Mart(ServerBase):
    """
    Class representing a biomart mart.

    Used to represent specific mart instances on the server. Provides
    functionality for listing and loading the datasets that are available
    in the corresponding mart.

    Args:
        name (str): Name of the mart.
        database_name (str): ID of the mart on the host.
        display_name (str): Display name of the mart.
        host (str): Url of host to connect to.
        path (str): Path on the host to access to the biomart service.
        port (int): Port to use for the connection.
        virtual_schema (str): The virtual schema of the dataset.

    Examples:

        Listing datasets:
            >>> server = Server(host='http://www.ensembl.org')
            >>> mart = server.['ENSEMBL_MART_ENSEMBL']
            >>> mart.list_datasets()

        Selecting a dataset:
            >>> dataset = mart['hsapiens_gene_ensembl']
    """

    RESULT_COLNAMES = ["type", "name", "display_name", "unknown", "unknown2",
                       "unknown3", "unknown4", "virtual_schema", "unknown5"]

    def __init__(self,
                 name: str,
                 database_name: str,
                 display_name: str,
                 host: Optional[str] = None,
                 path: Optional[str] = None,
                 port: Optional[int] = None,
                 virtual_schema: str = DEFAULT_SCHEMA,
                 extra_params: Optional = None):
        super().__init__(host=host, path=path, port=port)

        self._name = name
        self._database_name = database_name
        self._display_name = display_name

        self._virtual_schema = virtual_schema
        self._extra_params = extra_params

        self._datasets = None

    def __getitem__(self, name):
        return self.datasets[name]

    @property
    def name(self):
        """Name of the mart (used as id)."""
        return self._name

    @property
    def display_name(self):
        """Display name of the mart."""
        return self._display_name

    @property
    def database_name(self):
        """Database name of the mart on the host."""
        return self._database_name

    @property
    def datasets(self):
        """List of datasets in this mart."""
        if self._datasets is None:
            self._datasets = self._fetch_datasets()
        return self._datasets

    def list_datasets(self) -> pd.DataFrame:
        """
        Lists available datasets in a readable DataFrame format.

        Returns:
            pd.DataFrame: Frame listing available datasets.
        """
        def _row_gen(attributes):
            for attr in attributes.values():
                yield (attr.name, attr.display_name)

        return pd.DataFrame.from_records(_row_gen(self.datasets),
                                         columns=["name", "display_name"])

    def _fetch_datasets(self) -> Dict[str, Any]:
        # Get datasets using biomart.
        response = self.get(type="datasets", mart=self._name)

        # Read result frame from response.
        result = pd.read_csv(StringIO(response.text),
                             sep="\t", header=None, names=self.RESULT_COLNAMES)

        # Convert result to a dict of datasets.
        datasets = (self._dataset_from_row(row)
                    for _, row in result.iterrows())

        return {d.name: d for d in datasets}

    def _dataset_from_row(self, row) -> Dataset:
        return Dataset(name=row["name"], display_name=row["display_name"],
                       host=self.host, path=self.path, port=self.port,
                       virtual_schema=row["virtual_schema"])

    def __repr__(self):
        return (("<biomart.Mart name={!r}, display_name={!r},"
                 " database_name={!r}>")
                .format(self._name, self._display_name, self._database_name))
