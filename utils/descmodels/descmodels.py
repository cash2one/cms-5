# -*- coding: utf-8 -*-


import pymysql

if __name__ == '__main__':
    conn = pymysql.connect(host='172.26.136.192',
                           port=8065,
                           user='e4sdb',
                           passwd='dev2015!!',
                           db='e4sdb',
                           charset='UTF8')
    cur = conn.cursor()


    cur.execute("show tables")
    tables = cur.fetchall()
    for table in tables:
        cur.execute("show create table %s" % table[0])
        for r in cur.fetchall():
            print('\n\n')
            for data in r:
                print(data)
    print('\n\n')
    cur.close()
    conn.close()


