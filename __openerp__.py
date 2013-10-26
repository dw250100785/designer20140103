# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


{
    'name': 'Designer for Wuhan',
    'version': '0.1',
    'category': 'Tools',
    'description': """
武汉设计师广告行业管理软件
========================
1.重用addons
创意
项目
合同
发票
base
mail
2.全部模块  新建的对象【表】
工作卡   designer.card


""",
    'author': 'Evebit',
    'website': 'http://evebit.com',
    'depends': ['mail','base','idea','project','account_analytic_analysis','project_issue','crm','sale','hr','account','document','purchase',],
    'data': [
        'base_menu.xml',
        'designer_project_view.xml',
        'designer_brand_view.xml',
        'designer_idea_view.xml',
        'designer_card_view.xml',
        'designer_archive_view.xml',
        'designer_order_view.xml',
        'designer_paper_view.xml',
        'designer_policy_view.xml',
        'designer_quotation_view.xml',
        'designer_invoice_view.xml',
        'designer_contract_view.xml',
        'designer_inquiry_view.xml',
        'designer_offer_view.xml',
        'designer_bill_view.xml',
        'designer_agreement_view.xml',
        'designer_user.xml',
        'designer_sequence.xml',
        'security/designer_security.xml',
        'security/ir.model.access.csv',
        'workflow/designer_workflow.xml',
        'workflow/designer_idea_workflow.xml',
        'workflow/designer_order_workflow.xml',
        'workflow/designer_paper_workflow.xml',
        'workflow/designer_policy_workflow.xml',
        'workflow/designer_card_workflow.xml',
    ],
    'test':[],
    'installable': True,
    'images': [],
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
