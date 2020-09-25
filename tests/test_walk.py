from map_ops import walk
import unittest


class test_walk(unittest.TestCase):
    def test_all_defaults(self):
        # basically just return left
        d1 = {"foo": 1, "bar": 1}
        d2 = {"foo": 2, "baz": 2}
        gold = {"foo": 1, "bar": 1}
        output = walk(d1, d2)
        self.assertEqual(gold, output)

    def test_initializer(self):
        d1 = {"foo": 1, "bar": 1}
        d2 = {"foo": 2, "baz": 2}
        initializer = lambda x, y: y
        gold = {"foo": 2, "bar": 1, "baz": 2}
        output = walk(d1, d2, initializer=initializer)
        self.assertEqual(gold, output)
        
    def test_value_comparator(self):
        d1 = {"foo": 1, "bar": 1}
        d2 = {"foo": 2, "baz": 2}
        compare = lambda x, y: y
        gold = {"foo": 2, "bar": 1}
        output = walk(d1, d2, value_comparator=compare)
        self.assertEqual(gold, output)

    def test_list_strategy(self):
        from functools import reduce

        d1 = {"foo": [1, 2, 3]}
        d2 = {"foo": [1, 2, 3]}

        def list_strat(l1, l2):
            return reduce(lambda x, y: x + y, l1)

        gold = {"foo": 6}
        output = walk(d1, d2, list_strategy=list_strat)
        self.assertEqual(gold, output)


if __name__ == "__main__":
    unittest.main()
