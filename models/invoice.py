# -*- encoding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class AccountMove(models.Model):
    _inherit = 'account.move'

    bolson_id = fields.Many2one("bolson.bolson", string="Liquidacion", readonly=True, ondelete='restrict')
