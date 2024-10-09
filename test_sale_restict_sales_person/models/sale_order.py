from odoo import models, fields,api
from odoo.exceptions import AccessError

class SalesOrder(models.Model):
    # _name = 'sales.restrictions'
    _inherit = 'sale.order'

    user_id = fields.Many2one('res.users', string='Salesperson')

    @api.constrains('user_id')
    def _check_salesperson_permission(self):
        for order in self:
            if not self.env.user.has_group('test_sale_restict_sales_person.group_manager'):
                raise AccessError("Only managers can change the salesperson on a sale order.")
    # ui change
    @api.onchange('user_id')
    def _onchange_salesperson(self):
        if not self.env.user.has_group('test_sale_restict_sales_person.group_manager'):
            raise AccessError("Only managers can change the salesperson on a sale order.")
