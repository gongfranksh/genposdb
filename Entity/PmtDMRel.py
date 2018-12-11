# -*- coding: utf-8 -*-
from Entity.jsEntity import JsEntity


class PMTDMREL(JsEntity):

    def __init__(self,branchcode):
        JsEntity.init_by_branch(self, "PMT_DM_REL",branchcode)

    def sync_pmtdmdel(self):
        try:
            stamps = self.get_local_time_stamp()
            print 'sync_pmtdmdel==>', stamps
            needinsert = self.get_need_update_record(stamps)
            # print needinsert
            self.insert_local_pmt_dm_rel(needinsert)
        except BaseException as e:
            print ("sync_pmtdmdel error", e)


    def get_need_update_record(self,timestamp):
        sql="""
       SELECT   BraId, d.DMId, h.DMBeginDate,h.DMEndDate,
                SupId, ProId, OrigSalePrice,SalePrice, 
                CONVERT (int,d.timestamp) as timestamp 
                FROM dbo.pmt_dm_rel d LEFT JOIN prompt_peroid_dm h ON h.DMId=d.DMId 
        WHERE CONVERT (int,d.timestamp) > {0}
        and   BraId = '{1}' 
        ORDER BY CONVERT (int,d.timestamp) 
        """
        sql=sql.format(timestamp,self.branch_code)
        print sql
        return self.get_remote_result_by_sql(sql)



    def insert_local_pmt_dm_rel(self, res):
        print "--insert_local_pmt_dm_rel"
        i=0
        for row in res:
            row_4=self.IsNone(row[4])
            row_5=self.IsNone(row[5])
            row_6=self.IsNone(row[6])
            sql = """
            INSERT INTO PMT_DM_REL (
                           BRAID,
                           DMID,
                           DMBEGIN_DATE,
                           
                           DMEND_DATE,
                           SUP_ID,
                           PROID,
                           
                           ORIG_SALE_PRICE,
                           SALE_PRICE,
                           TIME_STAMP
                       )
                       VALUES (
                       '{0}','{1}','{2}',
                       '{3}','{4}','{5}',
                       {6},{7},{8}
                       
                       )
            """
            sql=sql.format(row[0],row[1],row[2],
                           row[3], row[4], row[5],
                           row[6], row[7], row[8],
                           )
            # print sql
            self.insert_local_table_by_sql(sql)
            self.print_need_insert(i,len(res))
            i+=1
