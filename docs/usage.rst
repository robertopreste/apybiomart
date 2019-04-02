=====
Usage
=====

apybiomart can be used in a project with a simple import::

    import apybiomart
    # or use an alias for simplicity
    import apybiomart as apy

The main purpose of the package is to perform queries on BioMart (either synchronously or asynchronously), however users may first need to explore the available marts, datasets, attributes and filters.

Marts, datasets, attributes and filters
---------------------------------------

BioMart contains different databases, called *marts*, each of which in turn contains several *datasets*, each related to a specific species. These datasets can be queried and it is possible to restrict the amount of data returned to one or more particular types of information, namely *attributes*, and using *filters* that only retain data satisfying one or more specific criteria.

For more information, please refer to BioMart's help_ page.

Marts
=====

In order to view the marts available on BioMart, the ``list_marts()`` function can be used::

    from apybiomart import list_marts
    list_marts()

A dataframe with the available marts is returned, with their proper ``name`` and ``display_name``.

Datasets
========

Available datasets for a specific mart can be retrieved using the ``list_datasets()`` function::

    from apybiomart import list_datasets
    list_datasets(mart="ENSEMBL_MART_ENSEMBL")
    # same as above, using the default mart
    list_datasets()

The ``list_datasets()`` function accepts an optional ``mart`` argument, which defaults to "ENSEMBL_MART_ENSEMBL". The returned dataframe contains all the available datasets in the given mart, with their ``name``, ``display_name`` and the ``mart`` to which they belong.

Attributes
==========

When querying a dataset, users may want to retrieve specific attributes; the ``list_attributes()`` function accepts an optional ``dataset`` (defaulting to "hsapiens_gene_ensembl") and gathers all the available attributes for the given dataset::

    from apybiomart import list_attributes
    list_attributes(dataset="hsapiens_gene_ensembl")
    # same as above, using the default dataset
    list_attributes()

The dataframe returned contains each attribute's ``name``, ``display_name``, ``description`` (where available), and the ``dataset`` to which it belongs.

Filters
=======

Datasets can be queried using filters that restrict the returned information to some specific subset of interest (e.g. chromosome, start position, etc.). In order to retrieve the list of filters available for a given dataset, the ``list_filters()`` function can be used::

    from apybiomart import list_filters
    list_filters("hsapiens_gene_ensembl")
    # same as above, using the default dataset
    list_filters()

This function accepts an optional ``dataset`` argument, which defaults to "hsapiens_gene_ensembl", and returns a dataframe with the ``name``, ``type``, ``description`` (where available) of each filter, as well as the ``dataset`` to which it belongs.

Queries
-------

Once the desired mart, dataset, attributes and filters have been explored (or if they were known beforehand), it is possible to query BioMart to retrieve the actual data; queries can be performed synchronously or asynchronously.

Exploring the difference between these two approaches is out of the scope of this document, but basically while in synchronous calls the client has to wait for a request to be complete before moving to the next one, in asynchronous calls the client can perform another request while the first one is idle, and so on until all the requests have been performed and a response was returned.

Simply put, apybiomart allows to perform synchronous queries to explore the data, and asynchronous queries to group multiple queries and run them efficiently.

Synchronous Queries
===================

Synchronous queries can be performed using the ``query()`` function, which accepts ``attributes`` and ``filters`` arguments, and an optional ``dataset`` argument (which defaults to "hsapiens_gene_ensembl")::

    from apybiomart import query
    query(attributes=["ensembl_gene_id", "external_gene_name"],
          filters={"chromosome_name": "1"},
          dataset="hsapiens_gene_ensembl")

The ``attributes`` are provided as a list of properties, while ``filters`` are represented by a filter name : filter value dictionary. The returned dataframe contains the result of the query, restricted according to the provided filters and attributes.

Asynchronous Queries
====================

Asynchronous queries can be performed using the ``aquery()`` function, which works just like ``query()``, with the only difference that this is an async coroutine, so it needs to be handled properly taking advantage of the ``asyncio`` event loop::

    import asyncio
    from apybiomart import aquery
    loop = asyncio.get_event_loop()
    loop.run_until_complete(
        aquery(attributes=["ensembl_gene_id", "external_gene_name"],
               filters={"chromosome_name": "1"},
               dataset="hsapiens_gene_ensembl")
    )

This allows to group multiple queries together, and the event loop will take care of scheduling them for execution::

    import asyncio
    from apybiomart import aquery
    loop = asyncio.get_event_loop()
    tasks = [aquery(attributes=["ensembl_gene_id", "external_gene_name"],
                    filters={"chromosome_name": str(i)},
                    dataset="hsapiens_gene_ensembl) for i in range(3)]
    loop.run_until_complete(asyncio.gather(*tasks))

It is of course possible to assign the query results to one or more specific variables, for future usage::

    # replacing last line of the previous code snippet
    single_result = loop.run_until_complete(asyncio.gather(*tasks))
    # or using multiple variables
    chrom1, chrom2, chrom3 = loop.run_until_complete(asyncio.gather(*tasks))

Please refer to the asyncio_ documentation for more information.

.. _help: https://www.ensembl.org/info/data/biomart/index.html
.. _asyncio: https://docs.python.org/3/library/asyncio.html
