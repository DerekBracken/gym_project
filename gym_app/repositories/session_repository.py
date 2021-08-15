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
