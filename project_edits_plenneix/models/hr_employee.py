from odoo import models,fields


class HREmployee(models.Model):
    _inherit = 'hr.employee'

    collaborators_ids = fields.One2many("collaborators","user_id",string="collaborators")