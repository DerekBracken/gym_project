from flask import Blueprint, Flask, redirect, render_template, request

from models.booking import Booking
import repositories.booking_repository as booking_repo
import repositories.member_repository as member_repo
import repositories.session_repository as session_repo

bookings_blueprint = Blueprint("bookings", __name__)

# INDEX
@bookings_blueprint.route("/bookings")
def bookings():
    bookings = booking_repo.select_all()
    return render_template("bookings/index.html", bookings=bookings)


# NEW
@bookings_blueprint.route("/bookings/new")
def new_booking():
    members = member_repo.select_all()
    sessions = session_repo.select_all()
    return render_template("bookings/new.html", members=members, sessions=sessions)


# CREATE
@bookings_blueprint.route("/bookings", methods=["POST"])
def create_booking():
    member_id = request.form["member_id"]
    session_id = request.form["session_id"]
    member = member_repo.select(member_id)
    session = session_repo.select(session_id)
    new_booking = Booking(member, session)
    booking_repo.save(new_booking)
    return redirect("/bookings")


# EDIT
@bookings_blueprint.route("/bookings/<id>/edit")
def edit_booking(id):
    booking = booking_repo.select(id)
    members = member_repo.select_all()
    sessions = session_repo.select_all()
    return render_template('bookings/edit.html', booking=booking, members=members, sessions=sessions)


# UPDATE
@bookings_blueprint.route("/bookings/<id>", methods=["POST"])
def update_booking(id):
    member_id = request.form["member_id"]
    session_id = request.form["session_id"]
    member = member_repo.select(member_id)
    session = session_repo.select(session_id)
    booking = Booking(member, session, id)
    booking_repo.update(booking)
    return redirect("/bookings")

