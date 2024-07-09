from flask import Flask, jsonify, request
import sqlite3
import auth
app = Flask(__name__)

@app.route("/")
def hello_world():
	return "Hello, World! LOL"

@app.route("/login", methods=["POST"])
def login():
	login_data = request.get_json()
	username = login_data["username"]
	password = login_data["password"]

	result = auth.login(username, password)
	if result != None:
		return jsonify(result)
	else:
		return "Record not found", 400
	


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000)
