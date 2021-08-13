from db.run_sql import run_sql

from models.member import Member
from models.session import Session

def save(member):
    sql = "INSERT INTO members (name, premium) VALUES (%s, %s) RETURNING *"
    values = [member.name, member.premium]
    results = run_sql(sql, values)
    id = results[0]['id']
    member.id = id
    return member


def select(id):
    pass

def select_all():
    pass

def delete(id):
    sql = "DELETE FROM members WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)

