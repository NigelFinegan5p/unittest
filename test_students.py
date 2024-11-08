import unittest
from student import Student


class TestStudent(unittest.TestCase):

    def test_full_name(self):
        print("test_full_name")
        self.assertEqual(self.student.full_name, "John Doe")


