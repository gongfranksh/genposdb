# -*- coding: utf-8 -*-
import os
import shutil

from Entity.Branch import Branch
from Entity.BranchEmployee import BranchEmployee
from Entity.GetBranch import GetBranch

##获取有效门店
from Entity.PmtDMRel import PMTDMREL
from Entity.Product import Product
from Entity.ProductBarCode import ProductBarCode
from Entity.ProductBranchRel import ProductBranchRel


def check_branch_sqllite():
    sqllite_db = 'jsPos'
    activebranch=GetBranch()
    branches=activebranch.get_active_branch()
    #数据库模板
    db_template=sqllite_db+'.db'
    if os.path.exists(db_template):
        print db_template+ ' is found'

    for row in branches:
        local_sqllite_db= sqllite_db+row[0]+'.db'
        if os.path.exists(local_sqllite_db) :
            print local_sqllite_db +' is found!'
        else:
            shutil.copy(db_template,local_sqllite_db)
            print local_sqllite_db + ' is need created!'


def sync_all():
    check_branch_sqllite()
    activebranch=GetBranch()
    branches=activebranch.get_active_branch()
    for row in branches:
        branch = Branch(row[0])
        branchemployee = BranchEmployee(row[0])
        product = Product(row[0])
        productbarcode = ProductBarCode(row[0])
        productbranchrel = ProductBranchRel(row[0])
        pmtdmrel = PMTDMREL(row[0])

        branchemployee.sync_branch_employee()
        branch.sync_branch()
        product.sync_product()
        productbarcode.sync_productbarcode()
        productbranchrel.sync_productbranchrel()
        pmtdmrel.sync_pmtdmdel()