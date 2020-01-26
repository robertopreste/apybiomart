=====
Usage
=====

apybiomart can be used in a project with a simple import::

    import apybiomart

The main purpose of the package is to perform queries on BioMart (either synchronously or
asynchronously), however users may first need to explore the available marts, datasets,
attributes and filters.

Marts, datasets, attributes and filters
=======================================

BioMart contains different databases, called *marts*, each of which in turn contains several
*datasets*, each related to a specific species. These datasets can be queried and it is
possible to restrict the amount of data returned to one or more particular types of
information, namely *attributes*, and using *filters* that only retain data satisfying one or
more specific criteria.

For more information, please refer to BioMart's help_ page.

Marts
-----

In order to view the marts available on BioMart, the ``find_marts()`` function can be used::

    from apybiomart import find_marts
    find_marts()

A dataframe with the available marts is returned, with their proper ``name`` and ``display_name``::

                     Mart_ID              Mart_name
    0   ENSEMBL_MART_ENSEMBL       Ensembl Genes 96
    1     ENSEMBL_MART_MOUSE       Mouse strains 96
    2  ENSEMBL_MART_SEQUENCE               Sequence
    3  ENSEMBL_MART_ONTOLOGY               Ontology
    4   ENSEMBL_MART_GENOMIC    Genomic features 96
    5       ENSEMBL_MART_SNP   Ensembl Variation 96
    6   ENSEMBL_MART_FUNCGEN  Ensembl Regulation 96

A CLI command is also available to retrieve the same information: ``apybiomart marts``.

Datasets
--------

Available datasets for a specific mart can be retrieved using the ``find_datasets()`` function::

    from apybiomart import find_datasets
    find_datasets(mart="ENSEMBL_MART_ENSEMBL")
    # same as above, using the default mart
    find_datasets()

The ``find_datasets()`` function accepts an optional ``mart`` argument, which defaults to
"ENSEMBL_MART_ENSEMBL". The returned dataframe contains all the available datasets in the
given mart, with their ``name``, ``display_name`` and the ``mart`` to which they belong::

                         Dataset_ID                                       Dataset_name               Mart_ID
    0       rroxellana_gene_ensembl           Golden snub-nosed monkey genes (Rrox_v1)  ENSEMBL_MART_ENSEMBL
    1          ggallus_gene_ensembl                             Chicken genes (GRCg6a)  ENSEMBL_MART_ENSEMBL
    2    dmelanogaster_gene_ensembl           Drosophila melanogaster genes (BDGP6.22)  ENSEMBL_MART_ENSEMBL
    ..                          ...                                                ...                   ...
    181      sdorsalis_gene_ensembl                Yellowtail amberjack genes (Sedor1)  ENSEMBL_MART_ENSEMBL
    182           ohni_gene_ensembl            Japanese medaka HNI genes (ASM223471v1)  ENSEMBL_MART_ENSEMBL
    183       pmarinus_gene_ensembl                       Lamprey genes (Pmarinus_7.0)  ENSEMBL_MART_ENSEMBL

A CLI command is also available to retrieve the same information: ``apybiomart datasets``, whose
``--mart`` option can be used to specify which mart will be used (default is
"ENSEMBL_MART_ENSEMBL").

Attributes
----------

When querying a dataset, users may want to retrieve specific attributes; the ``find_attributes()``
function accepts an optional ``dataset`` (defaulting to "hsapiens_gene_ensembl") and gathers all
the available attributes for the given dataset::

    from apybiomart import find_attributes
    find_attributes(dataset="hsapiens_gene_ensembl")
    # same as above, using the default dataset
    find_attributes()

The dataframe returned contains each attribute's ``name``, ``display_name``, ``description``
(where available), and the ``dataset`` to which it belongs::

                  Attribute_ID          Attribute_name             Attribute_description             Dataset_ID
    0          ensembl_gene_id          Gene stable ID             Stable ID of the Gene  hsapiens_gene_ensembl
    1  ensembl_gene_id_version  Gene stable ID version  Versionned stable ID of the Gene  hsapiens_gene_ensembl
    2    ensembl_transcript_id    Transcript stable ID       Stable ID of the Transcript  hsapiens_gene_ensembl
    ..                     ...                     ...                               ...                    ...
    3348            cds_length              CDS Length                                    hsapiens_gene_ensembl
    3349             cds_start               CDS start                                    hsapiens_gene_ensembl
    3350               cds_end                 CDS end                                    hsapiens_gene_ensembl

A CLI command is also available to retrieve the same information: ``apybiomart attributes``, whose
``--dataset`` option can be used to specify which dataset will be used (default is
"hsapiens_gene_ensembl").

Filters
-------

Datasets can be queried using filters that restrict the returned information to some specific
subset of interest (e.g. chromosome, start position, etc.). In order to retrieve the list of
filters available for a given dataset, the ``find_filters()`` function can be used::

    from apybiomart import find_filters
    find_filters("hsapiens_gene_ensembl")
    # same as above, using the default dataset
    find_filters()

This function accepts an optional ``dataset`` argument, which defaults to "hsapiens_gene_ensembl",
and returns a dataframe with the ``name``, ``type``, ``description`` (where available) of each
filter, as well as the ``dataset`` to which it belongs::

                               Filter_ID  Filter_type Filter_description             Dataset_ID
    0               link_so_mini_closure         list                     hsapiens_gene_ensembl
    1                    link_go_closure         text                     hsapiens_gene_ensembl
    2  link_ensembl_transcript_stable_id         text                     hsapiens_gene_ensembl
    ..                               ...          ...                ...                    ...
    39        germ_line_variation_source         list                     hsapiens_gene_ensembl
    40          somatic_variation_source         list                     hsapiens_gene_ensembl
    42               so_consequence_name         list                     hsapiens_gene_ensembl

A CLI command is also available to retrieve the same information: ``apybiomart filters``, whose
``--dataset`` option can be used to specify which dataset will be used (default is
"hsapiens_gene_ensembl").

Queries
=======

Once the desired mart, dataset, attributes and filters have been explored (or if they were known
beforehand), it is possible to query BioMart to retrieve the actual data; queries can be performed
synchronously or asynchronously.

Exploring the difference between these two approaches is out of the scope of this document, but
basically while in synchronous calls the client has to wait for a request to be complete before
moving to the next one, in asynchronous calls the client can perform another request while the
first one is idle, and so on until all the requests have been performed and a response was
returned.

Simply put, apybiomart allows to perform synchronous queries to explore the data, and asynchronous
queries to group multiple queries and run them efficiently.

Synchronous Queries
-------------------

Synchronous queries can be performed using the ``query()`` function, which accepts ``attributes``
and ``filters`` arguments, and an optional ``dataset`` argument (which defaults to
"hsapiens_gene_ensembl")::

    from apybiomart import query
    query(attributes=["ensembl_gene_id", "external_gene_name"],
          filters={"chromosome_name": "1"},
          dataset="hsapiens_gene_ensembl")

The ``attributes`` are provided as a list of properties, while ``filters`` are represented by a
filter name : filter value dictionary. The returned dataframe contains the result of the query,
restricted according to the provided filters and attributes.

Asynchronous Queries
--------------------

Asynchronous queries can be performed using the ``aquery()`` function, which works just like
``query()``, with the only difference that this is an async coroutine, so it needs to be handled
properly taking advantage of the ``asyncio`` event loop::

    import asyncio
    from apybiomart import aquery
    loop = asyncio.get_event_loop()
    loop.run_until_complete(
        aquery(attributes=["ensembl_gene_id", "external_gene_name"],
               filters={"chromosome_name": "1"},
               dataset="hsapiens_gene_ensembl")
    )

This allows to group multiple queries together, and the event loop will take care of scheduling
them for execution::

    import asyncio
    from apybiomart import aquery
    loop = asyncio.get_event_loop()
    tasks = [aquery(attributes=["ensembl_gene_id", "external_gene_name"],
                    filters={"chromosome_name": str(i)},
                    dataset="hsapiens_gene_ensembl") for i in range(3)]
    loop.run_until_complete(asyncio.gather(*tasks))

It is of course possible to assign the query results to one or more specific variables, for future
usage::

    # replacing last line of the previous code snippet
    single_result = loop.run_until_complete(asyncio.gather(*tasks))
    # or using multiple variables
    chrom1, chrom2, chrom3 = loop.run_until_complete(asyncio.gather(*tasks))

Please refer to the asyncio_ documentation for more information.

.. _help: https://www.ensembl.org/info/data/biomart/index.html
.. _asyncio: https://docs.python.org/3/library/asyncio.html
