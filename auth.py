import sqlite3


def login(username, password):
    con = sqlite3.connect("storage.db")
    cur = con.cursor()
    count = cur.execute("SELECT count(*) FROM admin where username=?", (username,)).fetchone()
    print(count)
    count_value = count[0]
    print(count_value)
    # for c in count:
    #     count_value = c[0]
    user = None
    if(count_value != 0):
        useru = cur.execute("SELECT * FROM admin where username=? AND password=?", (username, password,)).fetchall()
        print("ok")
        # print(password)
        print(useru)
        if(user == None):
            print("none")
        # print(useru[0][2])
        # if(password == useru[0][2]):
        #     print("ok1")
        #     user = useru
        #     return user
    return user