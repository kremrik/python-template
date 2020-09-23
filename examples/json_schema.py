from typing import Iterable, Optional


class JsonSchema(object):
    def __init__(self, schema: Optional[dict] = None):
        if schema:
            self.schema = schema
        else:
            self.schema = {"type": "object"}

    def __getitem__(self, key: str) -> "JsonSchema":
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

    def __bool__(self) -> bool:
        if "properties" not in self.schema:
            return False
        if len(self.schema["properties"]) == 0:
            return False
        return True

    def __iter__(self) -> Iterable:
        yield from self._get_properties()

    def __repr__(self) -> str:
        return str(self.schema)

    def _get_properties(self) -> dict:
        return self.schema.get("properties", {})
