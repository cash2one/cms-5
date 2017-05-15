# -*- coding: utf-8 -*-

import sys
import json
import pymysql

from datetime import datetime

from django.core.serializers.json import DjangoJSONEncoder


class CbbJSONEncoder(DjangoJSONEncoder):

    def default(self, obj):
        if isinstance(obj, datetime):
            serial = obj.strftime('%Y-%m-%d %H:%M:%S')
            return serial
        return super(CbbJSONEncoder, self).default(obj)

def dictfetchall(cursor):
    """Returns all rows from a cursor as a dict"""
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(0)

    # conn = pymysql.connect(host='172.26.136.192',
    #                        port=8065,
    #                        user='e4sdb',
    #                        passwd='dev2015!!',
    #                        db='e4sdb',
    #                        charset='UTF8')    
    conn = pymysql.connect(host='172.26.136.192',
                           port=8065,
                           user='e4sdb_data',
                           passwd='e4sdb_data',
                           db='e4sdb_data',
                           charset='UTF8')
    cur = conn.cursor()

    print('\n')
    print(sys.argv[1])
    print('\n')
    cur.execute(sys.argv[1])
    # conn.commit()
    
    data_dict = dictfetchall(cur)
    data_json = json.dumps(data_dict,
                           ensure_ascii=False,
                           indent=4,
                           cls=CbbJSONEncoder)
    print(data_json)
    # for r in cur.fetchall():
    #     print(r)
    print('\n')
    cur.close()
    conn.close()


