# -*- coding: utf-8 -*-

import pymysql
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class DBManager:
    def __init__(self, sql, database):
        self.sql = sql
        self.database = database

    def connect_db(self):
        config = {
            "host": "***",
            "port": 3306,
            "user": "***",
            "passwd": "***",
            "charset": "utf8",
        }

        conn = pymysql.connect(**config)
        conn.select_db(self.database)
        # cursor = conn.cursor()
        return conn

    def get_data_from_db(self):
        """
        select from
        :return:
        """
        db = self.connect_db()
        cursor = db.cursor()
        data = []
        try:
            cursor.execute(self.sql)
            result = cursor.fetchall()
            for item in result:
                tmp = []
                for i in item:
                    # if isinstance(i, unicode):
                    #     i = i.encode("utf-8")
                    # tmp.append(str(i))
                    tmp.append(i)
                data.append(tmp)
            return data

        except:
            print "Error: unable to fetch data"

        db.close()

    def alter_db_data(self):
        """
        update
        :return:
        """
        db = self.connect_db()
        cursor = db.cursor()
        try:
            cursor.execute(self.sql)
            db.commit()
            # print("update OK")
        except:
            db.rollback()
            # print("Rollback")
        db.close()


# if __name__ == "__main__":
