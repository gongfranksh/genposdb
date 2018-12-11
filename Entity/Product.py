# -*- coding: utf-8 -*-
from Entity.jsEntity import JsEntity

class Product(JsEntity):

    def __init__(self,branchcode):
        JsEntity.__init__(self, "Product",branchcode)

    def sync_product(self):
        try:
            stamps = self.get_local_time_stamp()
            print 'producttamps==>', stamps
            needinsert = self.get_remote_table_result_by_timestamp(stamps)
            # print needinsert
            self.insert_local_product(needinsert)
        except BaseException as e:
            print ("Sync_product error", e)

    def insert_local_product(self, res):
        print "--insert_local_product"
        i=0
        for row in res:
            row_12=self.IsNone(row[12])
            row_14=self.IsNone(row[14])
            row_15=self.IsNone(row[15])
            row_16=self.IsNone(row[16])
            row_17=self.IsNone(row[17])
            row_18=self.IsNone(row[18])
            row_19=self.IsNone(row[19])
            row_20=self.IsNone(row[20])
            row_21=self.IsNone(row[21])
            row_22=self.IsNone(row[22])
            row_23=self.IsNone(row[23])

            sql = """
                INSERT INTO PRODUCT (
                                    PROID,
                                    BARCODE,
                                    PRO_NAME,
                                    PRO_SNAME,
                                    CLASS_ID,
                                    SPEC,
                                    BRAND_ID,
                                    STAT_ID,
                                    GRADE,
                                    AREA,
                                    SUP_ID,
                                    MEASURE_ID,
                                    PACKET_QTY,
                                    TAX_TYPE,
                                    IN_TAX,
                                    TAX_PRICE,
                                    IN_PRICE,
                                    MIN_ORDER_QTY,
                                    NORMAL_PRICE,
                                    MEMBER_PRICE,
                                    GROUP_PRICE,
                                    RETURN_RAT,
                                    VIPDISCOUNT,
                                    POSDISCOUNT,
                                    STATUS,
                                    OPERATORID,
                                    CREATE_DATE,
                                    UPDATE_DATE,
                                    STOPDATE,
                                    TIME_STAMP
                                )
                                VALUES (  '{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}',
                                          '{10}','{11}',{12},'{13}',{14},{15},{16},{17},{18},{19},
                                          {20},{21},{22},{23},'{24}','{25}','{26}','{27}','{28}',{29}
                                 
                                );
                          """
            sql = sql.format(row[0], row[1], row[2], row[3],  row[4], row[5],row[6], row[7], row[8],  row[9],
                             row[10], row[11], row_12, row[13], row_14, row_15, row_16, row_17, row_18, row_19,
                             row_20, row_21, row_22, row_23, row[24], row[25], row[26], row[27], row[28], row[65],
                             )
            # print sql
            self.insert_local_table_by_sql(sql)
            self.print_need_insert(i,len(res))
            i+=1
