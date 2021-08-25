# MySQL에 저장

# conn = pymysql.connect(host = '127.0.0.1', user = 'Mini_1', password = '1q2w3e4r!!',
#                         db = 'MiniProjectDB', charset = 'utf8')

# cur = conn.cursor()

# cur.execute("CREATE TABLE IF NOT EXISTS userTable (id char(4),\
#             userName char(15), email char(20), birthYear int)")

# cur.execute("INSERT INTO userTable VALUES ('john', 'john bann', 'john@naver.com', 1990)")
# cur.execute("INSERT INTO userTable VALUES ('kim', 'kim chi', 'kim@naver.com', 1992)")
# cur.execute("INSERT INTO userTable VALUES ('lee', 'lee pal', 'lee@naver.com', 1988)")
# cur.execute("INSERT INTO userTable VALUES ('park', 'park su', 'park@naver.com', 1980)")

# conn.commit()
# conn.close()