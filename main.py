# -*- coding: utf-8 -*-
from Entity.Branch import Branch
from Entity.BranchEmployee import BranchEmployee
from Entity.PmtDMRel import PMTDMREL
from Entity.Product import Product
from Entity.ProductBarCode import ProductBarCode
from Entity.ProductBranchRel import ProductBranchRel

branch=Branch()
branchemployee=BranchEmployee()
product = Product()
productbarcode = ProductBarCode()
productbranchrel = ProductBranchRel('01002')
pmtdmrel  = PMTDMREL('01002')

branchemployee.sync_branch_employee()
branch.sync_branch()
product.sync_product()
productbarcode.sync_productbarcode()
productbranchrel.sync_productbranchrel()
pmtdmrel.sync_pmtdmdel()
