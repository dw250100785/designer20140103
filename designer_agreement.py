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
import logging

import openerp.addons.decimal_precision as dp

from openerp.osv import osv
from openerp.osv import fields
from openerp.tools.translate import _
import math
import time

_logger = logging.getLogger()
class designer_contract_type(osv.osv):
    """ 品牌"""
    _name = 'designer.contract.type'
    _columns = {
        'name': fields.char('名称', size=64, required=True),
        'comment': fields.text('备注', help='备注'),
    }
    _sql_constraints = [
        ('name', 'unique(name)', '名称不能重复')
    ]

    _order = 'name asc'



class designer_agreement(osv.osv):
    """ 扩展发票管理"""

    _name = "designer.agreement"
    _inherit = ['mail.thread']



    #人民币金额转大写程序Python版本
    #Copyright: zinges at foxmail.com
    #blog: http://zingers.iteye.com
    #感谢zinges提供了Python的版本

    def numtoCny(self,contract_amount):

        capUnit = ['万','亿','万','圆','']
        capDigit = { 2:['角','分',''], 4:['仟','佰','拾','']}
        capNum=['零','壹','贰','叁','肆','伍','陆','柒','捌','玖']
        snum = str('%019.02f') % contract_amount
        if snum.index('.')>16:
            return ''
        ret,nodeNum,subret,subChr='','','',''
        CurChr=['','']
        for i in range(5):
            j=int(i*4+math.floor(i/4))
            subret=''
            nodeNum=snum[j:j+4]
            lens=len(nodeNum)
            for k in range(lens):
                if int(nodeNum[k:])==0:
                    continue
                CurChr[k%2] = capNum[int(nodeNum[k:k+1])]
                if nodeNum[k:k+1] != '0':
                    CurChr[k%2] += capDigit[lens][k]
                if  not ((CurChr[0]==CurChr[1]) and (CurChr[0]==capNum[0])):
                    if not((CurChr[k%2] == capNum[0]) and (subret=='') and (ret=='')):
                        subret += CurChr[k%2]
            subChr = [subret,subret+capUnit[i]][subret!='']
            if not ((subChr == capNum[0]) and (ret=='')):
                ret += subChr

        return [ret,capNum[0]+capUnit[3]][ret=='']

    def onchange_contractamount(self, cr, uid, ids, contract_amount):
        if contract_amount > 0 :
            #这里需要注意 调用numtoCny   函数时 传参个数的统一，总监大人说了 重庆-mrshelly(49812643)  15:30:23
            #因为你使用了 self.numtoCny 所以,  有一个默认的 self 参数传过去了.
            big = self.numtoCny(contract_amount)
            return {'value':{'contract_amount_big': big}}
        else :
            return {}



    _columns = {
        'partner_id':fields.many2one('res.partner', '客户', required=True,
            change_default=True, track_visibility='always'),
        'contract_type': fields.many2one('designer.contract.type',string='合同类型', required=True),
        'contract_amount': fields.float('合同金额', digits_compute=dp.get_precision('contract_amount'),required=True),
        'contract_amount_big': fields.char('合同金额大写', required=True),
        'project_ids': fields.many2one('designer.project', string='项目简报'),
        'card_line': fields.one2many('designer.agreement.rule.line', 'card_id', '付款方式'),
        'state': fields.selection([
            ('draft', '草稿中'),
            ('open', '已批准'),
            ('verify1', '一次确认'),
            ('verify2', '二次确认'),
            ('cancel', '已拒绝')],
            '状态', readonly=True, track_visibility='onchange',
        ),


    }
    _rec_name = "contract_type"

    _defaults = {

    }
    def designer_agreement_draft(self, cr, uid, ids, context={}):
        return self.write(cr, uid, ids, {'state': 'draft'}, context=context)

    def designer_agreement_cancel1(self, cr, uid, ids, context=None):
        return self.write(cr, uid, ids, {'state': 'cancel'}, context=context)

    def designer_agreement_cancel2(self, cr, uid, ids, context=None):
        return self.write(cr, uid, ids, {'state': 'cancel'}, context=context)

    def designer_agreement_open(self, cr, uid, ids, context={}):
        return self.write(cr, uid, ids, {'state': 'open'}, context=context)

    def designer_agreement_verify1(self, cr, uid, ids, context={}):
        return self.write(cr, uid, ids, {'state': 'verify1'}, context=context)

    def designer_agreement_verify2(self, cr, uid, ids, context={}):
        return self.write(cr, uid, ids, {'state': 'verify2'}, context=context)



class designer_agreement_rule_line(osv.osv):
    """ 项目工作卡物料管理"""
    _name = 'designer.agreement.rule.line'
    _inherit = ['mail.thread']
    _columns = {
        'card_id': fields.many2one('designer.agreement', '工作卡', ondelete='cascade', select=True),
        'line_no': fields.integer('次数', required=True,change_default=True, select=True, track_visibility='always'),
        'percentage': fields.float('比例',digits_compute= dp.get_precision('Price'), required=True, change_default=True, select=True, track_visibility='always'),
        'price': fields.float('金额',digits_compute= dp.get_precision('Price'), required=True, change_default=True, select=True, track_visibility='always'),
        'note': fields.text('里程碑',size=64,change_default=True, select=True, track_visibility='always'),
    }
    _sql_constraints = [
        ('line_no', 'unique(line_no)', 'The name of the idea must be unique')
    ]
    _rec_name = "line_no"
    _defaults = {
     #   'line_no': 1,
    }
    _order = 'line_no asc'

