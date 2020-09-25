from typing import Any, Callable


__all__ = ["walk"]


def walk(
    d1: dict,
    d2: dict,
    initializer: Callable[[dict, dict], dict] = None,
    value_comparator: Callable[[Any, Any], Any] = None,
    list_strategy: Callable[[Any, Any], Any] = None,
):
    """
    initializer is best described by: "traverse d1 with
    respect to _, where _ is one of d1 or d2"
    """

    if not d1 or not d2:
        return d1 or d2

    if not initializer:
        initializer = lambda x, y: x
    if not value_comparator:
        value_comparator = lambda x, y: None
    if not list_strategy:
        list_strategy = lambda x, y: x

    output = initializer(d1, d2)

    for k, v in d1.items():
        res = None

        if k not in d2:
            res = v

        elif isinstance(v, dict):
            res = walk(
                v,
                d2[k],
                initializer,
                value_comparator,
                list_strategy,
            )

        elif isinstance(v, list):
            res = list_strategy(v, d2[k])

        elif v != d2[k]:
            res = value_comparator(v, d2[k])

        else:
            # nothing to do!
            pass

        if res:
            output[k] = res

    return output
