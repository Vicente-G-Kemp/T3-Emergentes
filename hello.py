from flask import Flask, jsonify, request
import sqlite3
import auth, company
app = Flask(__name__)

@app.route("/")
def hello_world():
	return "Hello, World! LOL"

@app.route("/api/v1/login", methods=["POST"])
def login():
	login_data = request.get_json()
	username = login_data["username"]
	password = login_data["password"]

	result = auth.login(username, password)
	if result != None:
		return jsonify(result)
	else:
		return "Record not found", 400
	
@app.route("/api/v1/create_company", methods=["POST"])
def create_company():
	company_data = request.get_json()
	auth_token = request.headers.get('auth-token')
	auth_status = auth.authenticate_token(auth_token)
	if(auth_status):
		company_name = company_data["company_name"]
		company_status = company.create_company(company_name)
		if(company_status):
			return "Status", 201
		else:
			return "Company already exists", 400
	else:
		return "Bad Token", 400

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000)
