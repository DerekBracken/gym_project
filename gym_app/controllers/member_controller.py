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
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    premium = request.form['membership']
    new_member = Member(first_name, last_name, premium)
    member_repo.save(new_member)
    return redirect("/members")

# SHOW
@members_blueprint.route("/members/<id>/show")
def show_member(id):
    member = member_repo.select(id)
    sessions = member_repo.sessions(member)
    return render_template('members/show.html', member=member, sessions=sessions)

# EDIT
@members_blueprint.route("/members/<id>/edit")
def edit_member(id):
    member = member_repo.select(id)
    sessions = member_repo.sessions(member)
    bookings = member_repo.bookings(member)
    return render_template('members/edit.html', member=member, bookings=bookings, sessions=sessions)


# UPDATE
@members_blueprint.route("/members/<id>", methods=["POST"])
def update_member(id):
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    premium = request.form['membership']
    member = Member(first_name, last_name, premium, id)
    member_repo.update(member)
    return redirect("/members")


# DELETE
@members_blueprint.route("/members/<id>/delete", methods=["POST"])
def delete_member(id):
    member_repo.delete(id)
    return redirect("/members")
