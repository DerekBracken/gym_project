class Booking:

    def __init__(self, session, member, id=None):
        self.session = session
        self.member = member
        self.id = id