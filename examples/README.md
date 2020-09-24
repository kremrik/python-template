### Using map-ops with other objects

`map_ops` exposes the `diff`, `put`, and `cut` functions for any object that
functions like a mapping type (ie, implements the following methods):
- `__getitem__`
- `__setitem__`
- `__iter__`
- `__bool__`

It's also required to have a "default" value to return when the constructor is
called with no args. Similar to how you can call `dict()` and produce an empty
dictionary, your mapping type must initialize to a sensible value that allows
for closure under combination. 

The included `json_schema.py` and `test_json_schema.py` files should be 
sufficient for demonstration.

Note that it will not work with array types as-is. It's just a simple example.