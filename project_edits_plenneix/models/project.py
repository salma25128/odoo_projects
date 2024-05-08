from odoo import models, fields

class NewProject(models.Model):
    _inherit = 'project.project'

    odoo_version = fields.Integer(string='odoo version')
    odoo_type = fields.Selection(
        [('community', 'Community'),
         ('enterprise', 'Enterprise')],
        string='Odoo Type')

    Github_account= fields.Char()

    github_repo_url = fields.Char(string='GitHub Repo URL', widget="url")
    hosting = fields.Selection([('on_prem', 'On Prem'), ('cloud_hosting', 'Cloud Hosting'), ('odoo_sh', 'Odoo SH'),
                                ('odoo_online', 'Odoo Online')], string='Hosting')
    hosting_description = fields.Html(string='Hosting Description')

    collaborators_ids = fields.One2many("collaborators", "project_ids",string="collaborators")

