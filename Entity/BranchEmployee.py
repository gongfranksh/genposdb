# -*- coding: utf-8 -*-
from Entity.jsEntity import JsEntity


class BranchEmployee(JsEntity):

    def __init__(self):
        JsEntity.__init__(self, "Branch_Employee")

    def sync_branch_employee(self):
        try:
            branchemployeestamps = self.get_local_timestamp()
            print 'branchemployeestamps==>', branchemployeestamps
            needinsert = self.get_remote_table_result_by_timestamp(branchemployeestamps)
            print needinsert
            self.insert_local_branch_employee(needinsert)
        except BaseException as e:
            print ("Sync_branch error", e)

    def insert_local_branch_employee(self,res):
        print "--insert_local_branch_employee"
        for row in res:
            #折扣率
            if row[14] is None:
                discount=1
            else:
                discount=row[14]

            sql = """
             INSERT INTO BRANCH_EMPLOYEE (BRAID,EMPID,EMP_NAME,PASSWORD,DISCOUNT,STATUS,TIMESTAMP) \
             VALUES('{0}','{1}','{2}','{3}',{4},'{5}',{6});
              """
            sql = sql.format(row[0], row[1], row[2], row[12], discount, row[14] , row[19])
            print sql
            self.insert_local_table_by_sql(sql)


