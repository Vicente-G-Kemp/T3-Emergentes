import sqlite3
import uuid 

def create_company(company_name):
    con = sqlite3.connect("storage.db")
    cur = con.cursor()
    check_company = cur.execute("SELECT * FROM company where company_name=?", (company_name, )).fetchall()

    print(type(check_company))
    print(check_company)

    if(not check_company):
        print("ok")
        company_api_key = uuid.uuid4().hex
        print(type(company_api_key))
        birds = [company_name, company_api_key,]
        cur.execute('''INSERT INTO company (company_name, company_api_key) VALUES (?, ?)''', birds)
        # print(cur.execute("SELECT * FROM accesstokens").fetchall())
        con.commit()
        con.close()
        # return "Company succesfully created."
        return True
    else:
        con.commit()
        con.close()
        # status = "Company already exists."
        # return status
        return False
    
def get_companies(company_api_key):
    con = sqlite3.connect("storage.db")
    cur = con.cursor()
    companies = None
    if(company_api_key == '*'):
        companies = cur.execute("SELECT * FROM company").fetchall()
    else:
        companies = cur.execute("SELECT * FROM company where company_api_key=?", (company_api_key, )).fetchone()

    return companies