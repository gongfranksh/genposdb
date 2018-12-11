# -*- coding: utf-8 -*-
import pymssql
import sqlite3
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

class GetBranch(object):

    def __init__(self):
        self.js_host = "192.168.72.5"
        self.js_user = "syread"
        self.js_pwd = "buynow"
        self.js_db = "headquarters"

    def __GetConnect_mssql(self):
        if not self.js_db:
            raise (NameError, "没有设置数据库信息")
        # self.conn = pymssql.connect(host=self.host, user=self.user, password=self.pwd, database=self.db, charset="utf8")
        self.conn_js = pymssql.connect(host=self.js_host, user=self.js_user, password=self.js_pwd, database=self.js_db, charset="utf8")
        cur = self.conn_js.cursor()
        if not cur:
            raise (NameError, "连接数据库失败")
        else:
            return cur

    def __MsSql_ExecQuery(self, sql):
        cur = self.__GetConnect_mssql()
        cur.execute(sql)
        resList = cur.fetchall()
        return resList

    def get_active_branch(self):
        sql = """
        SELECT braid,brasname FROM branch WHERE BraType='0' AND isopen='1';
        """
        res = self.__MsSql_ExecQuery(sql)
        return res

