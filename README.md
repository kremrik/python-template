# map-ops
A simple, but high-powered, module for operating on dictionaries

### Examples
For comprehensive examples, please read the [docs](https://kremrik.github.io/map-ops/)

```python
from map_ops.operations import cut, diff, put

d1 = {"foo": 1, "bar": 1}
d2 = {"foo": 2, "baz": 2}

diff(d1, d2)
{"bar": 1}

put(d1, d2)
{"foo": 2, "baz": 2, "bar": 1}

cut(d1, d2)
{"baz": 2}
```
