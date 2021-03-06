from db.run_sql import run_sql

from models.member import Member
from models.session import Session
from models.booking import Booking
import repositories.member_repository as member_repo
import repositories.session_repository as session_repo


def save(session):
    sql = "INSERT INTO sessions (name, description, time, day, capacity) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [session.name, session.description, session.time, session.day, session.capacity]
    results = run_sql(sql, values)
    id = results[0]['id']
    session.id = id
    return session

def select(id):
    session = None
    sql = "SELECT * FROM sessions WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result:
        session = Session(result['name'], result['description'], result['time'], result['day'], result['capacity'], result['id'])
    return session

def select_all():
    sessions = []
    sql = "SELECT * FROM sessions"
    results = run_sql(sql)
    for row in results:
        session = Session(row['name'], row['description'], row['time'], row['day'], row['capacity'], row['id'])
        sessions.append(session)
    return sessions

def delete(id):
    sql = "DELETE FROM sessions WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM sessions"
    run_sql(sql)

def update(session):
    sql = "UPDATE sessions SET (name, description, time, day, capacity) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [session.name, session.description, session.time, session.day, session.capacity, session.id]
    run_sql(sql, values)

def members(session):
    members = []

    sql = "SELECT members.* FROM members INNER JOIN bookings ON bookings.member_id = members.id WHERE session_id = %s"
    values = [session.id]
    results = run_sql(sql, values)

    for row in results:
        member = Member(row['first_name'], row['last_name'], row['premium'], row['id'])
        members.append(member)

    return members

def bookings(session):
    bookings = []

    sql = "SELECT * FROM bookings WHERE session_id = %s"
    values = [session.id]
    results = run_sql(sql, values)

    for row in results:
        member = member_repo.select(row['member_id'])
        booking = Booking(member, session, row['id'])
        bookings.append(booking)

    return bookings
