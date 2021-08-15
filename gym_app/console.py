import pdb
from models.member import Member
from models.session import Session
from models.booking import Booking

import repositories.member_repository as member_repo
import repositories.session_repository as session_repo
import repositories.booking_repository as booking_repo


member_repo.delete_all()
session_repo.delete_all()

session1 = Session("Yoga", "Viniyoga", "11:00", "Tuesday", 20)
session_repo.save(session1)
session2 = Session("Spin class", "Group Spin class", "15:00", "Monday", 15)
session_repo.save(session2)
session3 = Session("Weights", "Group weight session", "12:00", "Thursday", 10)
session_repo.save(session3)

members = [("Cathal Wilson", True), ("Derek Bracken", False),
           ("Sean Hollywood", False)]

for member in members:
    new_member = Member(member[0], member[1])
    member_repo.save(new_member)

pdb.set_trace()
