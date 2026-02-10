# Copyright 2026 Trescloud - Steven Luna
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class SaleOrderTypology(models.Model):
    _name = "sale.order.type"
    _inherit = ['sale.order.type' ,'analytic.mixin']
