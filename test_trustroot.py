# test_trustroot.py
"""
Tests for TrustRoot module.
"""

import unittest
from trustroot import TrustRoot

class TestTrustRoot(unittest.TestCase):
    """Test cases for TrustRoot class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = TrustRoot()
        self.assertIsInstance(instance, TrustRoot)
        
    def test_run_method(self):
        """Test the run method."""
        instance = TrustRoot()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
