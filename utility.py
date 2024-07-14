import sqlite3
import datetime
con = sqlite3.connect("storage.db")

cur = con.cursor()
# cur.execute("DROP TABLE IF EXISTS sensordata0")
# cur.execute("DROP TABLE IF EXISTS sensordata1")
# cur.execute("DROP TABLE IF EXISTS sensordata2")
# cur.execute(
#     "CREATE TABLE admin(id INTEGER PRIMARY KEY, username TEXT NOT NULL, password TEXT NOT NULL)"
#     )
# cur.execute(
#     "CREATE TABLE company(id INTEGER PRIMARY KEY, company_name TEXT NOT NULL, company_api_key TEXT NOT NULL)"
#     )
# cur.execute(
#     "CREATE TABLE location(id INTEGER PRIMARY KEY, company_id INTEGER NOT NULL, location_name TEXT NOT NULL, location_country TEXT NOT NULL, location_city TEXT NOT NULL, location_meta TEXT NOT NULL)"
#     )
# cur.execute(
#     "CREATE TABLE sensor(id INTEGER PRIMARY KEY, location_id INTEGER NOT NULL, sensor_name TEXT NOT NULL, sensor_category TEXT NOT NULL, sensor_meta TEXT NOT NULL, sensor_api_key TEXT NOT NULL)"
#     )
# cur.execute(
#     "CREATE TABLE sensordata0(id INTEGER PRIMARY KEY, sensor_id INTEGER NOT NULL, data0 TEXT, data1 TEXT, timestamp TEXT NOT NULL)"
#     )
# cur.execute(
#     "CREATE TABLE sensordata1(id INTEGER PRIMARY KEY, sensor_id INTEGER NOT NULL, data0 INTEGER, data1 INTEGER, timestamp TEXT NOT NULL)"
#     )
# cur.execute(
#     "CREATE TABLE sensordata2(id INTEGER PRIMARY KEY, sensor_id INTEGER NOT NULL, data0 TEXT, data1 TEXT, data2 INTEGER, timestamp TEXT NOT NULL)"
#     )
# cur.execute(
#     "CREATE TABLE accesstokens(id INTEGER PRIMARY KEY, access_token TEXT NOT NULL)"
#     )

# admin = [('admin1', '12345')]

# cur.executemany('''INSERT INTO admin (username, password) VALUES (?, ?)''', admin)

# res = cur.execute("SELECT * FROM sensordata0")

# print(res.fetchall())

# cur.execute("DELETE FROM location where id = 2")
time = datetime.datetime.fromtimestamp(1347517370).strftime('%Y-%m-%d %H:%M:%S')
print(type(time))

con.commit()
con.close()
