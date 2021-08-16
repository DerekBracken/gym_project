from flask import Blueprint, Flask, redirect, render_template, request

from models.member import Member
import repositories.member_repository as member_repo

members_blueprint = Blueprint("members", __name__)

# INDEX
@members_blueprint.route("/members")
def members():
    members = member_repo.select_all()
    return render_template("members/index.html", members=members)


# NEW
@members_blueprint.route("/members/new")
def new_member():
    return render_template("members/new.html", title='Add Member')



# CREATE
@members_blueprint.route("/members", methods=["POST"])
def create_member():
    name = request.form["name"]
    premium = request.form['membership']
    new_member = Member(name, premium)
    member_repo.save(new_member)
    return redirect("/members")


# EDIT
@members_blueprint.route("/members/<id>/edit")
def edit_member(id):
    member = member_repo.select(id)
    return render_template('members/edit.html', member=member)

# UPDATE
@members_blueprint.route("/members/<id>", methods=["POST"])
def update_member(id):
    name = request.form["name"]
    premium = request.form['membership']
    member = Member(name, premium, id)
    member_repo.update(member)
    return redirect("/members")

# DELETE
@members_blueprint.route("/members/<id>/delete", methods=["POST"])
def delete_member(id):
    member_repo.delete(id)
    return redirect("/members")

