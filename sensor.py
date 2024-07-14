import sqlite3
import uuid 
import datetime

def create_sensor(company_api_key, location_id, sensor_name, sensor_category, sensor_meta):
    con = sqlite3.connect("storage.db")
    cur = con.cursor()
    check_company = cur.execute("SELECT * FROM company where company_api_key=?", (company_api_key, )).fetchall()

    print(type(check_company))
    print(check_company)

    if(check_company):
        print("ok")
        check_location = cur.execute("SELECT * FROM location where id=?", (location_id,)).fetchone()
        print(check_location)
        if(check_location):
            print("OKK")
            print(check_company[0][0])
            check_sensor = cur.execute("SELECT * FROM sensor where sensor_name=?", (sensor_name,)).fetchone()
            if(not check_sensor):
                sensor_api_key = uuid.uuid4().hex
                print(type(sensor_api_key))
                sensor_data = [location_id, sensor_name, sensor_category, sensor_meta, sensor_api_key, ]
                cur.execute('''INSERT INTO sensor (location_id, sensor_name, sensor_category, sensor_meta, sensor_api_key) VALUES (?, ?, ?, ?, ?)''', sensor_data)
                con.commit()
                con.close()
                return True
            else:
                con.commit()
                con.close()
                return False
        else:
            return False
    else:
        con.commit()
        con.close()
        return False
    

def get_sensors(company_api_key, sensor_name):
    con = sqlite3.connect("storage.db")
    cur = con.cursor()
    locations = None
    if(company_api_key != '*'):
        c_id = cur.execute("SELECT * FROM company where company_api_key=?", (company_api_key, )).fetchone()[0]
        if(sensor_name == '*'):
            locations = cur.execute("SELECT location_id, sensor.id, sensor_name, sensor_category, sensor_meta, sensor_api_key FROM location JOIN sensor ON location.company_id =?", (c_id, )).fetchall()
        else:
            locations = cur.execute("SELECT location_id, sensor.id, sensor_name, sensor_category, sensor_meta, sensor_api_key FROM location JOIN sensor ON location.company_id =? WHERE sensor.sensor_name=?", (c_id, sensor_name, )).fetchone()
    return locations

def insert_data(sensor_api_key, json_data: list):
    con = sqlite3.connect("storage.db")
    cur = con.cursor()
    s_id = cur.execute("SELECT * FROM sensor where sensor_api_key=?", (sensor_api_key, )).fetchone()[0]

    if(json_data[0]["category"] == 0):
        print("ok")
        cur.execute("INSERT INTO sensordata0(sensor_id, data0, data1, timestamp) VALUES (?, ?, ?, ?)", (s_id, json_data[1]["data0"], json_data[1]["data1"], json_data[1]["timestamp"],)).fetchone()
        con.commit()
        con.close()
        return True
    if(json_data[0]["category"] == 1):
        cur.execute("INSERT INTO sensordata1(sensor_id, data0, data1, timestamp) VALUES (?, ?, ?, ?)", (s_id, json_data[1]["data0"], json_data[1]["data1"], json_data[1]["timestamp"],)).fetchone()
        con.commit()
        con.close()
        return True
    if(json_data[0]["category"] == 2):
        cur.execute("INSERT INTO sensordata2(sensor_id, data0, data1, data2, timestamp) VALUES (?, ?, ?, ?, ?)", (s_id, json_data[1]["data0"], json_data[1]["data1"], json_data[1]["data2"], json_data[1]["timestamp"],)).fetchone()
        con.commit()
        con.close()
        return True

    return False


def get_sensor_data(company_api_key, from_t: int, to_t: int, sensor_ids: list):
    con = sqlite3.connect("storage.db")
    cur = con.cursor()
    data = None
    if(company_api_key != '*'):
        c_id = cur.execute("SELECT * FROM company where company_api_key=?", (company_api_key, )).fetchone()[0]
        sensor_ids.insert(0, c_id)
        print(sensor_ids)

        time_from = datetime.datetime.fromtimestamp(from_t).strftime('%Y-%m-%d %H:%M:%S')
        time_to = datetime.datetime.fromtimestamp(to_t).strftime('%Y-%m-%d %H:%M:%S')
        print(time_from)
        print(time_to)
        sensor_ids.insert(len(sensor_ids), time_from)
        sensor_ids.insert(len(sensor_ids), time_to)
        sensor_ids.insert(len(sensor_ids), time_from)
        sensor_ids.insert(len(sensor_ids), time_to)
        sensor_ids.insert(len(sensor_ids), time_from)
        sensor_ids.insert(len(sensor_ids), time_to) #sry lmao no voy a buscar una alternativa
        
        data = cur.execute("SELECT * FROM sensor JOIN sensordata0 ON sensor.id = sensordata0.sensor_id JOIN sensordata1 ON sensor.id = sensordata1.sensor_id JOIN sensordata2 ON sensor.id = sensordata2.sensor_id JOIN location ON sensor.location_id = location.id JOIN company ON location.company_id = company.id WHERE company.id=? AND sensor.id IN ({seq}) AND sensordata0.timestamp BETWEEN (?) AND (?) AND sensordata1.timestamp BETWEEN (?) AND (?) AND sensordata2.timestamp BETWEEN (?) AND (?)".format(seq=','.join(['?']*(len(sensor_ids)-7))), (sensor_ids)).fetchall()
    return data