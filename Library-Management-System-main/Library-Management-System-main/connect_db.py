import pymysql


def connect(query):
    con = pymysql.connect(host="localhost", user="root", database="LMS")
    cur = con.cursor()
    cur.execute(query)
    result = cur.fetchall()
    con.commit()
    return result
