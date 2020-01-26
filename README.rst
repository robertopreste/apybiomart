==========
apybiomart
==========


.. image:: https://img.shields.io/pypi/v/apybiomart.svg
    :target: https://pypi.python.org/pypi/apybiomart

.. image:: https://www.repostatus.org/badges/latest/wip.svg
    :alt: Project Status: WIP – Initial development is in progress, but there has not yet been a stable, usable release suitable for the public.
    :target: https://www.repostatus.org/#wip

.. image:: https://travis-ci.com/robertopreste/apybiomart.svg?branch=master
    :target: https://travis-ci.com/robertopreste/apybiomart
    :alt: Travis CI build status

.. image:: https://circleci.com/gh/robertopreste/apybiomart.svg?style=svg
    :target: https://circleci.com/gh/robertopreste/apybiomart
    :alt: CircleCI build status

.. image:: https://codecov.io/gh/robertopreste/apybiomart/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/robertopreste/apybiomart
    :alt: Codecov status

.. image:: https://readthedocs.org/projects/apybiomart/badge/?version=latest
    :target: https://apybiomart.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://pyup.io/repos/github/robertopreste/apybiomart/shield.svg
    :target: https://pyup.io/repos/github/robertopreste/apybiomart/
    :alt: Updates

.. image:: https://pyup.io/repos/github/robertopreste/apybiomart/python-3-shield.svg
    :target: https://pyup.io/repos/github/robertopreste/apybiomart/
    :alt: Python 3

.. image:: https://pepy.tech/badge/apybiomart
    :target: https://pepy.tech/project/apybiomart
    :alt: Downloads


Async pythonic interface to BioMart.


* Free software: MIT license
* Documentation: https://apybiomart.readthedocs.io
* GitHub repo: https://github.com/robertopreste/apybiomart


Features
========

apybiomart is a Python module which provides a simple asynchronous interface to Ensembl BioMart_. Users can exploit the async interface to schedule multiple queries using all the commodities offered by Python's asyncio library.

Depending on specific needs, apybiomart offers different entry points:

* an asynchronous ``aquery()`` function, to schedule multiple queries in the same event loop;
* a synchronous ``query()`` function, which can be used for exploratory queries, executed in real time;
* a set of synchronous ``find_*()`` functions, which can be used to retrieve the list of available
  marts (``find_marts()``), datasets for a specific mart (``find_datasets()``), attributes
  (``find_attributes()``) and filters (``find_filters()``) for a specific dataset.

  - a set of related CLI commands also exists to allow exploration of these data from the command
    line; these are, respectively, ``apybiomart marts``, ``apybiomart datasets``,
    ``apybiomart attributes`` and ``apybiomart filters``. Run ``apybiomart --help`` for further
    details.

Please refer to the Usage_ section of the documentation for further information.

Background
----------

apybiomart was originally born as a fork of the great pybiomart_ package.

I was working on a project that employed a series of async calls to several online resources, but
I couldn't manage to perform asynchronous calls to BioMart using that package, so I decided to
modify it to better suit my needs. However, it gradually evolved into a very different thing:
the original implementation was rewritten and the structure of the package changed a bit, in a
way that I found most useful for my purpose.

This said, all the credits go to jrderuiter_, which created the original pybiomart_ package.

Installation
============

**apybiomart only supports Python 3**, and can be installed using pip::

    pip install apybiomart

Please refer to the Installation_ section of the documentation for further information.

Credits
=======

This package was created with Cookiecutter_ and the `cc-pypackage`_ project template.

.. _BioMart: https://www.ensembl.org/biomart/martview
.. _Usage: https://apybiomart.readthedocs.io/en/latest/usage.html
.. _pybiomart: https://github.com/jrderuiter/pybiomart
.. _jrderuiter: https://github.com/jrderuiter
.. _Installation: https://apybiomart.readthedocs.io/en/latest/installation.html
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cc-pypackage`: https://github.com/robertopreste/cc-pypackage
