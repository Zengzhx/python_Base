import pymysql


#封装数据连接
class DB:
    db = None

      def con(self):
        return self.getdb('localhost', 'root', 'root', 'test', 3306, 'utf8')

    def getdb(self, url, username, password, database,prot,charset):
        self.db = pymysql.Connect(host=url,
                             user=username,
                             password=password,
                             db=database,
                             port=prot,
                             charset=charset)
        cursor = self.db.cursor()
        return cursor

    def close(self):
        self.db.close()

