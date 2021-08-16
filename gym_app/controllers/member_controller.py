from flask import Blueprint, Flask, redirect, render_template, request

from models.member import Member
import repositories.member_repository as member_repo

members_blueprint = Blueprint("members", __name__)

# INDEX
@members_blueprint.route("/members")
def members():
    members = member_repo.select_all()
    return render_template("members/index.html", members=members)



