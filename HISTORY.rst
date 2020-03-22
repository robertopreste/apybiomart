=======
History
=======

0.1.0 (2019-03-26)
==================

* First development release.

0.1.1 (2019-03-27)
------------------

* Requests are converted to async calls;
* Code style is clean and Python 3 compatible.

0.1.2 (2019-03-27)
------------------

* Add basic tests.

0.2.0 (2019-03-31)
==================

* New version with different organisation of classes and functions;
* Sync ``query`` and async ``aquery`` functions to query Biomart;
* Sync ``list_*`` functions to retrieve available ``marts``, ``datasets``, ``filters`` and ``attributes``.

0.2.1 (2019-04-01)
------------------

* Add tests.

0.2.2 (2019-04-01)
------------------

* Basic functions working and tested;
* Fix documentation;
* Update requirements.

0.2.3 (2019-04-02)
------------------

* Update requirements;
* Fix type hints for query functions;
* Reorganise query classes into a single class;
* Update documentation.

0.2.4 (2019-04-04)
------------------

* Fix type hints;
* Fix docstrings in classes;
* Add docstrings to main entry points.

0.2.5 (2019-04-09)
------------------

* Fix test files with new BioMart versions;
* Add script to create test files automatically.

0.2.6 (2019-04-29)
------------------

* Update test files;
* Fix and update documentation.

0.3.0 (2019-05-05)
==================

* Change ``list_*`` functions names to ``find_*`` for better compliance;
* Update documentation.

0.3.1 (2019-05-11)
------------------

* Fix requirements handling;
* Add function to check internet connection.

0.3.2 (2019-05-29)
------------------

* Correct minor typos;
* Update documentation and testfiles.

0.3.3 (2019-07-29)
------------------

* Fix #37 - issue with the requests module not installed.

0.3.4 (2019-08-23)
------------------

* Better handling of filters arguments for ``query()`` and ``aquery()`` functions;
* Convert docstrings to Google style;
* Fix documentation.

0.3.5 (2019-08-25)
------------------

* Relax requirement versions.

0.4.0 (2020-01-26)
==================

* Add CLI commands for finding marts, datasets, attributes and filters;
* Change output dataframe column names.

0.5.0 (2020-03-22)
==================

* Add CLI and Python module options to save outputs to CSV file.
