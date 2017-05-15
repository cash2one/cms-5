#!/usr/bin/env python
# vim: fileencoding=utf-8: noexpandtab

"""
    A very simple wrapper for MySQLdb

    Methods:
        getOne() - get a single row
        getAll() - get all rows
        insert() - insert a row
        insertOrUpdate() - insert a row or update it if it exists
        update() - update rows
        delete() - delete rows
        query()  - run a raw sql query
        leftJoin() - do an inner left join query and get results

    License: GNU GPLv2

    Kailash Nadh, http://nadh.in
    May 2013
"""

import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
from collections import namedtuple
class SimpleMysql:
    conn = None
    cur = None
    conf = None

    def __init__(self, **kwargs):
        self.conf = kwargs
        self.conf["keep_alive"] = kwargs.get("keep_alive", False)
        self.conf["charset"] = kwargs.get("charset", "utf8")
        self.conf["host"] = kwargs.get("host", "localhost")
        self.conf["port"] = kwargs.get("port", 3306)
        self.conf["autocommit"] = kwargs.get("autocommit", False)

        self.connect()

    def connect(self):
        """Connect to the mysql server"""

        try:
            self.conn = MySQLdb.connect(db=self.conf['db'], host=self.conf['host'],
                                        port=self.conf['port'], user=self.conf['user'],
                                        passwd=self.conf['passwd'],
                                        charset=self.conf['charset'])
            self.cur = self.conn.cursor(MySQLdb.cursors.DictCursor)
            self.conn.autocommit(self.conf["autocommit"])
        except:
            print ("MySQL connection failed")
            raise


    def getOne(self, table=None, fields='*', where=None, order=None, limit=(0, 1)):
        """Get a single result

            table = (str) table_name
            fields = (field1, field2 ...) list of fields to select
            where = ("parameterizedstatement", [parameters])
                    eg: ("id=%s and name=%s", [1, "test"])
            order = [field, ASC|DESC]
            limit = [limit1, limit2]
        """

        cur = self._select(table, fields, where, order, limit)
        result = cur.fetchone()

        row = None
        if result:
            Row = namedtuple("Row", [f[0] for f in cur.description])
            row = Row(*result)

        return row


    def getAll(self, table=None, fields='*', where=None, order=None, limit=None):
        """Get all results

            table = (str) table_name
            fields = (field1, field2 ...) list of fields to select
            where = ("parameterizedstatement", [parameters])
                    eg: ("id=%s and name=%s", [1, "test"])
            order = [field, ASC|DESC]
            limit = [limit1, limit2]
        """

        cur = self._select(table, fields, where, order, limit)
        result = cur.fetchall()

        rows = None
        if result:
            Row = namedtuple("Row", [f[0] for f in cur.description])
            rows = [Row(*r) for r in result]

        return rows


    def leftJoin(self, tables=(), fields=(), join_fields=(), where=None, order=None, limit=None):
        """Run an inner left join query

            tables = (table1, table2)
            fields = ([fields from table1], [fields from table 2])  # fields to select
            join_fields = (field1, field2)  # fields to join. field1 belongs to table1 and field2 belongs to table 2
            where = ("parameterizedstatement", [parameters])
                    eg: ("id=%s and name=%s", [1, "test"])
            order = [field, ASC|DESC]
            limit = [limit1, limit2]
        """

        cur = self._select_join(tables, fields, join_fields, where, order, limit)
        result = cur.fetchall()

        rows = None
        if result:
            Row = namedtuple("Row", [f[0] for f in cur.description])
            rows = [Row(*r) for r in result]

        return rows


    def insert(self, table, data):
        """Insert a record"""
        str = ""
        keyslist,valslist,query = self._serialize_insert(data)
        for i in range(len(keyslist)):
            str = str + "%s,"
        str = str[:-1]
#        print (str) 
        sql = "INSERT INTO %s (%s) VALUES(%s)" % (table, query[0], str)
#        sql= "INSERT INTO test_base_car_series (AKQC_GRADE,CAR_PROPERTY,CAR_LEVEL,ORDER_NO,YCW_GRADE,CAR_SERIES_EN,OFFICIAL_CAR_LEVEL,STRUCTURE,QCZJ_GRADE,WAP_THUMBNAIL,IS_ENABLE,ENERGY_CATEGORY,IS_TESTDRIVE,CREATOR,START_GUIDEPRICE,BRIEF_INTRODUTION,UPDATED_DATE,MDM_CAR_SERIES_ID,SALES,MODIFIER,CREATED_DATE,IS_SHOW,CAR_BRAND_ID,ID,CAR_SERIES_ALIAS,END_GUIDEPRICE,TPYQC_GRADE,CAR_SERIES_CN,PC_THUMBNAIL,MDM_CAR_SERIES_CODE) VALUES (null,'1','2','0',null,null,'2',null,null,null,'1',null,null,'admin','0','xx','2016-03-01 19:48:32','N000272853',null,'admin','2016-03-01 19:32',null,'2','500214','xssx','0',null,'xs','http://img.chebaba.com/a9783430-266e-45cb-97ed-c11e4bec9fad.jpg','A36')"
#        print (sql,'sssssssss')
 

        return self.query(sql,valslist).rowcount


    def update(self, table, data,id):
        """Insert a record"""
        keylist,valuelist,insert = self._serialize_insert(data)
        query = self._serialize_update(keylist)
        sql = "UPDATE %s SET %s" % (table, query)
   
        sql += " WHERE ID = %s" % id
        return self.query(sql,valuelist).rowcount
      


    def insertOrUpdate(self, table, data):
        insert_data = data.copy()
        keylist,valuelist,insert = self._serialize_insert(insert_data)
        vls = ",".join(valuelist)
        str = ''
        str2 = ''
        for i in range(len(keylist)):
            str = str + "%s,"
            str2 = str2 + (keylist[i]+'=%s,' )
        str = str[:-1]
        str2 = str2[:-1]
        sql = "INSERT INTO %s (%s) VALUES(%s) ON DUPLICATE KEY UPDATE %s" % (table, insert[0], str, str2)
        newstr = vls +',' + vls
        needlist = newstr.split(',')
        return self.query(sql,needlist).rowcount
		
		

    def delete(self, table, where = None):
        """Delete rows based on a where condition"""

        sql = "DELETE FROM %s" % table

        if where and len(where) > 0:
            sql += " WHERE %s" % where[0]

        return self.query(sql, where[1] if where and len(where) > 1 else None).rowcount


    def query(self, sql, params = None):
        """Run a raw query"""

        # check if connection is alive. if not, reconnect
        try:
#            self.cur.execute(sql, params)
            # sql= "INSERT INTO test_base_car_series (AKQC_GRADE,CAR_PROPERTY,CAR_LEVEL,ORDER_NO,YCW_GRADE,CAR_SERIES_EN,OFFICIAL_CAR_LEVEL,STRUCTURE,QCZJ_GRADE,WAP_THUMBNAIL,IS_ENABLE,ENERGY_CATEGORY,IS_TESTDRIVE,CREATOR,START_GUIDEPRICE,BRIEF_INTRODUTION,UPDATED_DATE,MDM_CAR_SERIES_ID,SALES,MODIFIER,CREATED_DATE,IS_SHOW,CAR_BRAND_ID,ID,CAR_SERIES_ALIAS,END_GUIDEPRICE,TPYQC_GRADE,CAR_SERIES_CN,PC_THUMBNAIL,MDM_CAR_SERIES_CODE) VALUES (null,'1','2','0',null,null,'2',null,null,null,'1',null,null,'admin','0','xx','2016-03-01 19:48:32','N000272853',null,'admin','2016-03-01 19:32',null,'2','500214','xssx','0',null,'xs','http://img.chebaba.com/a9783430-266e-45cb-97ed-c11e4bec9fad.jpg','A36')"
            self.cur.execute(sql,params)
        except MySQLdb.OperationalError as e:
            # mysql timed out. reconnect and retry once
            if e[0] == 2006:
                self.connect()
                self.cur.execute(sql, params)
            else:
                raise
        except:
            print("Query failed")
            raise

        return self.cur

    def commit(self):
        """Commit a transaction (transactional engines like InnoDB require this)"""
        return self.conn.commit()

    def is_open(self):
        """Check if the connection is open"""
        return self.conn.open

    def end(self):
        """Kill the connection"""
        self.cur.close()
        self.conn.close()

    # ===

    def _serialize_insert(self, data):
        """Format insert dict values into strings"""

        keyslist = []
        valslist = []
        templist = [] 
        b = []
        c = []

        for k in data:
            keyslist.append(str(k))  	
            valslist.append(str(data[k]))
        templist = valslist.copy()
        keys = ''
        vals = ''
        for j in range(len(valslist)):
            if valslist[j] == 'None':
                templist[j] = 'null'
                valslist[j] = 'null'
            else:
                templist[j] = '"%s"'%(valslist[j])
        for j in range(len(valslist)):
            if valslist[j] == 'null':
                b.append(j) 
        c=b.copy()			
        for i in range(len(b)):
            if i ==0:
                c[i] = b [i]
            if i >0:
                c[i] = b [i] -i					
        for i in range(len(b)):
            valslist.pop(c[i])
            keyslist.pop(c[i])			
        keys =','.join(keyslist)
        return keyslist,valslist,[keys, vals]
		
    def _serialize_update(self, keylist):
        """Format update dict values into string"""
        str = ''
        for i in range(len(keylist)):
            str = str + keylist[i] + '=%s,'
        str = str[:-1]
        return str
		
		
    # def _serialize_update(self,keylist,valuelist):
        # """Format update dict values into string"""
        # str = ''
        # for i in range(len(keylist)):
            # print (keylist[i],valuelist[i])
            # str = str + keylist[i] + '=' + valuelist[i] + ',' 
        # str = str[:-1]
        # print (str,'ssssssssssssssssss')
        # return str 

		
    def IsExistsinSQL(self,table,data):		
        keyslist,valslist,query = self._serialize_insert(data)			
        sql = "SELECT * FROM %s where ID = %s"%(table,data['ID'])
        p = self.cur.execute(sql)
        return p,data['ID']
		

		
		

    # def _select(self, table=None, fields=(), where=None, order=None, limit=None):
        # """Run a select query"""

        # sql = "SELECT %s FROM `%s`" % (",".join(fields), table)

        # # where conditions
        # if where and len(where) > 0:
            # sql += " WHERE %s" % where[0]

        # # order
        # if order:
            # sql += " ORDER BY %s" % order[0]

            # if len(order) > 1:
                # sql+= " %s" % order[1]

        # # limit
        # if limit:
            # sql += " LIMIT %s" % limit[0]

            # if len(limit) > 1:
                # sql+= ", %s" % limit[1]

        # return self.query(sql, where[1] if where and len(where) > 1 else None)

    def _select_join(self, tables=(), fields=(), join_fields=(), where=None, order=None, limit=None):
        """Run an inner left join query"""

        fields = [tables[0] + "." + f for f in fields[0]] + \
                 [tables[1] + "." + f for f in fields[1]]

        sql = "SELECT %s FROM %s LEFT JOIN %s ON (%s = %s)" % \
                (     ",".join(fields),
                    tables[0],
                    tables[1],
                    tables[0] + "." + join_fields[0], \
                    tables[1] + "." + join_fields[1]
                )

        # where conditions
        if where and len(where) > 0:
            sql += " WHERE %s" % where[0]

        # order
        if order:
            sql += " ORDER BY %s" % order[0]

            if len(order) > 1:
                sql+= " " + order[1]

        # limit
        if limit:
            sql += " LIMIT %s" % limit[0]

            if len(limit) > 1:
                sql+= ", %s" % limit[1]

        return self.query(sql, where[1] if where and len(where) > 1 else None)

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.end()
