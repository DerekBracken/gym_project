import unittest
from models.member import Member


class TestMember(unittest.TestCase):

    def setUp(self):
        self.member1 = Member("Cathal", "Wilson", True)
        self.member2 = Member("Kathryn", "McVitie", False, 10)

    # @unittest.skip("Delete this line to run the test")
    def test_has_name(self):
        self.assertEqual('Cathal', self.member1.first_name)

    # @unittest.skip("Delete this line to run the test")
    def test_has_name(self):
        self.assertEqual('Wilson', self.member1.last_name)

    # @unittest.skip("Delete this line to run the test")
    def test_has_premium_True(self):
        self.assertEqual(True, self.member1.premium)

    # @unittest.skip("Delete this line to run the test")
    def test_has_premium_False(self):
        self.assertEqual(False, self.member2.premium)

    # @unittest.skip("Delete this line to run the test")
    def test_has_id(self):
        self.assertEqual(10, self.member2.id)
