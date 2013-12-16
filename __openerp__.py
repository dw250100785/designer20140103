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
    'category': 'Other',
    'sequence': 300,
    'summary': '武汉设计师广告行业管理软件',
    'maintainer': '250100785@qq.com',
    'description': u"""
武汉设计师广告行业管理软件
========================

        系统要求：
            openerp7.0
        功能:
        1. 接受淘宝主动通知，自动添加、确认订单、发货等。
        2. 同步淘宝订单
        3. 导入淘宝产品, 同步库存
        4. 导入淘宝用户
        5. 自动评价，中差评预警
        6. 跟踪淘宝订单物流信息, 签收提醒
        7. ......
""",
    'author': 'Evebit',
    'website': 'http://evebit.com',
    'depends': [
        'mail',
        'base',
        'idea',
        'project',
        'account_analytic_analysis',
        'project_issue',
        'crm',
        'sale',
        'hr',
        'account',
        'document',
        'purchase',
        ],
    'data': [
        'security/designer_security.xml',
        'security/access_agreement/ir.model.access.csv',
        'security/access_archive/ir.model.access.csv',
        'security/access_bill/ir.model.access.csv',
        'security/access_card/ir.model.access.csv',
        'security/access_idea/ir.model.access.csv',
        'security/access_inquiry/ir.model.access.csv',
        'security/access_offer/ir.model.access.csv',
        'security/access_order/ir.model.access.csv',
        'security/access_paper/ir.model.access.csv',
        'security/access_policy/ir.model.access.csv',
        'security/access_project/ir.model.access.csv',
        'designer_user.xml',
        'base_menu.xml',
        'designer_project_view.xml',
        'designer_brand_view.xml',
        'designer_idea_view.xml',
        'designer_card_view.xml',
        'designer_archive_view.xml',
        'designer_order_view.xml',
        'designer_paper_view.xml',
        'designer_policy_view.xml',
        #'designer_quotation_view.xml',
        #'designer_invoice_view.xml',
        #'designer_contract_view.xml',
        'designer_inquiry_view.xml',
        'designer_offer_view.xml',
        'designer_bill_view.xml',
        'designer_agreement_view.xml',
        'designer_sequence.xml',
        'workflow/designer_workflow.xml',
        'workflow/designer_idea_workflow.xml',
        'workflow/designer_order_workflow.xml',
        'workflow/designer_paper_workflow.xml',
        'workflow/designer_policy_workflow.xml',
        'workflow/designer_card_workflow.xml',
        'workflow/designer_bill_workflow.xml',
    ],
    'update_xml': [],
    'js': [],
    'css': [],
    'qweb': [],
    'demo': [],
    'test':[],
    'application': False,
    'installable': True,
    'auto_install': False,
    'images': [],
    'certificate' : '001292377792581874189',
    "license": "GPL-3",
    "active": False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
