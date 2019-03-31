==========
apybiomart
==========


.. image:: https://img.shields.io/pypi/v/apybiomart.svg
        :target: https://pypi.python.org/pypi/apybiomart

.. image:: https://img.shields.io/travis/robertopreste/apybiomart.svg
        :target: https://travis-ci.com/robertopreste/apybiomart

.. image:: https://readthedocs.org/projects/apybiomart/badge/?version=latest
        :target: https://apybiomart.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


.. image:: https://pyup.io/repos/github/robertopreste/apybiomart/shield.svg
     :target: https://pyup.io/repos/github/robertopreste/apybiomart/
     :alt: Updates



Async pythonic interface to Biomart. 


* Free software: MIT license
* Documentation: https://apybiomart.readthedocs.io.


Features
--------

* single asynchronous `aquery()` function that takes `attributes`, `filters`, and optional `dataset` argument (`dataset` defaults to `"hsapiens_gene_ensembl"`)
    - this `aquery()` function needs to be wrapped in an async loop and all the stuff to actually use it
* synchronous `query()` function that can be used to load a query at a time
* a set of `list_*()` synchronous functions, that list:
    - available marts
    - available datasets for a specific mart (with an optional `mart` argument defaulting to `"ENSEMBL_MART_ENSEMBL"`)
    - available attributes for a dataset (with an optional `dataset` argument defaulting to `"hsapiens_gene_ensembl"`)
    - available filters for a dataset (with an optional `dataset` argument defaulting to `"hsapiens_gene_ensembl"`)

Credits
-------

This package was created with Cookiecutter_ and the `cc-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cc-pypackage`: https://github.com/robertopreste/cc-pypackage
