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

