import sqlite3

# db 연결
conn = sqlite3.connect("c:/pydb/mydb.db")
print(conn, "데이터베이스 연결 성공!!")

# 자료 검색 - fetchall()
def select():
  with sqlite3.connect("c:/pydb/mydb.db") as conn:
    cursor = conn.cursor()
    sql = "SELECT * FROM emp"
    cursor.execute(sql)
    rows = cursor.fetchall()
    # print(rows)
    for row in rows:
      print(row)
      
# 자료 삽입
def insert():
  with sqlite3.connect("c:/pydb/mydb.db") as conn:
    cursor = conn.cursor()
    sql = "INSERT INTO emp(id, name, salary) values('e301', '김대리', 4000000)"
    cursor.execute(sql)
    conn.commit()
    print("사원 추가 완료!")
    
# 자료 1건 검색 - fetchone()
def select_one():
  with sqlite3.connect("c:/pydb/mydb.db") as conn:
    cursor = conn.cursor()
    sql = "SELECT * FROM emp WHERE name = '김대리'"
    cursor.execute(sql)
    row = cursor.fetchone()
    print(row)

conn.close() # 접속 끊기

# 함수 호출
# insert()
# select()
select_one()