# -*- coding: utf-8 -*-
from Entity.jsEntity import JsEntity


class ProductBranchRel(JsEntity):

    def __init__(self,branchcode):
        JsEntity.init_by_branch(self, "Product_branch_rel",branchcode)

    def sync_productbranchrel(self):
        try:
            stamps = self.get_local_time_stamp()
            print 'sync_productbranchrel==>', stamps
            needinsert = self.get_remote_table_result_by_branch_timestamp(stamps)
            print needinsert
            self.insert_local_product_branch_rel(needinsert)
        except BaseException as e:
            print ("Sync_product error", e)

    def insert_local_product_branch_rel(self, res):
        print "--insert_local_product_barcode"
        for row in res:
            row_17=self.IsNone(row[17])
            row_10=self.IsNone(row[10])
            row_8=self.IsNone(row[8])
            row_5=self.IsNone(row[5])
            row_6=self.IsNone(row[6])
            row_2=self.IsNone(row[2])
            row_3=self.IsNone(row[3])
            row_9=self.IsNone(row[9])
            row_7=self.IsNone(row[7])

            sql = """
                          INSERT INTO PRODUCT_BRANCH_REL (
                                   BRAID,  PROID, SUP_ID, CAN_CHANGE_PRICE,
                                   SUP_PMT_FLAG,PROMT_FLAG, POT_FLAG, DCFLAG,

                                   MIN_PRICE,
                                   MAX_PRICE,
                                   NORMAL_PRICE,
                                   MEMBER_PRICE,
                                   RETURN_RAT,
                                   STATUS,
                                   OPERATORID,
                                   CREATE_DATE,
                                   
                                   UPDATE_DATE,
                                   STOPDATE,
                                   TIME_STAMP
                               )
                               VALUES ('{0}','{1}','{2}','{3}',{4},'{5}','{6}',{7},
                               {8},{9},{10},{11},{12},{13},'{14}',
                               '{15}','{16}','{17}',{18});
                          """
            sql = sql.format(row[0], row[1], row[14], row[4], row_10, row[12], row[13], row_17,
                             row_8, row_5,row_6, row_2, row_3, row_9, row_7, row[23],
                             row[21], row[22], row[25]
                             )
            print sql

            self.insert_local_table_by_sql(sql)
