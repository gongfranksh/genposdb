# -*- coding: utf-8 -*-
import pymssql
import sqlite3
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

class JsEntity(object):

    def __CONNECT_INFO(self):
        self.sqllite_db='jsPos'+self.branch_code+'.db'
        self.js_host = "192.168.72.5"
        self.js_user = "syread"
        self.js_pwd = "buynow"
        self.js_db = "headquarters"
        self.__Connect_sqllite()

    def __init__(self, table,branchcode):
        self.remote_table = table
        self.local_table = table
        self.branch_code =branchcode
        self.__CONNECT_INFO()

    def init_table_diff(self, remotetable,localtable,branchcode):
        self.local_table = localtable
        self.remote_table = remotetable
        self.branch_code =branchcode
        self.__CONNECT_INFO()

    def init_by_branch(self, table,branchcode):
        self.remote_table = table
        self.local_table = table
        self.branch_code =branchcode
        self.__CONNECT_INFO()

    def init_table_diff_by_branch(self, remotetable,localtable,branchcode):
        self.local_table = localtable
        self.remote_table = remotetable
        self.branch_code = branchcode
        self.__CONNECT_INFO()

    def __IsNoneRow(self,row):
            if row[0] is None:
                return 0
            else:
                return row[0]

    def IsNone(self,row):
            if row is None:
                return 0
            else:
                return row

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


    def __Connect_sqllite(self):
        self.sqllite_conn = sqlite3.connect(self.sqllite_db)

    def __sqllite_exesql(self,sql):
        c =  self.sqllite_conn.cursor()
        cursor = c.execute(sql)
        return  cursor

    def __sqllite_exec_sql_no_result(self, sql):
        try:
            c = self.sqllite_conn.cursor()
            c.execute(sql)
            self.sqllite_conn.commit()
        except BaseException as e:
            print('ValueError:', e)

    def get_local_timestamp(self):
        sql = """
        SELECT max(TIMESTAMP)  FROM {0};
        """
        sql=sql.format(self.local_table)

        res = self.__sqllite_exesql(sql)
        for row in res:
            return self.__IsNoneRow(row)


    def get_local_time_stamp(self):
        sql = """
        SELECT max(TIME_STAMP)  FROM {0};
        """
        sql=sql.format(self.local_table)
        print sql
        res = self.__sqllite_exesql(sql)
        for row in res:
            return self.__IsNoneRow(row)


    def truncate_local_table(self):
        sql = """
        delete  FROM {0};
        """
        sql=sql.format(self.local_table)
        self.__sqllite_exec_sql_no_result(sql)

    def get_remote_table_result_all(self):
        sql = """
        SELECT * FROM {0};
        """
        sql=sql.format(self.remote_table)
        res = self.__MsSql_ExecQuery(sql)
        return res

    def get_remote_table_result_by_timestamp(self,timestamp):
        sql = """
        SELECT *,CONVERT (int,timestamp) as stamps FROM {0} where CONVERT (int,timestamp) > {1} order by timestamp ;
        """
        sql=sql.format(self.remote_table,timestamp)
        res = self.__MsSql_ExecQuery(sql)
        return res

    def get_remote_table_result_by_branch_timestamp(self,timestamp):
        sql = """
        SELECT *,CONVERT (int,timestamp) as stamps FROM {0} 
        where CONVERT (int,timestamp) > {1} and braid='{2}' 
        order by timestamp ;
        """
        sql=sql.format(self.remote_table,timestamp,self.branch_code)
        print sql
        res = self.__MsSql_ExecQuery(sql)
        return res

    def get_remote_result_by_sql(self,sql):
        res = self.__MsSql_ExecQuery(sql)
        return res

    def insert_local_table_by_sql(self,sql):
        self.__sqllite_exec_sql_no_result(sql)

    def delete_local_table_by_sql(self,sql):
        self.__sqllite_exec_sql_no_result(sql)

    def print_need_insert(self,current,total):
        print ("%s: [%d/%d]" % (self.local_table,current, total))
