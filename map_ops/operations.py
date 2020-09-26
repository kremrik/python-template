from map_ops.core import diff_, put_, cut_


__all__ = ["cut", "diff", "put"]


def diff(d1: dict, d2: dict) -> dict:
    """Returns the key/value subset of `d1` not in `d2`

    Examples:
        >>> d1 = {"foo": 1, "bar": 1}
        >>> d2 = {"foo": 2, "baz": 2}
        >>> diff(d1, d2)
        {"bar": 1}

    Args:
        d1: A Python dict
        d2: A Python dict

    Returns:
        A Python dict
    """
    return diff_(d1, d2)


def put(d1: dict, d2: dict) -> dict:
    """Adds the keys/values in `d1` to `d2` if they do not
    already exist (non-mutating action)

    Examples:
        >>> d1 = {"foo": 1, "bar": 1}
        >>> d2 = {"foo": 2, "baz": 2}
        >>> put(d1, d2)
        {"foo": 2, "baz": 2, "bar": 1}

    Args:
        d1: A Python dict
        d2: A Python dict

    Returns:
        A Python dict
    """
    return put_(d1, d2)


def cut(d1: dict, d2: dict) -> dict:
    """Removes the keys/values in `d1` to `d2` if they do
    not already exist (non-mutating action)

    Examples:
        >>> d1 = {"foo": 1, "bar": 1}
        >>> d2 = {"foo": 2, "baz": 2}
        >>> cut(d1, d2)
        {"baz": 2}

    Args:
        d1: A Python dict
        d2: A Python dict

    Returns:
        A Python dict
    """
    return cut_(d1, d2)
