#from libs.db.dbconn import getconn
import sqlite3

def select_emp():
    # 사원 전체 검색
    conn = sqlite3.connect("c:/pydb/will.db")
    cur = conn.cursor()
    sql = "SELECT * FROM employee ORDER BY salary DESC"
    cur.execute(sql)
    rs = cur.fetchall()   # rs=resultSet의 약자
    for i in rs:
        print(i)
    conn.close()

def select_one():
    # 사원 1명 검색
    conn = sqlite3.connect("c:/pydb/will.db")
    cur = conn.cursor()
    sql = "SELECT * FROM employee WHERE emp_id = 'e1002'"
    cur.execute(sql)  # 튜플은 1개일때 코머를 꼭 붙인다.
    rs = cur.fetchone()
    print(rs)
    conn.close()

def insert_emp():
    # 사원 추가
    conn = sqlite3.connect("c:/pydb/will.db")
    cur = conn.cursor()
    sql = "INSERT INTO employee VALUES ('e1002', '박인비', 31, 20000)"
    cur.execute(sql)
    conn.commit()
    conn.close()

def update_emp():
    # 사원 정보 수정
    conn = sqlite3.connect("c:/pydb/will.db")
    cur = conn.cursor()
    sql = "UPDATE employee SET salary = 30000 WHERE emp_id = 'e1001'"
    #추신수의 급여를 10000에서 30000으로 변경
    cur.execute(sql)
    conn.commit()
    conn.close()

def delete_emp():
    # 사원 정보 삭제
    conn = sqlite3.connect("c:/pydb/will.db")
    cur = conn.cursor()
    # 사원 아이디가 'e102'인 사원 정보를 삭제
    sql = "DELETE FROM employee WHERE emp_id = 'e1002'"
    cur.execute(sql)
    conn.commit()
    conn.close()

if __name__=="__main__":
    #insert_emp()
    #update_emp()
    delete_emp()
    select_emp()
    #select_one()
