from unittest import TestCase
from ivt.initialization.playergen import NameGenerator


class NameGeneratorTestCase(TestCase):
    def test_when_getting_n_names_return_list_with_n_names(self):
        set_of_names = NameGenerator.get_set_of_random_names(4)
        self.assertEqual(len(set_of_names), 4)
