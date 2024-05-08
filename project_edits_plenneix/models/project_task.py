from odoo import models, fields, api

class ProjectTask(models.Model):
    _inherit = 'project.task'


    ref = fields.Char(default='new', readonly=True, copy=False)

    developer_id = fields.Many2one('hr.employee', string='Developer')
    functional_consultant_id = fields.Many2one('hr.employee', string='Functional Consultant')
    development_status = fields.Selection([
                                                    ('pending', 'Pending'),
                                                    ('ongoing', 'Ongoing'),
                                                    ('delivered', 'Delivered'),
                                                    ('onhold', 'On Hold'),
                                                    ('cancelled', 'Cancelled')],
                                                    string='Development Status')

    module = fields.Char(string='Module')
    branch = fields.Char(string='Branch')
    release_notes = fields.Text(string='Release Notes')
    # priority = fields.Selection([
    #                              ('low', 'Low'),
    #                              ('medium', 'Medium'),
    #                              ('high', 'High')],
    #                               string='Priority')

    internal_deadline = fields.Date(string='Internal Deadline')
    allocated_time_research = fields.Float(string='Research and Solution Design Allocated Time')
    allocated_time_development = fields.Float(string='Development Allocated Time')
    allocated_time_testing = fields.Float(string='Testing Allocated Time')
    total_allocated_time = fields.Float(string='Total Allocated Time', compute='_compute_total_allocated_time')
    _sql_constraints = [
        ('ref_unique', 'unique(ref)', 'reference must be unique!'),
    ]

    # sequence
    @api.model
    def create(self, vals):
        if vals.get('task_number', 'new') == 'new':
            vals['ref'] = self.env['ir.sequence'].next_by_code('project.task.sequence') or 'new'
            res = super(ProjectTask, self).create(vals)
        return res

    # allocated time
    @api.depends('allocated_time_research', 'allocated_time_development', 'allocated_time_testing')
    def _compute_total_allocated_time(self):
        for rec in self:
           rec.total_allocated_time = rec.allocated_time_research + rec.allocated_time_development + rec.allocated_time_testing