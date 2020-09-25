from map_ops.operations import (
    diff,
    put,
    cut,
    rmerge,
    rdiff,
)
import unittest


class test_diff(unittest.TestCase):
    def test_falsy_side(self):
        cases = [({"foo": 1}, {}), ({}, {"foo": 1})]

        for obj1, obj2 in cases:
            self.assertEqual(diff(obj1, obj2), {"foo": 1})

    def test_no_diff(self):
        obj1 = {"foo": 1}
        obj2 = {"foo": 1}
        gold = {}
        output = diff(obj1, obj2)
        self.assertEqual(gold, output)

    def test_single_level(self):
        obj1 = {"foo": None, "bar": 1, "qux": 1}
        obj2 = {"foo": 1, "baz": 2}
        gold = {"bar": 1, "qux": 1}
        output = diff(obj1, obj2)
        self.assertEqual(gold, output)

    def test_mult_level(self):
        obj1 = {"foo": {"bar": {"baz": 1, "dur": 1}}}
        obj2 = {"foo": {"bar": {"qux": 1}}}
        gold = {"foo": {"bar": {"baz": 1, "dur": 1}}}
        output = diff(obj1, obj2)
        self.assertEqual(gold, output)

    def test_multi_level_does_not_return_falsy_dict(self):
        obj1 = {"foo": {"bar": {"baz": 1}}}
        obj2 = {"foo": {"bar": {"baz": 1}}}
        gold = {}
        output = diff(obj1, obj2)
        self.assertEqual(gold, output)


class test_put(unittest.TestCase):
    def test_falsy_sides(self):
        cases = [({"foo": 1}, {}), ({}, {"foo": 1})]

        for obj1, obj2 in cases:
            self.assertEqual(put(obj1, obj2), {"foo": 1})

    def test_no_change(self):
        obj1 = {"foo": 1}
        obj2 = {"foo": 1}
        gold = {"foo": 1}
        output = put(obj1, obj2)
        self.assertEqual(gold, output)

    def test_single_level(self):
        obj1 = {"bar": 1, "qux": 1}
        obj2 = {"foo": 1}
        gold = {"bar": 1, "foo": 1, "qux": 1}
        output = put(obj1, obj2)
        self.assertEqual(gold, output)

    def test_mult_level(self):
        obj1 = {"foo": {"bar": {"baz": 1, "dur": 1}}}
        obj2 = {"foo": {"bar": {"qux": 1}}}
        gold = {
            "foo": {"bar": {"qux": 1, "baz": 1, "dur": 1}}
        }
        output = put(obj1, obj2)
        self.assertEqual(gold, output)


class test_cut(unittest.TestCase):
    def test_falsy_sides(self):
        cases = [({"foo": 1}, {}), ({}, {"foo": 1})]

        for obj1, obj2 in cases:
            self.assertEqual(cut(obj1, obj2), {"foo": 1})

    def test_no_change(self):
        obj1 = {"bar": 1}
        obj2 = {"foo": 1}
        gold = {"foo": 1}
        output = cut(obj1, obj2)
        self.assertEqual(gold, output)

    def test_single_level(self):
        obj1 = {"bar": None, "baz": None}
        obj2 = {"foo": 1, "bar": 1, "baz": 1}
        gold = {"foo": 1}
        output = cut(obj1, obj2)
        self.assertEqual(gold, output)

    def test_mult_level(self):
        obj1 = {"foo": {"bar": {"baz": 1, "qux": 1}}}
        obj2 = {"foo": {"bar": {"baz": 1, "qux": 1}}}
        gold = {}
        output = cut(obj1, obj2)
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
        gold = {"bar": [None, 2, None], "baz": {"one": 1}}
        output = rdiff(obj1, obj2)
        self.assertEqual(gold, output)


if __name__ == "__main__":
    unittest.main()
