from MySQL import  ConnectMySQL

DB = ConnectMySQL.DB()

cursor = DB.con()

sql = '''
INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)
'''

try:
   # 执行sql语句
   index = 1
   while index < 1000:
       result = cursor.execute(sql)
       print(result)
   # 提交到数据库执行
       DB.db.commit()
       index += 1
       print(index)
except:
   # 如果发生错误则回滚
   DB.db.rollback()

DB.close()