from odoo import models, fields, api
from odoo17.odoo.exceptions import ValidationError


class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'estate odoo app'
    # _log_access = False         #prevent log access login except id / automated fields

    name = fields.Char(required=1)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date()
    expected_price = fields.Float(required=1, default=100.0)
    selling_price = fields.Float()
    bedrooms = fields.Integer()

    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    living_area = fields.Integer()
    garden_area = fields.Integer()
    total_area = fields.Integer(compute="_compute_total")
    garden_orientation = fields.Selection([('north', 'North'), ('south', 'South'),
                                           ('east', 'East'), ('west', 'West')]
                                            ,default="south")

    user_id = fields.Many2one('res.users', string='Salesman', index=True, tracking=True,
                              default=lambda self: self.env.user)
    partner_id = fields.Many2one("res.partner", string="Buyer")

    estate_tags_ids = fields.Many2many("estate.tags", string="Tags")
    estate_types_id = fields.Many2one("estate.types", string="Types")
    offers_ids = fields.One2many("estate.offers", "estate_property_ids",string="offers")
    best_price = fields.Float(compute="_compute_best_price")


    # user_email = fields.Char('User Email', related='user_id.email', readonly=True)
    # user_login = fields.Char('User Login', related='user_id.login', readonly=True)
    # sql constraints
    _sql_constraints = [
        ('unique_name','unique(name)','hello'),
        ('price_positive', 'check("expected_price > 0")', 'expected price must be positive')
       ]

    # python constraints
    @api.constrains('bedrooms')
    def _check_bedrooms(self):
        for rec in self:
            if rec.bedrooms == 0:
                raise ValidationError('Please enter valid number of bedrooms')

    # computed fields
    @api.depends('garden_area','living_area')
    def _compute_total(self):
         for rec in self:
            rec.total_area = rec.garden_area + rec.living_area

    @api.depends('offers_ids')
    def _compute_best_price(self):
        for rec in self:
            rec.best_price = max(self.mapped('offers_ids.price'),default=0)