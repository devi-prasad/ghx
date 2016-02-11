import pypyodbc

class MSSQLghx(object):
    """docstring for ClassName"""
    def __init__(self, dsn):
	    self._dsn = dsn
	    self._con = None
	    self._cur = None
	    self._last = 0

    def connect(self):
        print("DSN = " + self._dsn)
        self._con = pypyodbc.connect('DSN=' + self._dsn)
        if self._con is not None:
            print("success")
        else:
            print("not sucess")
        self._cur = self._con.cursor()
        return self._cur

    def insert(self, tablename, cid):
        self._cur.execute('insert into {}(repoID) values({});'.format(tablename, cid))
        self._cur.commit()
        
    def update(self, tablename, field, key, value):
        try:
	        self._cur.execute('update {} set {} = {} where repoID = {};'.format(tablename, key, value, field))
	        self._cur.commit()
        except:
            raise Exception

    def close(self):
        self._con.close()

    def lastid(self, tablename):
        self._cur.execute("select count(*) from " + tablename)
        self._last = list(self._cur)[0][0]
        return self._last	


def testmssql():
			
		myConn = pypyodbc.connect('DSN=GHXRepodb')
		if myConn is not None:
			print("success")
		else:
			print("not sucess")

		cur=myConn.cursor()

		cur.execute(''' insert into test values('pks','sois')''')
		cur.execute('''select * from test;''')

		for d in cur.description:
			print(d[0], end=" ")

		print('')

		for row in cur.fetchall():
			for field in row:
				print(field, end=" ")
			print('')

		cur.commit()
		myConn.close()


if __name__ == '__main__':
	testmssql()