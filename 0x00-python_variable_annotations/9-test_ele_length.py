#!/usr/bin/env python3
import unittest
element_length = __import__('9-element_length').element_length  # Replace with the actual module name

class TestElementLength(unittest.TestCase):
    
    def test_strings(self):
        # Test with a list of strings
        data = ["apple", "banana", "cherry"]
        result = element_length(data)
        expected = [("apple", 5), ("banana", 6), ("cherry", 6)]
        self.assertEqual(result, expected)
        
    def test_empty_list(self):
        # Test with an empty list
        data = []
        result = element_length(data)
        expected = []
        self.assertEqual(result, expected)
        
    def test_mixed_sequences(self):
        # Test with a list containing mixed sequences (strings, lists, tuples)
        data = ["hello", [1, 2, 3], (4, 5)]
        result = element_length(data)
        expected = [("hello", 5), ([1, 2, 3], 3), ((4, 5), 2)]
        self.assertEqual(result, expected)

    def test_nested_sequences(self):
        # Test with nested sequences
        data = [[1, [2, 3]], "test", ("nested", "tuple")]
        result = element_length(data)
        expected = [([1, [2, 3]], 2), ("test", 4), (("nested", "tuple"), 2)]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
