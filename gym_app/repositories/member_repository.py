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
    member = None
    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result:
        member = Member(result['name'], result['premium'], result['id'])
    return member

def select_all():
    pass

def delete(id):
    sql = "DELETE FROM members WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)

