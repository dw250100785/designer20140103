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

class purchase_order(osv.osv):
    """ 扩展内部询价单"""
    _name = "purchase.order"
    _inherit = ['purchase.order']
    _columns = {
        'project_ids': fields.many2one('designer.project', string='项目简报'),
    }

class sale_order(osv.osv):
    """ 扩展报价单"""
    _name = "sale.order"
    _inherit = ['sale.order']
    _columns = {
        'project_ids': fields.many2one('designer.project', string='项目简报'),
    }

