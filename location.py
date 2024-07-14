import sqlite3
import uuid 

def create_location(company_api_key, location_name, location_country, location_city, location_meta):
    con = sqlite3.connect("storage.db")
    cur = con.cursor()
    check_company = cur.execute("SELECT * FROM company where company_api_key=?", (company_api_key, )).fetchall()

    print(type(check_company))
    print(check_company)

    if(check_company):
        print("ok")
        check_location = cur.execute("SELECT * FROM location where location_name=? AND company_id=?", (location_name, check_company[0][0],)).fetchall()
        if(not check_location):
            print(check_company[0][0])

            location_data = [check_company[0][0], location_name, location_country, location_city, location_meta, ]
            cur.execute('''INSERT INTO location (company_id, location_name, location_country, location_city, location_meta) VALUES (?, ?, ?, ?, ?)''', location_data)

            con.commit()
            con.close()
            return True
        else:
            return False
    else:
        con.commit()
        con.close()
        return False
    

def get_locations(company_api_key, location_name):
    con = sqlite3.connect("storage.db")
    cur = con.cursor()
    locations = None
    if(company_api_key != '*'):
        c_id = cur.execute("SELECT * FROM company where company_api_key=?", (company_api_key, )).fetchone()[0]
        if(location_name == '*'):
            locations = cur.execute("SELECT * FROM location WHERE company_id=?", (c_id, )).fetchall()
        else:
            locations = cur.execute("SELECT * FROM location WHERE location_name=? AND company_api_key=?", (location_name, company_api_key, )).fetchone()
    return locations