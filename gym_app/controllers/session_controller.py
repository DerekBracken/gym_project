from datetime import time
from sys import displayhook
from flask import Blueprint, Flask, redirect, render_template, request

from models.session import Session
import repositories.session_repository as session_repo

sessions_blueprint = Blueprint("sessions", __name__)

# INDEX
@sessions_blueprint.route("/sessions")
def sessions():
    sessions = session_repo.select_all()
    return render_template("sessions/index.html", sessions=sessions)

# NEW
@sessions_blueprint.route("/sessions/new")
def new_session():
    return render_template("sessions/new.html", title='Add Session')


# CREATE
@sessions_blueprint.route("/sessions", methods=["POST"])
def create_session():
    name = request.form["name"]
    description = request.form["description"]
    time = request.form["time"]
    day = request.form["day"]
    capacity = request.form["capacity"]
    new_session = Session(name, description, time, day, capacity)
    session_repo.save(new_session)
    return redirect("/sessions")


# EDIT
@sessions_blueprint.route("/sessions/<id>/edit")
def edit_session(id):
    session = session_repo.select(id)
    return render_template('sessions/edit.html', session=session)


# UPDATE
@sessions_blueprint.route("/sessions/<id>", methods=["POST"])
def update_session(id):
    name = request.form["name"]
    description = request.form["description"]
    time = request.form["time"]
    day = request.form["day"]
    capacity = request.form["capacity"]
    session = Session(name, description, time, day, capacity, id)
    session_repo.update(session)
    return redirect("/sessions")


# DELETE
@sessions_blueprint.route("/sessions/<id>/delete", methods=["POST"])
def delete_session(id):
    session_repo.delete(id)
    return redirect("/sessions")




