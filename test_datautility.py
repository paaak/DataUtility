# test_datautility.py
"""
Tests for DataUtility module.
"""

import unittest
from datautility import DataUtility

class TestDataUtility(unittest.TestCase):
    """Test cases for DataUtility class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DataUtility()
        self.assertIsInstance(instance, DataUtility)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DataUtility()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
