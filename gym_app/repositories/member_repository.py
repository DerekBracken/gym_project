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
    