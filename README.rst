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



Async pythonic interface to BioMart.


* Free software: MIT license
* Documentation: https://apybiomart.readthedocs.io.
* GitHub repo: https://github.com/robertopreste/apybiomart


Features
--------

`apybiomart` is a Python module which provides a simple asynchronous interface to Ensembl BioMart_. Users can exploit the async interface to schedule multiple queries using all the commodities offered by Python's `asyncio` library.

Depending on specific needs, `apybiomart` offers different entry points:

* an asynchronous `aquery()` function, to schedule multiple queries in the same event loop;
* a synchronous `query()` function, which can be used for exploratory queries, executed in real time;
* a set of synchronous `list_*()` functions, which can be used to retrieve the list of available marts, datasets for a specific mart, attributes and filters for a specific dataset.


Background
==========

`apybiomart` was originally born as a fork of the great pybiomart_ package.

I was working on a project that employed a series of async calls to several online resources, but I couldn't manage to perform asynchronous calls to BioMart using that package, so I decided to modify it to better suit my needs. However, it gradually evolved into a very different thing: the original implementation was rewritten and the structure of the package changed a bit, in a way that I found most useful for my purpose.

This said, all the credits go to jrderuiter_, which created the original `pybiomart` package.

Credits
-------

This package was created with Cookiecutter_ and the `cc-pypackage`_ project template.

.. _BioMart: https://www.ensembl.org/biomart/martview
.. _pybiomart: https://github.com/jrderuiter/pybiomart
.. _jrderuiter: https://github.com/jrderuiter
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cc-pypackage`: https://github.com/robertopreste/cc-pypackage
