from MySQL import ConnectMySQL

DB = ConnectMySQL.DB()

cursor = DB.con()

sql = '''
DROP TABLE IF EXISTS EMPLOYEE;
CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,
         SEX CHAR(1),
         INCOME FLOAT )
'''
result = cursor.execute(sql)
print(result)
DB.close()
