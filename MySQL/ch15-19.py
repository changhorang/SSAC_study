import pymysql

conn = pymysql.connect(host = '127.0.0.1', user = 'test1', password = '1q2w3e4r!!',
                        db = 'hanbitDB', charset = 'utf8')
cur = conn.cursor()

cur.execute("select * from userTable")

print("사용자 ID/ 사용자 이름 / 이메일 / 출생년도")
print("-"*40)

while(True):
    row = cur.fetchone()
    if row == None:
        break
    print("{}\t{}\t{}\t{}".format(row[0], row[1], row[2], row[3]))

conn.close()