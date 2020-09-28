.. _operations:

operations
==========
The basic building-blocks of ``map_ops``

Examples
--------

``diff``, ``put``, and ``cut`` are closed under combination, allowing for
advanced functionality with minimal effort. For example, let's say we have a
stream of records (dicts) headed our way. We also need those records to have an
identical set of keys, since the incoming records vary in shape. Here's how we
can accomplish this:

.. highlight:: python
.. code-block:: python

    from map_ops.operations import cut, diff, put

    template = {
        "foo": 0,
        "bar": "",
        "baz": 0.0
    }

    record = {
        "foo": 42,
        "bar": "ni",
        "qux": True
    }

    # which fields need to be removed?
    diff(record, template)
    {'qux': True}

    # which fields do we need to add?
    diff(template, record)
    {'baz': 0.0}

    # fix it with a one-liner!
    put(diff(template, record), cut(diff(record, template), record))
    {'foo': 42, 'bar': 'ni', 'baz': 0.0}

    # we could actually make it shorter by just letting
    # `put` skip existing fields in `template`
    put(template, cut(diff(record, template), record))
    {'foo': 42, 'bar': 'ni', 'baz': 0.0}


Let's figure out the superset of keys a list of dicts contains:

.. highlight:: python
.. code-block:: python

    from map_ops.operations import cut, diff, put
    from functools import reduce
    
    messy_array = [
        {"foo": 1},
        {"bar": 2},
        {"foo": 3, "qux": 3}
    ]

    reduce(
        lambda d1, d2: put(d1, d2), 
        messy_array
    ).keys()
    dict_keys(['foo', 'qux', 'bar'])


.. automodule:: map_ops.operations
    :members: cut, diff, put
