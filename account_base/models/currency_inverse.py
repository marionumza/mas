# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class Currency(models.Model):
    _inherit = "res.currency"

    rate = fields.Float()

class CurrencyRate(models.Model):
    _inherit = "res.currency.rate"

    inverse_rate = fields.Float()
    rate = fields.Float()

    @api.onchange('inverse_rate')
    def onchange_inverse(self):
        if self.inverse_rate:
            self.rate = 1/self.inverse_rate
        else:
            self.rate = 0