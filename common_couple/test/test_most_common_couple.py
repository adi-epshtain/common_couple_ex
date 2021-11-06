import unittest
import logging as log

from NCR_EX.common_couple.utils import find_most_common_couple


class TestMostCommonCouple(unittest.TestCase):
    def setUp(self):

        log.info("{} Test: {}".format("#"*100, self._testMethodName))
        log.info("Test Description: {}".format(self.shortDescription()))

    def test_most_common_couple_happy_flow(self):
        """
        Test get function most common couple happy flow
        expected to get the suitable tuple of items were bought together in the same basket the most.
        """
        expected_first_item = 'Kidney Beans'
        expected_second_item = 'Kidney Beans'

        baskets = [['Milk', 'Onion', 'Nutmeg', 'Kidney Beans', 'Eggs', 'Yogurt'],
                   ['Dill', 'Onion', 'Nutmeg', 'Kidney Beans', 'Eggs', 'Yogurt'],
                   ['Milk', 'Apple', 'Kidney Beans', 'Eggs'],
                   ['Milk', 'Unicorn', 'Corn', 'Kidney Beans', 'Yogurt'],
                   ['Corn', 'Onion', 'Onion', 'Kidney Beans', 'Ice cream', 'Eggs']]

        results = find_most_common_couple(baskets)
        self.assertIn(expected_first_item, results)
        self.assertIn(expected_second_item, results)

    def test_most_common_couple_happy_flow2(self):
        """
        Test get function most common couple happy flow
        expected to get the suitable tuple of items were bought together in the same basket the most.
        """
        expected_first_item = 'meat'
        expected_second_item = 'ketchup'

        baskets = [['coke', 'ice', 'meat', 'ketchup', 'apple', 'banana'],
                   ['coke', 'bread', 'meat', 'ketchup', 'apple', 'strawberry'],
                   ['coke', 'pepsi', 'meat', 'ketchup', 'apple', 'banana'],
                   ['pepsi', 'ice', 'meat', 'bread', 'tomato', 'cucumber'],
                   ['sprite', 'rum', 'meat', 'ketchup', 'strawberry', 'banana']]

        results = find_most_common_couple(baskets)
        self.assertIn(expected_first_item, results)
        self.assertIn(expected_second_item, results)

    def test_most_common_couple_failed(self):
        """
        Test get function most common couple failed flow
        expected to get ("", "")
        """
        expected_first_item = ''
        expected_second_item = ''

        baskets = []

        results = find_most_common_couple(baskets)
        self.assertIn(expected_first_item, results)
        self.assertIn(expected_second_item, results)

