# Copyright 2015 Carlos Sánchez Cifuentes <csanchez@grupovermon.com>
# Copyright 2015-2016 Oihane Crucelaegui <oihane@avanzosc.com>
# Copyright 2015-2020 Tecnativa - Pedro M. Baeza
# Copyright 2016 Lorenzo Battistini
# Copyright 2016 Carlos Dauden <carlos.dauden@tecnativa.com>
# Copyright 2018 David Vidal <david.vidal@tecnativa.com>
# Copyright 2026 Trescloud - Steven Luna
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Sale Order Type Analytic",
    "version": "18.0.1.0.0",
    "category": "Sales Management",
    "author": "Grupo Vermon,"
    "AvanzOSC,"
    "Tecnativa,"
    "Agile Business Group,"
    "Niboo,"
    "Odoo Community Association (OCA),"
    "Trescloud CIA LTDA",
    "website": "https://github.com/OCA/sale-workflow",
    "license": "AGPL-3",
    "depends": ["sale_order_type"],
    # "demo": ["demo/sale_order_demo.xml"], # TODO: lo necesitamos?
    "data": [
        "views/sale_order_view.xml",
        "views/sale_order_type_view.xml",
    ],
    "installable": True,
    "auto_install": True,
}
