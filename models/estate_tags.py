from odoo import models, fields

class Tags(models.Model):
    _name = 'estate.tags'
    _description = 'estate property tags'


    name = fields.Char(required=1 ,string="Tags")
    estate_property_ids = fields.Many2many("estate.property")
