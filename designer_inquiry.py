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

class designer_inquiry(osv.osv):
    """ 自定义的询价单"""
    _name = "designer.inquiry"
    _inherit = ['mail.thread']
    _columns = {
        'name': fields.char('单号', size=64, required=True, select=True, help="Unique number of the purchase order, computed automatically when the purchase order is created."),
        'partner_id':fields.many2one('res.partner', '制作部', required=True,
            change_default=True, track_visibility='always'),
        'project_ids': fields.many2one('designer.project', string='项目简报'),
        'date_order':fields.date('日期', required=True, select=True, help="Date on which this document has been created."),
        'card_line': fields.one2many('designer.inquiry.line', 'card_id', '物料清单'),
        'state': fields.selection([('draft', '草稿中'),
            ('open', '已批准'),
            ('cancel', '已拒绝'),
            ('close', '已完成')],
            '状态', readonly=True, track_visibility='onchange',
        )
    }
    _description = "内部询价单，针对外包商"
    _rec_name = 'name'
    _sql_constraints = [

    ]
    _defaults = {
         'date_order': fields.date.context_today,
         'state': lambda *a: 'draft',
         'name': lambda obj, cr, uid, context: '/',
    }
    _order = 'name asc'

    def create(self, cr, uid, vals, context=None):
        if vals.get('name','/')=='/':
            vals['name'] = self.pool.get('ir.sequence').get(cr, uid, 'designer.inquiry') or '/'
        order =  super(designer_inquiry, self).create(cr, uid, vals, context=context)
        return order

    def copy(self, cr, uid, id, default=None, context=None):
        if not default:
            default = {}
        default.update({
            'state':'draft',
            'name': self.pool.get('ir.sequence').get(cr, uid, 'designer.inquiry'),
        })
        return super(designer_inquiry, self).copy(cr, uid, id, default, context)

    def designer_card_cancel(self, cr, uid, ids, context=None):
        return self.write(cr, uid, ids, {'state': 'cancel'}, context=context)

    def designer_card_open(self, cr, uid, ids, context={}):
        return self.write(cr, uid, ids, {'state': 'open'}, context=context)

    def designer_card_close(self, cr, uid, ids, context={}):
        return self.write(cr, uid, ids, {'state': 'close'}, context=context)

    def designer_card_draft(self, cr, uid, ids, context={}):
        return self.write(cr, uid, ids, {'state': 'draft'}, context=context)

class designer_inquiry_line(osv.osv):
    """ 项目工作卡物料管理"""
    _name = 'designer.inquiry.line'
    _inherit = ['mail.thread']
    _columns = {
        'card_id': fields.many2one('designer.inquiry', '工作卡', ondelete='cascade', select=True),
        'line_no': fields.char('编号', required=True,change_default=True, select=True, track_visibility='always'),
        'project_request': fields.text('项目要求', size=64, required=True, change_default=True, select=True, track_visibility='always'),
        'number': fields.integer('数量', required=True, change_default=True, select=True, track_visibility='always'),
        'price': fields.float('价格',digits_compute= dp.get_precision('Price'), required=True, change_default=True, select=True, track_visibility='always'),
        'subprice': fields.float('总价', required=True, change_default=True, select=True, track_visibility='always'),
        'note': fields.text('备注',size=64,change_default=True, select=True, track_visibility='always'),
    }
    _sql_constraints = [
        ('line_no', 'unique(line_no)', 'The name of the idea must be unique')
    ]
    _defaults = {
    }
    _order = 'line_no asc'
