import sqlite3
import uuid 

def login(username, password):
    con = sqlite3.connect("storage.db")
    cur = con.cursor()
    check_user = cur.execute("SELECT * FROM admin where username=? AND password=?", (username, password,)).fetchall()

    print(type(check_user))
    print(check_user)

    if(check_user):
        print("ok")
        token = uuid.uuid4().hex
        print(type(token))
        cur.execute("INSERT INTO accesstokens(access_token) VALUES (?)", [(token)])
        print(cur.execute("SELECT * FROM accesstokens").fetchall())
        con.commit()
        con.close()
        return token
    else:
        con.commit()
        con.close()
        user = None
        return user
    
def authenticate_token(token):
    con = sqlite3.connect("storage.db")
    cur = con.cursor()
    check_token = cur.execute("SELECT * FROM accesstokens where access_token=?", (token, )).fetchall()
    print(check_token)
    if(check_token):
        return True
    else:
        return False
    
def authenticate_company(company_api_key):
    con = sqlite3.connect("storage.db")
    cur = con.cursor()
    check_token = cur.execute("SELECT * FROM company where company_api_key=?", (company_api_key, )).fetchall()
    print(check_token)
    if(check_token):
        return True
    else:
        return False
    
def authenticate_sensor(sensor_api_key):
    con = sqlite3.connect("storage.db")
    cur = con.cursor()
    check_token = cur.execute("SELECT * FROM sensor where sensor_api_key=?", (sensor_api_key, )).fetchall()
    print(check_token)
    if(check_token):
        return True
    else:
        return False