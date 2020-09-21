from copy import deepcopy
from typing import Union


__all__ = ["cut", "diff", "put"]


def diff(d1: dict, d2: dict) -> Union[None, dict]:
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
    if not d1 or not d2:
        return d1 or d2

    return _traverse(d1, d2, lambda x: {})


def put(d1: dict, d2: dict) -> Union[None, dict]:
    """Adds the keys/values in `d1` to `d2` if they do not
    already exist (non-mutating action)

    Examples:
        >>> d1 = {"baz": 1}
        >>> d2 = {"foo": 2, "bar": 2}
        >>> put(d1, d2)
        {"foo": 2, "bar": 2, "baz": 1}

    Args:
        d1: A Python dict
        d2: A Python dict

    Returns:
        A Python dict
    """
    if not d1 or not d2:
        return d1 or d2

    return _traverse(d1, d2, lambda x: deepcopy(x))


def cut(d1: dict, d2: dict) -> Union[None, dict]:
    """Removes the keys/values in `d1` to `d2` if they do
    not already exist (non-mutating action)

    Examples:
        >>> d1 = {"bar": None}
        >>> d2 = {"foo": 2, "bar": 2}
        >>> cut(d1, d2)
        {"foo": 2}

    Args:
        d1: A Python dict
        d2: A Python dict

    Returns:
        A Python dict
    """
    if not d1 or not d2:
        return d1 and d2

    return _traverse(d2, d1, lambda x: {})


def _traverse(d1, d2, initializer=None, output=None):
    output = initializer(d2)

    for k, v in d1.items():
        if k not in d2:
            output[k] = v

        if isinstance(v, dict):
            return {
                k: _traverse(
                    v, d2.get(k), initializer, output
                )
            }

    return output
