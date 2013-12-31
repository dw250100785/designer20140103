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

from openerp.osv import osv
from openerp.osv import fields
from openerp.tools.translate import _
import time
import workflow_func
from openerp.addons.base.ir import ir_attachment


class project_project(osv.osv):
    _name = 'project.project'
    _inherit = "project.project"
    _columns = {
        'work_id': fields.many2one('designer.card', '所属工作卡', change_default=True, select=True, track_visibility='always'),
        }
project_project()

class designer_project(osv.osv):
    """ 项目简报"""
    _name = 'designer.project'
    _inherit = ['mail.thread','ir.attachment']

    def _data_get(self, cr, uid, ids, name, arg, context=None):
        if context is None:
            context = {}
        result = {}
        location = self.pool.get('ir.config_parameter').get_param(cr, uid, 'ir_attachment.location')
        bin_size = context.get('bin_size')
        for attach in self.browse(cr, uid, ids, context=context):
            if location and attach.store_fname:
                result[attach.id] = self._file_read(cr, uid, location, attach.store_fname, bin_size)
            else:
                result[attach.id] = attach.db_datas
        return result

    def _data_set(self, cr, uid, id, name, value, arg, context=None):
        # We dont handle setting data to null
        if not value:
            return True
        if context is None:
            context = {}
        location = self.pool.get('ir.config_parameter').get_param(cr, uid, 'ir_attachment.location')
        file_size = len(value.decode('base64'))
        if location:
            attach = self.browse(cr, uid, id, context=context)
            if attach.store_fname:
                self._file_delete(cr, uid, location, attach.store_fname)
            fname = self._file_write(cr, uid, location, value)
            super(ir_attachment, self).write(cr, uid, [id], {'store_fname': fname, 'file_size': file_size}, context=context)
        else:
            super(ir_attachment, self).write(cr, uid, [id], {'db_datas': value, 'file_size': file_size}, context=context)
        return True


    _columns = {
        #'datas_fname': fields.char('附件名',size=256),#必须上传附件
        #'datas': fields.function(_data_get, fnct_inv=_data_set, string='附件', type="binary", nodrop=True),
        'create_uid': fields.many2one('res.users','简报撰写人', required=True, readonly=True,states={'draft': [('readonly', False)]}),
        'work_id': fields.many2one('designer.card', '所属工作卡', readonly=True, states={'draft': [('readonly', False)]}, required=True, change_default=True, select=True, track_visibility='always'),
        'name': fields.char('项目简报', size=64, required=True, readonly=True, states={'draft': [('readonly', False)]}),
        'partner_id': fields.many2one('res.partner', '客户', readonly=True, states={'draft': [('readonly', False)]}, required=True, change_default=True, select=True, track_visibility='always'),
        'product_id': fields.many2one('product.product', '产品', readonly=True, required=True, change_default=True, select=True,states={'draft': [('readonly', False)]}),
        'client_current_situation': fields.text('客户情况', help='包括企业背景，历史沿革、经营范围、行业地位、品牌发展状况、产品销售状况、产品特点、价格、消费者关系、通路状况、行销计划、包装策略、当前广告表现、以往广告等', readonly=True, states={'draft': [('readonly', False)]}),
        'problem': fields.text('面临问题', help='面临问题', readonly=True, states={'draft': [('readonly', False)]}),
        'ad_requirement': fields.text('广告需求', help='广告需求', readonly=True, states={'draft': [('readonly', False)]}),
        'client_will': fields.text('客户意向', help='客户意向', readonly=True, states={'draft': [('readonly', False)]}),
        'how_to_operating': fields.text('如何跟进', help='如何跟进', readonly=True, states={'draft': [('readonly', False)]}),
        'manager_will': fields.text('总经理意向', help='总经理意向', readonly=True, states={'draft': [('readonly', False)]}),
        'receiver_uid':fields.many2one('res.users','我方对接人', required=True, readonly=True ,states={'draft': [('readonly', False)]}),
        'project_ids': fields.many2one('project.project', string='项目', readonly=True, states={'draft': [('readonly', False)]}),
        'state': fields.selection([('draft', '草稿中'),
            ('open', '已批准'),
            ('cancel', '已拒绝'),
            ('close', '已完成')],
            '状态', readonly=True, track_visibility='onchange',
        ),
         #工作流审批以及记录
        'wkf_logs':fields.function(
            workflow_func._get_workflow_logs,
            string='审批记录',
            type='one2many',
            relation="workflow.logs",
            readonly=True),
    }
    _sql_constraints = [
        ('name', 'unique(name)', 'The name of the idea must be unique')
    ]
    _defaults = {
        'state': lambda *a: 'draft',
    }
    _order = 'name asc'

    def designer_project_cancel(self, cr, uid, ids, context=None):
        return self.write(cr, uid, ids, {'state': 'cancel'}, context=context)

    def designer_project_open(self, cr, uid, ids, context={}):
        return self.write(cr, uid, ids, {'state': 'open'}, context=context)

    def designer_project_close(self, cr, uid, ids, context={}):
        return self.write(cr, uid, ids, {'state': 'close'}, context=context)

    def designer_project_draft(self, cr, uid, ids, context={}):
        return self.write(cr, uid, ids, {'state': 'draft'}, context=context)
