#from libs.db.oracle_dbconn import getconn

import cx_Oracle
import os

def getconn():
    # LOCATION = r'c:/instantclient_19_12'
    # os.environ["PATH"] = LOCATION + ":" + os.environ["PATH"] # 환경 설정
    conn = cx_Oracle.connect("system", "12345", "localhost:1522/xe")
    return conn

def select_data():
    conn = getconn()
    cur = conn.cursor()
    sql = "SELECT * FROM person"
    cur.execute(sql)
    rs = cur.fetchall()
    for i in rs:
        print(i)

    conn.close()

def insert_data():
    conn = getconn()
    cur = conn.cursor()
    sql = "INSERT INTO person VALUES ('park', 'p1234567', '박대양', 45)"
    cur.execute(sql)
    conn.commit()
    conn.close()

def select_one():
    conn = getconn()
    cur = conn.cursor()
    sql = "SELECT * FROM person WHERE userId = 'park'"
    #sql = "SELECT * FROM person WHERE userId = ?"
    cur.execute(sql)
    rs = cur.fetchone()
    print(rs)
    conn.close()

if __name__ == "__main__":
    #insert_data()
    #select_one()
    select_data()


