from map_ops.core import diff_, put_


__all__ = ["rmerge", "rdiff"]


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
    return put_(
        d1,
        d2,
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
    return diff_(
        d1,
        d2,
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

    end_slice = min(len(l1), len(l2))
    diffs = [
        l1[idx] if l1[idx] != l2[idx] else None
        for idx in range(end_slice)
    ]
    remainder = l1[end_slice:]

    return diffs + remainder
