from odoo import models, fields

class Types(models.Model):
    _name = 'estate.types'
    _description = 'estate property types'


    name = fields.Char(required=1, string="types")
