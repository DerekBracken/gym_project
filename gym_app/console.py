import pdb
from models.member import Member
from models.session import Session
from models.booking import Booking

import repositories.member_repository as member_repo
import repositories.session_repository as session_repo
import repositories.booking_repository as booking_repo


member_repo.delete_all()
session_repo.delete_all()

session1 = Session("HIIT", "HIIT or high-intensity interval training is a really time efficient workout in which you give 100% effort for short periods of time, followed by short recovery periods.", "11:00", "Tuesday", 20)
session_repo.save(session1)
session2 = Session("Abs Class", "A gym based abs class is a great way of building core strength and core stability.", "15:00", "Monday", 15)
session_repo.save(session2)
session3 = Session("Indoor Cycling", "Indoor cycling or Spinning as it is commonly known as is a group cycling class to music. ", "12:00", "Thursday", 10)
session_repo.save(session3)
session4 = Session("Boxing ", "A gym-based boxing workout will include pad work, bag work and some boxing-specific strength and conditioning routines.", "12:00", "Thursday", 10)
session_repo.save(session4)
session5 = Session("Vini Yoga", "In essence, yoga involves a series of poses and stretches which help you to gain strength and improve flexibility.", "12:00", "Thursday", 10)
session_repo.save(session5)


member1 = Member("Cathal", "Wilson", True)
member_repo.save(member1)
member2 = Member("John", "Smith", False)
member_repo.save(member2)
member3 = Member("Sean", "Hughes", False)
member_repo.save(member3)
member4 = Member("Mary", "Nolan", True)
member_repo.save(member4)
member5 = Member("Kathryn", "Greenslade", False)
member_repo.save(member5)


booking1 = Booking(member1, session1)
booking_repo.save(booking1)
booking2 = Booking(member2, session2)
booking_repo.save(booking2)
booking3 = Booking(member3, session3)
booking_repo.save(booking3)
booking4 = Booking(member4, session4)
booking_repo.save(booking4)
booking5 = Booking(member5, session5)
booking_repo.save(booking5)

pdb.set_trace()
