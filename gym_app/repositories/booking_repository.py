from db.run_sql import run_sql

from models.booking import Booking


def save(booking):
    sql = "INSERT INTO bookings (member_id, session_id) VALUES (%s, %s) RETURNING *"
    values = [booking.member.id, booking.session.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    booking.id = id

def select(id):
    pass

def select_all():
    pass

def delete(id):
    pass

def delete_all():
    pass

def update(booking):
    pass
