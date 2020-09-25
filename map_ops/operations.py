from map_ops.walk import walk
from copy import deepcopy


__all__ = ["cut", "diff", "put", "rmerge", "rdiff"]


# fully composable functions
# ----------------------------------------------------------
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
    return walk(d1, d2, initializer=lambda x, y: {})


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
    d2 = deepcopy(d2)
    return walk(d1, d2, initializer=lambda x, y: y)


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
    return walk(d2, d1, initializer=lambda x, y: {})


# less composable functions
# ----------------------------------------------------------
def rmerge(d1: dict, d2: dict) -> dict:
    """Recursively merges `d1` and `d2`, merging lists via
    simple __add__ (non-mutating action)

    Examples:
        >>> d1 = {"foo": 1, "bar": [1, 2]}
        >>> d2 = {"baz": 2, "bar": [3, 4]}
        >>> rmerge(d1, d2)
        {"foo": 1, "bar": [1, 2, 3, 4], "baz": 2}

    Args:
        d1: A Python dict
        d2: A Python dict

    Returns:
        A Python dict
    """
    d2 = deepcopy(d2)
    return walk(
        d1,
        d2,
        initializer=lambda x, y: y,
        list_strategy=lambda x, y: x + y,
    )


def rdiff(d1: dict, d2: dict) -> dict:
    """Recursively differences `d1` and `d2`, positionally
    comparing any lists (similar to clojure.datat/diff);
    (non-mutating action)

    Examples:
        >>> d1 = {"foo": 1, "bar": [1, 2, 3]}
        >>> d2 = {"foo": 2, "bar": [3, 2, 1, 4]}
        >>> rdiff(d1, d2)
        {"foo": 1, "bar": [1, None, 3]}

    Args:
        d1: A Python dict
        d2: A Python dict

    Returns:
        A Python dict
    """
    return walk(
        d1,
        d2,
        initializer=lambda x, y: {},
        value_comparator=lambda x, y: x,
        list_strategy=_diff_list,
    )


def _diff_list(l1: list, l2: list) -> list:
    """
    positional comparison mimicking Clojure's
    clojure.data/diff function
    """
    if l1 == l2:
        return []
    return [
        element if element != l2[idx] else None
        for idx, element in enumerate(l1)
    ]
