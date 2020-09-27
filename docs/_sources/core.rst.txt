core
====

Generalized procedures backing :meth:`map_ops.operations`. 
If you need greater control over specific behavior as it pertains to any of the
basic ``operations`` functions, use these instead.

Examples
--------
Here are some case studies for how you could write a custom ``put`` function
that concatenates lists. The first one is only concerned with lists occuring at
the "top" level of a dictionary (ie, excluding lists WITHIN lists):

.. highlight:: python
.. code-block:: python

    from map_ops.core import put_

    d1 = {
        "foo": {
            "bar": [1, 2]
        }
    }
    d2 = {
        "foo": {
            "bar": [3, 4]
        }
    }

    def l_put(d1, d2):
        strategy = lambda x, y: x + y
        return put_(d1, d2, list_strategy=strategy)

    l_put(d1, d2)
    {
        "foo": {
            "bar": [1, 2, 3, 4]
        }
    }

We can up the game a little and assume we want to also concatenate lists within
complex objects which are, themselves, in a list:

.. highlight:: python
.. code-block:: python

    from map_ops.core import put_
    from functools import reduce

    d1 = {
        "foo": [
            {"bar": [1, 2]},
            {"bar": [3, 4]}
        ]
    }
    d2 = {
        "foo": [
            {"baz": 1, "bar": [5, 6]}
        ]
    }

    def strategy(l1, l2):
        if not isinstance(l1[0], dict):
            # what to do with a list of primitives
            return l1 + l2
        # what to do with a list of dicts
        return reduce(
            lambda x, y: put_(x, y, list_strategy=strategy),
            l1 + l2
        )

    put_(d1, d2, list_strategy=strategy)
    {
        "foo": [
            {
                "baz": 1,
                "bar": [1, 2, 3, 4, 5, 6]
            }
        ]
    }


.. automodule:: map_ops.core
    :members: cut_, diff_, put_
