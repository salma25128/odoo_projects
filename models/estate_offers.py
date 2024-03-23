from odoo import models, fields,api
from datetime import datetime


class Offers(models.Model):
    _name = 'estate.offers'
    _description = 'estate property offers'


    name = fields.Char(string="Offers")
    estate_property_ids = fields.Many2one("estate.property")
    partner_id = fields.Many2one("res.partner", string="partner")
    price = fields.Float()
    status = fields.Selection([("accepted","Accepted"),("refused","Refused")] ,copy="False")
    validity_date = fields.Char()
    date_deadline = fields.Date(compute="_compute_deadline", inverse="_inverse_deadline")
    create_date = fields.Datetime(default=fields.Datetime.now)
    validity = fields.Integer(default=7)


