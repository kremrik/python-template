from map_ops.operations import diff, put, cut
import unittest


class test_diff(unittest.TestCase):
    def test_falsy_left_side(self):
        obj1 = {}
        obj2 = {"foo": 1}
        gold = {}
        output = diff(obj1, obj2)
        self.assertEqual(gold, output)

    def test_falsy_right_side(self):
        obj1 = {"foo": 1}
        obj2 = {}
        gold = {"foo": 1}
        output = diff(obj1, obj2)
        self.assertEqual(gold, output)

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

    def test_pseudo_immutability(self):
        obj1 = {"foo": 1, "bar": [1, 2]}
        obj2 = {"foo": 1}
        gold = {"bar": [1, 2]}
        output = diff(obj1, obj2)
        obj1["bar"].append(3)
        self.assertEqual(gold, output)


class test_put(unittest.TestCase):
    def test_falsy_left_side(self):
        obj1 = {}
        obj2 = {"foo": 1}
        gold = {"foo": 1}
        output = put(obj1, obj2)
        self.assertEqual(gold, output)

    def test_falsy_right_side(self):
        obj1 = {"foo": 1}
        obj2 = {}
        gold = {"foo": 1}
        output = put(obj1, obj2)
        self.assertEqual(gold, output)

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

    def test_pseudo_immutability(self):
        obj1 = {"foo": 1}
        obj2 = {"bar": [1, 2]}
        gold = {"foo": 1, "bar": [1, 2]}
        output = put(obj1, obj2)
        obj2["bar"].append(3)
        self.assertEqual(gold, output)


class test_cut(unittest.TestCase):
    def test_falsy_left_side(self):
        obj1 = {}
        obj2 = {"foo": 1}
        gold = {"foo": 1}
        output = cut(obj1, obj2)
        self.assertEqual(gold, output)

    def test_falsy_right_side(self):
        obj1 = {"foo": 1}
        obj2 = {}
        gold = {}
        output = cut(obj1, obj2)
        self.assertEqual(gold, output)

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

    def test_pseudo_immutability(self):
        obj1 = {"foo": 1}
        obj2 = {"foo": 1, "bar": [1, 2]}
        gold = {"bar": [1, 2]}
        output = cut(obj1, obj2)
        obj2["bar"].append(3)
        self.assertEqual(gold, output)


if __name__ == "__main__":
    unittest.main()
