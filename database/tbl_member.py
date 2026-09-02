import sqlite3

# DB 접속 함수 정의
def getconn():
    conn = sqlite3.connect("c:/pydb/member.db")
    return conn

# 테이블 생성 함수 정의
def create_table():
    # 테이블 생성
    conn = getconn()
    cur = conn.cursor()
    sql = """
    CREATE TABLE member(
        m_id CHAR(4) PRIMARY KEY,
        m_passwd CHAR(10) NOT NULL,
        m_name TEXT NOT NULL,
        m_joindate TEXT DEFAULT (datetime('now','localtime'))
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
    sql = "INSERT INTO member(m_id, m_passwd, m_name) VALUES (?, ?, ?)"
    cur.execute(sql, ('1001', 'm123456781', '김도영'))  # 튜플
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
    sql = "SELECT * FROM member WHERE m_id = ?"
    cur.execute(sql, ('1001',))  # 튜플 - 자료 1개(콤머 붙임)
    rs = cur.fetchone()
    print(rs)
    conn.close()

def update_member():
    # 자료 수정
    conn = getconn()
    cur = conn.cursor()
    sql = "UPDATE member SET m_passwd = ? WHERE m_name = ?"
    cur.execute(sql, ('m123456782', '김도영'))
    conn.commit()
    conn.close()

def delete_member():
    # 자료 삭제
    conn = getconn()
    cur = conn.cursor()
    sql = "DELETE FROM member WHERE m_id = ?"
    cur.execute(sql, ('1001', ))
    conn.commit()
    conn.close()

# 함수 호출
# create_table()
insert_member()
#select_one()
#update_member()
#delete_member()
select_member()
