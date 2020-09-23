from examples.json_schema import JsonSchema
from map_ops import diff, put, cut
import unittest


schema1 = JsonSchema(
    {
        "type": "object", 
        "properties": {
            "foo": {
                "type": "integer"
            }, 
            "bar": {
                "type": "number"
            }
        }
    }
)

schema2 = JsonSchema(
    {
        "type": "object", 
        "properties": {
            "foo": {
                "type": "integer"
            }, 
            "baz": {
                "type": "string"
            }
        }
    }
)


class test(unittest.TestCase):

    def test_diff(self):
        gold = JsonSchema(
            {
                "type": "object", 
                "properties": {
                    "bar": {
                        "type": "number"
                    }
                }
            }
        )
        output = diff(schema1, schema2)
        self.assertEqual(gold, output)

    def test_put(self):
        gold = JsonSchema(
            {
                "type": "object", 
                "properties": {
                    "foo": {
                        "type": "integer"
                    }, 
                    "bar": {
                        "type": "number"
                    },
                    "baz": {
                        "type": "string"
                    }
                }
            }
        )
        output = put(schema1, schema2)
        self.assertEqual(gold, output)

    def test_cut(self):
        gold = JsonSchema(
            {
                "type": "object", 
                "properties": {
                    "baz": {
                        "type": "string"
                    }
                }
            }
        )
        output = cut(schema1, schema2)
        self.assertEqual(gold, output)


if __name__ == "__main__":
    unittest.main()
