from MySQL import ConnectMySQL

DB = ConnectMySQL.DB()

cursor = DB.con()

sql = '''
Delete from employee 
'''
try:
    results = cursor.execute(sql)
    DB.db.commit()
except:
    DB.db.rollback()
finally:
    DB.close()