# -*- coding: utf-8 -*-
from Entity.jsEntity import JsEntity


class Branch(JsEntity):

    def __init__(self):
        JsEntity.__init__(self, "BRANCH")

    def sync_branch(self):
        try:
            self.truncate_local_table()
            needinsert = self.get_remote_table_result_all()
            print needinsert
            self.insert_local_branch(needinsert)
        except BaseException as e:
            print ("Sync_branch error", e)


    def insert_local_branch(self,res):
        print "--insert_local_branch"
        for row in res:
            sql = """
                     INSERT INTO BRANCH(BRAID,BRANAME,BRASNAME,BRATYPE,STATUS)\
                   VALUES('{0}','{1}','{2}','{3}','{4}');
                     """
            sql = sql.format(row[0], row[1], row[2], row[3], row[4])
            print sql
            self.insert_local_table_by_sql(sql)
