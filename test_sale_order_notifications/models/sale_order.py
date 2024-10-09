from odoo import models, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.model
    def send_invoiced_email(self, sale_order):
        # Check if the sale order is invoiced
        if sale_order.state == 'sale' and sale_order.invoice_status == 'invoiced':
            email_template = self.env.ref('test_sale_order_notifications.email_template_invoiced_sale_order')
            if email_template:
                email_template.send_mail(sale_order.id, force_send=True)
