map_ops
=======
https://github.com/kremrik/map-ops

A simple, but high-powered, module for operating on dictionaries. 

Introduction
------------
``map_ops`` was designed to be the simplest possible way to add keys/values,
remove keys/values, and find differences between two dictionaries. However,
closure under composition allows you to treat a small set of functions as a
DSL of-sorts, providing sophisticated behavior with minimal effort.

Basic Usage
-----------
The most basic usage is obtained in :ref:`operations`. 
This module exposes three functions, fully closed under combination, and
returning new objects (no weird behavior when mutating original objects).

   .. highlight:: python
   .. code-block:: python

      from map_ops.operations import cut, diff, put

      d1 = {"foo": 1, "bar": 1}
      d2 = {"foo": 2, "baz": 2}

      diff(d1, d2)
      {"bar": 1}

      put(d1, d2)
      {"foo": 2, "baz": 2, "bar": 1}

      cut(d1, d2)
      {"baz": 2}


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   operations
   other
   core

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
