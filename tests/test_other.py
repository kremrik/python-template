from map_ops.other import rdiff, rmerge
import unittest


class test_rmerge(unittest.TestCase):
    def test_falsy_left_side(self):
        obj1 = {}
        obj2 = {"foo": 1}
        gold = {"foo": 1}
        output = rmerge(obj1, obj2)
        self.assertEqual(gold, output)

    def test_falsy_right_side(self):
        obj1 = {"foo": 1}
        obj2 = {}
        gold = {"foo": 1}
        output = rmerge(obj1, obj2)
        self.assertEqual(gold, output)

    def test_rmerge(self):
        obj1 = {"foo": 1, "bar": [1, 2], "baz": {"one": 1}}
        obj2 = {"bar": [3, 4], "baz": {"two": 2}, "qux": 1}
        gold = {
            "foo": 1,
            "bar": [1, 2, 3, 4],
            "baz": {"one": 1, "two": 2},
            "qux": 1,
        }
        output = rmerge(obj1, obj2)
        self.assertEqual(gold, output)

    def test_pseudo_immutability(self):
        obj1 = {"foo": 1}
        obj2 = {"foo": 1, "bar": [1, 2]}
        gold = {"foo": 1, "bar": [1, 2]}
        output = rmerge(obj1, obj2)
        obj2["bar"].append(3)
        self.assertEqual(gold, output)


class test_rdiff(unittest.TestCase):
    def test_falsy_left_side(self):
        obj1 = {}
        obj2 = {"foo": 1}
        gold = {}
        output = rdiff(obj1, obj2)
        self.assertEqual(gold, output)

    def test_falsy_right_side(self):
        obj1 = {"foo": 1}
        obj2 = {}
        gold = {"foo": 1}
        output = rdiff(obj1, obj2)
        self.assertEqual(gold, output)

    def test_no_change(self):
        obj1 = {"foo": {"bar": [1, 2]}}
        obj2 = {"foo": {"bar": [1, 2]}}
        gold = {}
        output = rdiff(obj1, obj2)
        self.assertEqual(gold, output)

    def test_rdiff(self):
        obj1 = {
            "foo": 1,
            "bar": [1, 2, 3],
            "baz": {"one": 1},
        }
        obj2 = {
            "foo": 1,
            "bar": [3, 2, 1],
            "baz": {"two": 2},
            "qux": 1,
        }
        gold = {"bar": [1, None, 3], "baz": {"one": 1}}
        output = rdiff(obj1, obj2)
        self.assertEqual(gold, output)

    def test_rdiff_equal_lists(self):
        obj1 = {
            "foo": 1,
            "bar": [1, 2, 3],
            "baz": {"one": 1},
        }
        obj2 = {
            "foo": 1,
            "bar": [1, 2, 3],
            "baz": {"two": 2},
            "qux": 1,
        }
        gold = {"baz": {"one": 1}}
        output = rdiff(obj1, obj2)
        self.assertEqual(gold, output)

    def test_pseudo_immutability(self):
        obj1 = {"foo": [1, 2, 3]}
        obj2 = {"foo": [1, 2]}
        gold = {"foo": [None, None, 3]}
        output = rdiff(obj1, obj2)
        obj2["foo"].append(4)
        self.assertEqual(gold, output)


if __name__ == "__main__":
    unittest.main()
