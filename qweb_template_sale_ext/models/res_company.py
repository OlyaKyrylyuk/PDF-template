from odoo import models, fields


class ResCompany(models.Model):
    _inherit = 'res.company'

    edrpou = fields.Char(string="EDRPOU")
    certificate_number = fields.Char(string="Certificate Number")
