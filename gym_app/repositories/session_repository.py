from db.run_sql import run_sql

from models.member import Member
from models.session import Session


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
        session = Session(result['name'], result['description'], result['time'], result['day'], result['capacity'])
    return session

def select_all():
    pass