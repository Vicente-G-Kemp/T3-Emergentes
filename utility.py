import sqlite3

con = sqlite3.connect("storage.db")

cur = con.cursor()
# cur.execute("DROP TABLE IF EXISTS admin")
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
#     "CREATE TABLE sensordata(id INTEGER PRIMARY KEY, sensor_id INTEGER)"
#     )
# cur.execute(
#     "CREATE TABLE accesstokens(id INTEGER PRIMARY KEY, access_token TEXT NOT NULL)"
#     )

# admin = [('admin1', '12345')]

# cur.executemany('''INSERT INTO admin (username, password) VALUES (?, ?)''', admin)

res = cur.execute("SELECT * FROM admin")
print(res.fetchall()[0])

con.commit()
con.close()
