from db.run_sql import run_sql

from models.member import Member
from models.session import Session
from models.booking import Booking


def save(member):
    sql = "INSERT INTO members (first_name, last_name, premium) VALUES (%s, %s, %s) RETURNING *"
    values = [member.first_name, member.last_name, member.premium]
    results = run_sql(sql, values)
    id = results[0]['id']
    member.id = id
    return member


def select(id):
    member = None
    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result:
        member = Member(result['first_name'], result['last_name'], result['premium'], result['id'])
    return member


def select_all():
    members = []
    sql = "SELECT * FROM members"
    results = run_sql(sql)
    for row in results:
        member = Member(row['first_name'], row['last_name'], row['premium'], row['id'])
        members.append(member)
    return members


def delete(id):
    sql = "DELETE FROM members WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)


def update(member):
    sql = "UPDATE members SET (first_name, last_name, premium) = (%s, %s, %s) WHERE id = %s"
    values = [member.first_name, member.last_name, member.premium, member.id]
    run_sql(sql, values)


def sessions(member):
    sessions = []

    sql = "SELECT sessions.* FROM sessions INNER JOIN bookings ON bookings.session_id = sessions.id WHERE member_id = %s"
    values = [member.id]
    results = run_sql(sql, values)

    for row in results:
        session = Session(row['name'], row['description'], row['time'], row['day'], row['capacity'], row['id'])
        sessions.append(session)

    return sessions

def bookings(member):
    bookings = []

    sql = "SELECT * FROM bookings WHERE member_id = %s"
    values = [member.id]
    results = run_sql(sql, values)

    for row in results:
        booking = Booking(row['member_id'], row['session_id'], row['id'])
        bookings.append(booking)

    return sessions
