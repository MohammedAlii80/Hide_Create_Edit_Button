# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import UserError
from odoo.exceptions import ValidationError
from odoo.exceptions import Warning
from dateutil.relativedelta import relativedelta
from odoo.models import BaseModel
from lxml import etree

from odoo import api, fields, models, _
from odoo.exceptions import UserError

class stockpicking(models.Model):
    _inherit = 'stock.picking'



fields_view_get_extra = stockpicking.fields_view_get

def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):
    result = fields_view_get_extra(self, view_id=view_id, view_type=view_type, toolbar=toolbar, submenu=submenu)

    if self.env.user.has_group('Hide_Main_Buttons.hide_create_edit_button_inventory'):
        temp = etree.fromstring(result['arch'])
        temp.set('create', '0')
        result['arch'] = etree.tostring(temp)

    if self.env.user.has_group('Hide_Main_Buttons.hide_create_edit_button_inventory'):
        temp = etree.fromstring(result['arch'])
        temp.set('edit', '0')
        result['arch'] = etree.tostring(temp)
    return result

stockpicking.fields_view_get = fields_view_get



class purchase(models.Model):
    _inherit = 'purchase.order'



fields_view_get_extra = purchase.fields_view_get

def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):
    result = fields_view_get_extra(self, view_id=view_id, view_type=view_type, toolbar=toolbar, submenu=submenu)

    if self.env.user.has_group('makan_tracking.hide_create_edit_button_purchase'):
        temp = etree.fromstring(result['arch'])
        temp.set('create', '0')
        result['arch'] = etree.tostring(temp)

    if self.env.user.has_group('makan_tracking.hide_create_edit_button_purchase'):
        temp = etree.fromstring(result['arch'])
        temp.set('edit', '0')
        result['arch'] = etree.tostring(temp)
    return result

purchase.fields_view_get = fields_view_get

