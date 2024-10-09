from odoo import models, fields, api ,Command

class ProductTemplate(models.Model):
    _inherit = 'product.template'


    def write(self, vals):
        manufacture_route = self.env.ref('mrp.route_warehouse0_manufacture')
        if 'route_ids' in vals:
            route_commands = vals.get('route_ids')
            route_ids = set()

            # many2Many field stored in relational table command tell it how to act
            for command in route_commands:
                if isinstance(command, (tuple, list)) and len(command) >= 2:
                    action, route_id = command[0], command[1]
                    if action in [4, 5, 6]:
                        route_ids.add(route_id)

            # Check
            if manufacture_route.id in route_ids:
                for rec in self:
                    if 'MRP' not in rec.name:
                        vals['name'] = rec.name + ' [MRP]'
            else:
                for rec in self:
                    # Remove [MRP]
                    vals['name'] = rec.name.replace(' [MRP]', '')

        res = super(ProductTemplate, self).write(vals)
        return res








