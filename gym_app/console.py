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

member1 = Member("Cathal", "Wilson", True)
member_repo.save(member1)
member2 = Member("Derek", "Bracken", False)
member_repo.save(member2)
member3 = Member("Sean", "Hollywood", False)
member_repo.save(member3)

booking1 = Booking(member1, session1)
booking_repo.save(booking1)
booking2 = Booking(member2, session2)
booking_repo.save(booking2)
booking3 = Booking(member3, session3)
booking_repo.save(booking3)

pdb.set_trace()
