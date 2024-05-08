from odoo import models, fields

class Collaborators(models.Model):
    _name = 'collaborators'
    _description = ' project ctollaborators'

    employee_id =fields.Many2one('hr.employee', string='Employee', index=True, tracking=True)
    user_id = fields.Many2one('res.users', string='Employee', index=True, tracking=True, default=lambda self: self.env.user)
    status = fields.Selection(
                                [('active', 'Active'),
                                         ('inactive', 'Inactive')],
                                  string='Status')
    project_ids = fields.Many2one("project.project")

    def action_active(self):
        for rec in self:
            rec.status = 'active'


    def action_inactive(self):
        for rec in self:
            rec.status= 'inactive'