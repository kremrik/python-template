from map_ops.walk import walk
from copy import deepcopy


__all__ = ["cut", "diff", "put"]


def diff(obj1, obj2):
    """Returns the key/value subset of `obj1` not in `obj2`

    Examples:
        >>> obj1 = {"foo": 1, "bar": 1}
        >>> obj2 = {"foo": 2, "baz": 2}
        >>> diff(obj1, obj2)
        {"bar": 1}

    Args:
        obj1: A Python dict
        obj2: A Python dict

    Returns:
        A Python dict
    """
    initializer = lambda x, y: {}
    return walk(obj1, obj2, initializer=initializer)


def put(obj1, obj2):
    """Adds the keys/values in `obj1` to `obj2` if they do not
    already exist (non-mutating action)

    Examples:
        >>> obj1 = {"foo": 1, "bar": 1}
        >>> obj2 = {"foo": 2, "baz": 2}
        >>> put(obj1, obj2)
        {"foo": 2, "baz": 2, "bar": 1}

    Args:
        obj1: A Python dict
        obj2: A Python dict

    Returns:
        A Python dict
    """
    obj2 = deepcopy(obj2)
    initializer = lambda x, y: y
    return walk(obj1, obj2, initializer=initializer)


def cut(obj1, obj2):
    """Removes the keys/values in `obj1` to `obj2` if they do
    not already exist (non-mutating action)

    Examples:
        >>> obj1 = {"foo": 1, "bar": 1}
        >>> obj2 = {"foo": 2, "baz": 2}
        >>> cut(obj1, obj2)
        {"baz": 2}

    Args:
        obj1: A Python dict
        obj2: A Python dict

    Returns:
        A Python dict
    """
    initializer = lambda x, y: {}
    return walk(obj2, obj1, initializer=initializer)
