import unittest
import pandas as pd
from pandas.testing import assert_frame_equal
from src.identify_and_remove_duplicates import identify_and_remove_duplicates


class TestIdentifyAndRemoveDuplicates(unittest.TestCase):
    def test_identify_and_remove_duplicates(self):
        """
        Test that the definition removes duplicates
        """

        d = pd.DataFrame({'col1': [1, 2, 1], 'col2': [3, 4, 3]})

        result = identify_and_remove_duplicates(d)
        expected_result = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
        assert_frame_equal(result, expected_result)

    def test_no_duplicates(self):
        """
        Test that the definition removes duplicates
        """

        d = pd.DataFrame({'col1': [1, 2, 2], 'col2': [3, 4, 3]})

        result = identify_and_remove_duplicates(d)

        assert_frame_equal(result, d)

    def test_duplicates_keep_first(self):
        """
        Test that the definition removes duplicates
        """
        d = pd.DataFrame({'col1': [1, 2, 1, 4], 'col2': [3, 4, 3, 5]})

        result = identify_and_remove_duplicates(d)
        expected_d = pd.DataFrame({'col1': [1, 2, 4], 'col2': [3, 4, 5]})
        assert_frame_equal(result.reset_index(drop=True), expected_d.reset_index(drop=True))

if __name__ == '__main__':
    unittest.main()
