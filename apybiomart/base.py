#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
from typing import Optional

DEFAULT_HOST = "http://www.biomart.org"
DEFAULT_PATH = "/biomart/martservice"
DEFAULT_PORT = 80
DEFAULT_SCHEMA = "default"


class ServerBase:
    """
    Base class that handles requests to the biomart server.

    Attributes:
        host (str): Host to connect to for the biomart service.
        path (str): Path to the biomart service on the host.
        port (str): Port to connect to on the host.
        url (str): Url used to connect to the biomart service.
        # use_cache (bool): Whether to cache requests to biomart.
        # cache is disabled
    """

    def __init__(self,
                 host: Optional[str] = None,
                 path: Optional[str] = None,
                 port: Optional[int] = None):
        """
        ServerBase constructor.
        :param Optional[str] host: url of the host to connect to
        :param Optional[str] path: path on the host to access the biomart
        service
        :param Optional[int] port: port to use for the connection
        """
        # Use defaults if arg is None.
        host: str = host or DEFAULT_HOST
        path: str = path or DEFAULT_PATH
        port: str = port or DEFAULT_PORT

        # Add http prefix and remove trailing slash.
        host = self._add_http_prefix(host)
        host = self._remove_trailing_slash(host)

        # Ensure path starts with slash.
        path = self._add_leading_slash(path)

        self._host = host
        self._path = path
        self._port = port

    @property
    def host(self):
        """Host to connect to for the biomart service."""
        return self._host

    @property
    def path(self):
        """Path to the biomart service on the host."""
        return self._path

    @property
    def port(self):
        """Port to connect to on the host."""
        return self._port

    @property
    def url(self):
        """Url used to connect to the biomart service."""
        return "{}:{}{}".format(self._host, self._port, self._path)

    @staticmethod
    def _add_http_prefix(url: str,
                         prefix: str = "http://") -> str:
        """
        Add an http:// or https:// prefix to the given url, if this is not
        already present in the url.
        :param str url: input url
        :param str prefix: url prefix to add if not already present
        (default: 'http://')
        :return: str
        """
        if not url.startswith("http://") or url.startswith("https://"):
            url = prefix + url
        return url

    @staticmethod
    def _remove_trailing_slash(url: str) -> str:
        """
        Remove the trailing forward slash from the given url, if present.
        :param str url: input url
        :return: str
        """
        if url.endswith("/"):
            url = url[:-1]
        return url

    @staticmethod
    def _add_leading_slash(path: str) -> str:
        """
        Add a leading forward slash to the given path, if not already present.
        :param str path: input path
        :return: str
        """
        if not path.startswith("/"):
            path = "/" + path
        return path

    # TODO: will need to re-implement this
    def get(self, **params):
        """Performs get request to the biomart service.

        Args:
            **params (dict of str: any): Arbitrary keyword arguments, which
                are added as parameters to the get request to biomart.

        Returns:
            requests.models.Response: Response from biomart for the request.

        """
        if self._use_cache:
            r = requests.get(self.url, params=params)
        else:
            with requests_cache.disabled():
                r = requests.get(self.url, params=params)
        r.raise_for_status()
        return r


class BiomartException(Exception):
    """Basic exception class for biomart exceptions."""
    pass
