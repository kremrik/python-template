from typing import Iterable, Optional


class JsonSchema(object):
    def __init__(self, schema: Optional[dict] = None):
        if schema:
            self.schema = schema
        else:
            # barebones json-schema definition
            self.schema = {"type": "object"}

    def __getitem__(self, key: str) -> "JsonSchema":
        # `map_ops` determines whether to recurse based on
        # whether the value corresponding to a given key is
        # of the same type as its parent, so if we're at
        # the "bottom" of a tree, we don't want it to be of
        # the same type as its parent (ie, primitive). This
        # is similar to not recursing at {"foo": 1} because
        # the value corresponding to "foo" is not a dict.

        properties = self._get_properties()
        value = properties[key]

        if "properties" in value:
            return JsonSchema(value)
        return value

    def __setitem__(self, key: str, value: dict) -> None:
        properties = self._get_properties()

        if not properties:
            self.schema["properties"] = properties
        properties[key] = value
    
    def __iter__(self) -> Iterable:
        yield from self._get_properties()

    def __bool__(self) -> bool:
        # This makes sure that, for example, if we diff two
        # identical nested schemas, we still return a falsy
        # result (in this case, `{"type": "object"}`)
        
        if "properties" not in self.schema:
            return False
        return True

    def __eq__(self, other: "JsonSchema") -> bool:
        return self.schema == other.schema

    def __repr__(self) -> str:
        return str(self.schema)

    def _get_properties(self) -> dict:
        return self.schema.get("properties", {})
