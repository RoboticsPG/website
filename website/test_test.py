from django.test import TestCase

class TestTest(TestCase):
    def test_fails(self):
        """This test should fail"""
        self.assertEqual(True, False)

    def test_pass(self):
        """This test should pass"""
        self.assertEqual(True, True)
