import unittest
import repositories.member_repository as member_repo
from models.member import Member


class TestMemberRepository(unittest.TestCase):

    def setUp(self):
        pass

    # @unittest.skip("Delete to run the test")
    def test_save(self):  
        member1 = Member("Kathryn McVitie")
        member_repo.save(member1)
        members = member_repo.select_all()  
        member = member_repo.select(members[-1].id) 
        self.assertEqual("Kathryn McVitie", member.name)

    # @unittest.skip("Delete to run the test")
    def test_select(self):
        member1 = Member("Kathryn McVitie")
        member_repo.save(member1)
        members = member_repo.select_all()  
        member = member_repo.select(members[-1].id) 
        self.assertEqual("Kathryn McVitie", member.name)

    # @unittest.skip("Delete to run the test")
    def test_select_all(self):
        members = member_repo.select_all()
        self.assertEqual(2, len(members))

    # @unittest.skip("Delete to run the test")
    def test_delete(self):
        members_before = member_repo.select_all()  
        member = member_repo.select(members_before[-1].id)
        member_repo.delete(member.id)
        members_after = member_repo.select_all()  
        self.assertEqual(len(members_after), len(members_before)-1) 

    # @unittest.skip("Delete to run the test")
    def test_delete_all(self):
        member_repo.delete_all()
        members = member_repo.select_all()
        self.assertEqual(0, len(members))

    @unittest.skip("Delete to run the test")
    def test_update(self):
        pass

    @unittest.skip("Delete to run the test")
    def test_sessions(self):
        pass
