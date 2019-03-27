#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import pytest


class TestMartStatic(object):
    """Offline unit tests for Mart (using a static response)."""

    def test_attributes(self, mock_mart):
        """Tests setting of basic mart attributes."""

        assert mock_mart.name == 'ENSEMBL_MART_ENSEMBL'
        assert mock_mart.display_name == 'Ensembl Genes 95'
        assert mock_mart.database_name == 'ensembl_mart_95'

    def test_datasets(self, mocker, mock_mart, mart_datasets_response):
        """Tests retrieval of datasets."""

        mock_get = mocker.patch.object(
            mock_mart, 'get', return_value=mart_datasets_response)

        assert len(mock_mart.datasets) > 0
        mock_get.assert_called_once_with(type='datasets',
                                         mart='ENSEMBL_MART_ENSEMBL')

    def test_get_item(self, mocker, mock_mart, mart_datasets_response):
        """Tests accessing a specific dataset."""

        mocker.patch.object(mock_mart, 'get',
                            return_value=mart_datasets_response)
        dataset = mock_mart['mmusculus_gene_ensembl']

        assert dataset.name == 'mmusculus_gene_ensembl'
