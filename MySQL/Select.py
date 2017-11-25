from MySQL import ConnectMySQL

'''
数据库查询操作
    Python查询Mysql使用 fetchone() 方法获取单条数据, 使用fetchall() 方法获取多条数据。
    fetchone(): 该方法获取下一个查询结果集。结果集是一个对象
    fetchall(): 接收全部的返回结果行.
    rowcount: 这是一个只读属性，并返回执行execute()方法后影响的行数。
'''
db = ConnectMySQL.DB()

cursor = db.con()

sql = '''
select * from EMPLOYEE 
'''

try:
    cursor.execute(sql)

    results = cursor.fetchall()
    index = 1
    for row in results:
        print(row)
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        # 打印结果
        print("ID=%s fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
              (index, fname, lname, age, sex, income))
        index += 1
except:
    print("no data")
finally:
    db.close()