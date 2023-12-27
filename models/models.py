# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import _, api, fields, models, tools, Command
from odoo.exceptions import UserError, ValidationError


class Partner(models.Model):
    _inherit = 'res.partner'

    distributor = fields.Boolean('Is Distributor')
    default_distributor = fields.Boolean('Default Distributor?')

    @api.constrains('default_distributor')
    def _check_distributor(self):
        check_distributor = self.env['res.partner'].search([('default_distributor', '=', True)])
        if len(check_distributor) > 1:
            raise ValidationError(_("You cannot enable multiple distributor!!"))


class Sales(models.Model):
    _inherit = 'sale.order'

    sale_distributor = fields.Many2one('res.partner', 'Distributor')

