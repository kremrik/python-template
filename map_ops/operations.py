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
    return _traverse(obj1, obj2, lambda x: type(obj1)())


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
    return _traverse(obj1, obj2, lambda x: deepcopy(x))


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
    return _traverse(obj2, obj1, lambda x: type(obj1)())


def _traverse(obj1, obj2, initializer=None, output=None):
    if not obj1 or not obj2:
        return obj1 or obj2

    output = initializer(obj2)

    for k in obj1:
        v = obj1[k]
        if k not in obj2:
            output[k] = v

        elif isinstance(v, type(obj1)):
            res = _traverse(
                v, obj2[k], initializer, output
            )
            if res:
                output[k] = res

    return output
