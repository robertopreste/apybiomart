#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import pytest
from apybiomart.base import ServerBase, DEFAULT_HOST, DEFAULT_PATH, DEFAULT_PORT


class TestServerBase(object):
    """Tests for ServerBase class."""

    def test_basic(self, default_url):
        """Tests default instantation."""

        base_obj = ServerBase()

        assert base_obj.host == DEFAULT_HOST
        assert base_obj.path == DEFAULT_PATH
        assert base_obj.port == DEFAULT_PORT
        assert base_obj.url == default_url

    def test_params(self):
        """Tests instantation with custom args."""

        base_obj = ServerBase(
            host='http://www.ensembl.org',
            path='/other/path',
            port=8080)

        assert base_obj.host == 'http://www.ensembl.org'
        assert base_obj.path == '/other/path'
        assert base_obj.port == 8080
        assert base_obj.url == 'http://www.ensembl.org:8080/other/path'

    def test_missing_http(self):
        """Tests url with missing http."""

        base_obj = ServerBase(host='www.ensembl.org')

        assert base_obj.host == 'http://www.ensembl.org'

    def test_trailing_slash(self):
        """Tests url with trailing slash."""

        base_obj = ServerBase(host='http://www.ensembl.org/')

        assert base_obj.host == 'http://www.ensembl.org'

    # def test_get(self, mocker, default_url):
    #     """Tests get invocation."""
    #
    #     req = pytest.helpers.mock_response()
    #
    #     mock_get = mocker.patch.object(requests, 'get', return_value=req)
    #
    #     base_obj = ServerBase()
    #     base_obj.get()
    #
    #     mock_get.assert_called_once_with(default_url, params={})
    #
    # def test_get_with_params(self, mocker, default_url):
    #     """Tests get invocation with custom parameters."""
    #
    #     req = pytest.helpers.mock_response()
    #
    #     mock_get = mocker.patch.object(requests, 'get', return_value=req)
    #
    #     base_obj = ServerBase()
    #     base_obj.get(test=True)
    #
    #     mock_get.assert_called_once_with(default_url, params={'test': True})

