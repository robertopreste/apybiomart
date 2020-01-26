===
API
===

Python Module
=============

Entry points
------------

These functions are available after you ``import apybiomart`` and should be used as the main entry
points for apybiomart. If you want more control, you can use the internal classes described below.

.. automodule:: apybiomart.apybiomart
    :members:


Internal classes
----------------

These are the internal classes used by apybiomart, and can be imported with
``from apybiomart.classes import <ClassName>``. Use them if you want more control over the
application.

.. automodule:: apybiomart.classes
    :members:

____

Command Line Interface
======================

.. click:: apybiomart.cli:main
    :prog: apybiomart
    :show-nested:
