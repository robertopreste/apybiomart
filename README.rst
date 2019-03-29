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

TODO
====

* single `aquery()` function that takes `attributes`, `filters`, and optional `dataset` and `mart` arguments (should default to one of the available ones)
    - this `query()` function should actually be an async coroutine
    - so the user should wrap that in an async loop and all the stuff to actually use it
* another `query()` function that is actually sync, so can be used to load a query at a time
* a set of `list_*()` functions (that may not necessarily be async), that list:
    - ~~available marts~~
    - ~~available datasets for a specific mart (should take an optional `mart` argument defaulting to one of the available ones)~~
    - available attributes for a dataset (same as above, with a dataset and mart)
    - available filters for a dataset (same as above)

Credits
-------

This package was created with Cookiecutter_ and the `cc-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cc-pypackage`: https://github.com/robertopreste/cc-pypackage
