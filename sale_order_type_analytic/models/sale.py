# Copyright 2020 Tecnativa - Pedro M. Baeza
# Copyright 2023 Tecnativa - Sergio Teruel
# Copyright 2026 Trescloud - Steven Luna
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from datetime import datetime, timedelta

from odoo import _, api, fields, models


class SaleOrder(models.Model):
    _name = "sale.order"
    _inherit = ["sale.order", "analytic.mixin"]

    @api.depends("type_id")
    def _compute_analytic_distribution(self):
        # Se inspira en como está hecho en versión 16, pero adaptado a la distribución analitica en versión 18
        res = None
        if hasattr(super(), "_compute_analytic_distribution"):
            res = super()._compute_analytic_distribution()
        for order in self.filtered("type_id"):
            order_type = order.type_id
            if order_type.analytic_distribution:
                order.analytic_distribution = order_type.analytic_distribution
        return res

class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    @api.depends("order_id.type_id")
    def _compute_analytic_distribution(self):
        # Herencia para aplicar la distribución analítica definida en la distribución del encabezado del pedido de venta.
        res = super()._compute_analytic_distribution()
        for line in self.filtered("order_id.type_id"):
            order_type = line.order_id.type_id
            if order_type.analytic_distribution:
                line.analytic_distribution = order_type.analytic_distribution
        return res
