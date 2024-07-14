from flask import Flask, jsonify, request
import sqlite3
import auth, company, location, sensor
import re

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
	
@app.route("/api/v1/company", methods=["POST"])
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
	
@app.route("/api/v1/company", methods=["GET"])
def get_company():
	params = request.args.get('key', default = '*', type = str)
	auth_token = request.headers.get('auth-token')
	auth_status = auth.authenticate_token(auth_token)
	if(auth_status):
		company_status = company.get_companies(params)
		if(company_status != None):
			return jsonify(company_status)
		else:
			return "No companies", 400
	else:
		return "Bad Token", 400

@app.route("/api/v1/location", methods=["POST"])
def create_location():
	location_data = request.get_json()
	auth_token = request.headers.get('auth-token')
	auth_status = auth.authenticate_token(auth_token)
	if(auth_status):
		company_api_key = location_data["company_api_key"]
		location_name = location_data["location_name"]
		location_country = location_data["location_country"]
		location_city = location_data["location_city"]
		location_meta = location_data["location_meta"]

		location_status = location.create_location(company_api_key, location_name, location_country, location_city, location_meta)
		if(location_status):
			return "Status", 201
		else:
			return "Invalid company key or Location already exists", 400
	else:
		return "Bad Token", 400

@app.route("/api/v1/location", methods=["GET"])
def get_location():
	ckey = request.args.get('company_key', default = '*', type = str)
	lname = request.args.get('location_name', default = '*', type = str)
	auth_token = request.headers.get('auth-token')
	auth_status = auth.authenticate_token(auth_token)
	if(auth_status):
		location_status = location.get_locations(ckey, lname)
		if(location_status != None):
			return jsonify(location_status)
		else:
			return "No locations", 400
	else:
		return "Bad Token", 400

@app.route("/api/v1/sensor", methods=["POST"])
def create_sensor():
	sensor_data = request.get_json()
	auth_token = request.headers.get('auth-token')
	auth_status = auth.authenticate_token(auth_token)
	if(auth_status):
		company_api_key = sensor_data["company_api_key"]
		location_id = sensor_data["location_id"]
		sensor_name = sensor_data["sensor_name"]
		sensor_category = sensor_data["sensor_category"]
		sensor_meta = sensor_data["sensor_meta"]

		sensor_status = sensor.create_sensor(company_api_key, location_id, sensor_name, sensor_category, sensor_meta)
		if(sensor_status):
			return "Status", 201
		else:
			return "Invalid company key or Sensor already exists", 400
	else:
		return "Bad Token", 400

@app.route("/api/v1/sensor", methods=["GET"])
def get_sensor():
	ckey = request.args.get('company_key', default = '*', type = str)
	sname = request.args.get('sensor_name', default = '*', type = str)
	auth_token = request.headers.get('auth-token')
	auth_status = auth.authenticate_token(auth_token)
	if(auth_status):
		sensor_status = sensor.get_sensors(ckey, sname)
		if(sensor_status != None):
			return jsonify(sensor_status)
		else:
			return "No sensors", 400
	else:
		return "Bad Token", 400


@app.route("/api/v1/sensor_data", methods=["POST"])
def insert_data():
	sensor_records = request.get_json()
	auth_token = request.headers.get('sensor-api-key')
	auth_status = auth.authenticate_sensor(auth_token)
	if(auth_status):
		sensor_api_key = sensor_records["sensor_api_key"]
		json_data = sensor_records["json_data"]

		sensor_status = sensor.insert_data(sensor_api_key, json_data)

		if(sensor_status):
			return "Status", 201
		else:
			return "Invalid category", 400
	else:
		return "Bad Token", 400

@app.route("/api/v1/sensor_data", methods=["GET"])
def get_data():
	from_t = request.args.get('from', default = 0, type = int)
	to_t = request.args.get('to', default = 0, type = int)

	sensor_id = request.args.get('sensor_id')
	sensor_ids = re.split(',',re.split(r'\s*[][]\s*', sensor_id)[1])
	print(sensor_ids)
	auth_token = request.headers.get('company-api-key')
	auth_status = auth.authenticate_company(auth_token)
	if(auth_status):
		sensor_status = sensor.get_sensor_data(auth_token, from_t, to_t, sensor_ids)
		if(sensor_status != None):
			return jsonify(sensor_status)
		else:
			return "No sensors", 400
	else:
		return "Bad Token", 400
	
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000)
