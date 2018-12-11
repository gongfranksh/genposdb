# -*- coding: utf-8 -*-
from Entity.jsEntity import JsEntity


class ProductBarCode(JsEntity):

    def __init__(self,branchcode):
        JsEntity.init_table_diff(self, "Product_barcode", "Product_bar_code",branchcode)

    def sync_productbarcode(self):
        try:
            stamps = self.get_local_time_stamp()
            print 'sync_productbarcaode==>', stamps
            needinsert = self.get_remote_table_result_by_timestamp(stamps)
            # print needinsert
            self.insert_local_product_barcode(needinsert)
        except BaseException as e:
            print ("Sync_product error", e)

    def insert_local_product_barcode(self, res):
        print "--insert_local_product_barcode"
        i=0
        for row in res:
            row_4=self.IsNone(row[4])
            row_5=self.IsNone(row[5])
            row_6=self.IsNone(row[6])
            sql = """
              INSERT INTO PRODUCT_BAR_CODE (
                                 PROID,
                                 BARCODE,
                                 BAR_MODE,
                                 QUANTITY,
                                 NORMAL_PRICE,
                                 MEMBER_PRICE,
                                 STATUS,
                                 MAIN_FLAG,
                                 TIME_STAMP
                             ) VALUES ('{0}','{1}','{2}',{4},{5},{6},'{7}','{8}' ,{9});
                          """
            sql = sql.format(row[0], row[1], row[2], row[3], row_4, row_5, row_6, row[7], row[8], row[12]
                           )
            # print sql
            self.insert_local_table_by_sql(sql)
            self.print_need_insert(i,len(res))
            i+=1
