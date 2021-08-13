import pdb
from models.member import Member
from models.session import Session
from models.booking import Booking

import repositories.member_repository as member_repo
import repositories.session_repository as session_repo
import repositories.booking_repository as booking_repo

members = [("Cathal Wilson", True), ("Derek Bracken", False), ("Sean Hollywood", False)]

member_repo.delete_all()


for member in members:
    new_member = Member(member[0], member[1])
    member_repo.save(new_member)

pdb.set_trace()