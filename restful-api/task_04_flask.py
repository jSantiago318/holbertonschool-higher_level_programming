#!/usr/bin/python3
"""A simple RESTful API built with Flask."""
from flask import Flask, jsonify, request

app = Flask(__name__)

# Users are stored in memory, keyed by username. Starts empty on purpose:
# testing data must not be committed.
users = {}


@app.route("/")
def home():
    """Return a welcome message for the root endpoint."""
    return "Welcome to the Flask API!"


@app.route("/data")
def data():
    """Return the list of all stored usernames."""
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """Return the API status."""
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """Return the full object for a username, or 404 if not found.

    Args:
        username: The username captured from the dynamic route.
    """
    user = users.get(username)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)


@app.route("/add_user", methods=["POST"])
def add_user():
    """Add a new user from a POSTed JSON body.

    Returns:
        A confirmation message with the new user's data (201), or an error
        response for invalid JSON (400), a missing username (400), or a
        duplicate username (409).
    """
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    app.run()
