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
import openerp.addons.decimal_precision as dp

from openerp.osv import osv
from openerp.osv import fields
from openerp.tools.translate import _
import time

class designer_bill(osv.osv):
    """ 发票管理"""
    _name = "designer.bill"
    _inherit = ['mail.thread']

    _columns = {
        'partner_id':fields.many2one('res.partner', '客户', required=True,
            change_default=True, track_visibility='always'),
        'invoice_head': fields.char('发票抬头', size=64, required=True),
        'invoice_amount': fields.float('金额', digits_compute=dp.get_precision('invoice_amount'),required=True),
        'project_ids': fields.many2one('designer.project', string='项目简报'),
        'state_apply': fields.selection(
            [('true', '是'),
            ('false', '否')],
            '申请',track_visibility='onchange',
        ),
        'state_make_out': fields.selection(
            [('true', '是'),
            ('false', '否')],
            '开票',track_visibility='onchange',
        ),
        'state_draw': fields.selection(
            [('true', '是'),
            ('false', '否')],
            '领取', track_visibility='onchange',
        ),
        'state_arrive': fields.selection(
            [('true', '是'),
            ('false', '否')],
            '到账',track_visibility='onchange',
        )

    }
    _rec_name = 'invoice_head'

    _order = 'partner_id asc'

    _defaults = {
        'state_apply': 'false',
        'state_make_out': 'false',
        'state_draw': 'false',
        'state_arrive': 'false',
    }
