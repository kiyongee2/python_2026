import sqlite3

def getconn():
    # DB 접속함수 정의
    conn = sqlite3.connect("c:/pydb/will.db")
    return conn

def create_table():
    # 테이블 생성
    conn = getconn()
    cur = conn.cursor()
    sql = """
    CREATE TABLE member(
        memberId CHAR(5) PRIMARY KEY,
        passwd CHAR(10) NOT NULL,
        name TEXT NOT NULL,
        gender CHAR(4),
        age INTEGER
    )
    """
    cur.execute(sql)
    conn.commit()
    print("테이블 생성")
    conn.close()

def insert_member():
    # 자료 삽입
    conn = getconn()
    cur = conn.cursor()
    # 자료 삽입 방법 - 동적 바인딩('?' 기호로 대응)
    sql = "INSERT INTO member VALUES (?, ?, ?, ?, ?)"
    cur.execute(sql, ('10003', 'm123456781', 'RM', '남자', 28))  # 튜플
    conn.commit()
    print("회원 추가")
    conn.close()

def select_member():
    # 자료 검색
    conn = getconn()
    cur = conn.cursor()
    sql = "SELECT * FROM member"
    cur.execute(sql)
    rs = cur.fetchall()
    for i in rs:
        print(i)
    conn.close()

def select_one():
    # 특정한 자료 1개 검색
    conn = getconn()
    cur = conn.cursor()
    sql = "SELECT * FROM member WHERE memberId = ?"
    cur.execute(sql, ('10002',))  # 튜플 - 자료 1개(콤머 붙임)
    rs = cur.fetchone()
    print(rs)
    conn.close()

def update_member():
    # 자료 수정
    conn = getconn()
    cur = conn.cursor()
    sql = "UPDATE member SET age = ? WHERE name = ?"
    cur.execute(sql, (27, '지민'))
    conn.commit()
    conn.close()

def delete_member():
    # 자료 삭제
    conn = getconn()
    cur = conn.cursor()
    sql = "DELETE FROM member WHERE memberId = ?"
    cur.execute(sql, (10003, ))
    conn.commit()
    conn.close()

#create_table()
#insert_member()
#select_one()
#update_member()
#delete_member()
select_member()
