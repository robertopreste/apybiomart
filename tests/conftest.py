#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import pytest
import pickle
import os
from apybiomart.base import DEFAULT_HOST, DEFAULT_PATH, DEFAULT_PORT
from apybiomart.server import Server


BASE_DIR = os.path.dirname(__file__)


@pytest.helpers.register
def data_path(relative_path, relative_to=BASE_DIR):
    """Returns data path to test file."""

    return os.path.join(relative_to, 'data', relative_path)


class MockResponse(object):
    """Mock response class."""

    def __init__(self, text=''):
        self.text = text
        # self.content = text.encode('utf-8')
        self.content = text

    def raise_for_status(self):
        """Mock raise_for_status function."""
        pass


@pytest.helpers.register
def mock_response(text=''):
    """Helper function for creating a mock response."""
    return MockResponse(text=text)


@pytest.fixture
def server_marts_response():
    """Returns a cached Server response containing marts."""

    # Code for saving cached request.
    # from apybiomart import Server
    # server = Server(host='http://www.ensembl.org')
    # req = server.get(type='registry')
    # with open('tests/data/server_request.pkl', 'wb') as f:
    #     pickle.dump(req.text, file=f, protocol=2)

    # Load cached request.
    # file_path = pytest.helpers.data_path('marts_response.pkl')
    file_path = pytest.helpers.data_path('server_request.pkl')

    with open(file_path, 'rb') as file_:
        return MockResponse(text=pickle.load(file_))


@pytest.fixture
def mock_mart(mocker, server_marts_response):
    """Returns an example mart, built using a cached response."""

    mocker.patch.object(Server, 'get', return_value=server_marts_response)

    server = Server(host='http://www.ensembl.org')
    return server['ENSEMBL_MART_ENSEMBL']


@pytest.fixture
def mart_datasets_response():
    """Returns a cached Mart response containing datasets."""

    # Code for saving pickle.
    # mart = server.marts["ENSEMBL_MART_ENSEMBL"]
    # req = mart.get(type='datasets', mart=mart._name)
    # with open('tests/data/mart_request.pkl', 'wb') as f:
    #     pickle.dump(req.text, file=f, protocol=2)

    # Load cached request.
    # file_path = pytest.helpers.data_path('datasets_response.pkl')
    file_path = pytest.helpers.data_path('mart_request.pkl')

    with open(file_path, 'rb') as file_:
        return pytest.helpers.mock_response(text=pickle.load(file_))


@pytest.fixture
def mock_dataset(mocker, mock_mart, mart_datasets_response):
    """Returns an example dataset, built using a cached response."""

    mocker.patch.object(mock_mart, 'get', return_value=mart_datasets_response)
    return mock_mart.datasets['mmusculus_gene_ensembl']


@pytest.fixture
def mock_dataset_with_config(mocker, mock_dataset, dataset_config_response):
    """Returns an example dataset, mocked to return a configuration."""

    mocker.patch.object(
        mock_dataset, 'get', return_value=dataset_config_response)
    mock_dataset.attributes
    return mock_dataset


@pytest.fixture
def dataset_config_response():
    """Returns a cached Dataset config response."""

    # Dumped using the following code.
    # from apybiomart import Dataset
    # dataset = Dataset(name="hsapiens_gene_ensembl",
    #                   host="http://www.ensembl.org")
    # req = dataset.get(type='configuration', dataset=dataset._name)
    # with open('tests/data/config_response.pkl', 'wb') as f:
    #    pickle.dump(req.text, file=f, protocol=2)

    # Load cached request.
    file_path = pytest.helpers.data_path('config_response.pkl')

    with open(file_path, 'rb') as file_:
        return pytest.helpers.mock_response(pickle.load(file_))


@pytest.fixture
def dataset_query_response():
    """Returns a cached Dataset query response."""

    # Dumped from inside query using the below code.
    # from apybiomart import Dataset
    # dataset = Dataset("mmusculus_gene_ensembl",
    #                   host="http://www.ensembl.org")
    # response = dataset.query(attributes=["ensembl_gene_id",
    #                                      "external_gene_name"])
    # with open('tests/data/query_response.pkl', 'wb') as f:
    #    pickle.dump(response.text, file=f, protocol=2)

    # Load cached request.
    file_path = pytest.helpers.data_path('query_response.pkl')

    with open(file_path, 'rb') as file_:
        return pytest.helpers.mock_response(pickle.load(file_))


@pytest.fixture
def default_url():
    """Default URL fixture."""
    return '{}:{}{}'.format(DEFAULT_HOST, DEFAULT_PORT, DEFAULT_PATH)


@pytest.fixture
def query_params():
    """Example query parameters."""

    return {
        "attributes": ["ensembl_gene_id"],
        "filters": {
            "chromosome_name": ["1"]
        }
    }

