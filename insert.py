import sqlite3

conn = sqlite3.connect('test.db')
print('successfully connected')

conn.execute("INSERT INTO TEACHERS VALUES(1,'James','kariuki',45,56000.00)")
conn.execute("INSERT INTO TEACHERS VALUES(2,'Job','Kinyua',20,77000.00)")
conn.execute("INSERT INTO TEACHERS VALUES(3,'Mike','Ross',22,50000.00)")
conn.execute("INSERT INTO TEACHERS VALUES(4,'Rose','Wangeshi',30,46000.00)")
conn.execute("INSERT INTO TEACHERS VALUES(5,'Oscar','kariuki',45,40000.00)")
conn.execute("INSERT INTO TEACHERS VALUES(6,'Wayne','karago',34,36000.00)")

conn.commit()
print("successfully inserted records")
conn.close()