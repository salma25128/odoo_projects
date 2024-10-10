
from odoo import models, fields, api

class ProjectTask(models.Model):
        _inherit = 'project.task'

        parent_id = fields.Many2one('project.task', string='Parent Task', ondelete='cascade', index=True)
        child_ids = fields.One2many('project.task', 'parent_id', string='Sub-tasks')
        depth = fields.Integer(string='Depth', compute='_compute_depth', store=True)
# Parent_id > depth >filter
        @api.depends('parent_id')
        def _compute_depth(self):
            for task in self:
                depth = 0
                parent = task.parent_id
                while parent:
                    depth += 1
                    parent = parent.parent_id
                    task.depth = depth

        @api.model
        def get_ordered_tasks(self):
            ordered_tasks = []
            def add_task_and_subtasks(task, depth=0):
                task_data = {
                    'id': task.id,
                    'name': task.name,
                    'parent_id': task.parent_id.id if task.parent_id else None,
                    'depth': depth,
                }
                ordered_tasks.append(task_data)
                for sub_task in task.child_ids:
                    add_task_and_subtasks(sub_task, depth + 1)
            root_tasks = self.search([('parent_id', '=', False)])
            for root_task in root_tasks:
                add_task_and_subtasks(root_task)

            return ordered_tasks


        # -----------------------------------------------------------------
        #    parent_id = fields.Many2one(
        #     'project.task', string="Parent Task", index=True,
        #     help="The parent task of this task."
        # )
        #
        # child_ids = fields.One2many(
        #     'project.task', 'parent_id', string="Subtasks"
        # )
        #
        # # Sequence field to order tasks
        # sequence = fields.Integer(default=10)
        #
        # @api.depends('parent_id')
        # def _compute_task_hierarchy(self):
        #     """ This method can compute task hierarchy for sorting. """
        #     for task in self:
        #         if task.parent_id:
        #             task.sequence = task.parent_id.sequence + 1
        #         else:
        #             task.sequence = 10
        # --------------------------------------------
        # @api.model
        # def create(self, vals):
        #
        #     if vals.get('parent_id'):
        #         parent_task = self.browse(vals.get('parent_id'))
        #         vals['sequence'] = parent_task.sequence + 1
        #     return super(ProjectTask, self).create(vals)
        #
        # def write(self, vals):
        #     if 'parent_id' in vals:
        #         parent_task = self.browse(vals.get('parent_id'))
        #         vals['sequence'] = parent_task.sequence + 1
        #     return super(ProjectTask, self).write(vals)
    # --------------------------------------------------------------------------------------
    # parent_id = fields.Many2one('project.task', string='Parent Task', ondelete='cascade')
    # child_ids = fields.One2many('project.task', 'parent_id', string='Sub-tasks')
    #
    #
        # @api.model
        # def read_group(self, domain, fields, groupby, offset=0, limit=None, orderby=None, lazy=True):
        #     # Call the super method with all expected parameters
        #     result = super(ProjectTask, self).read_group(
        #         domain=domain,
        #         fields=fields,
        #         groupby=groupby,
        #         offset=offset,
        #         limit=limit,
        #         orderby=orderby,
        #         lazy=lazy
        #     )
        #     # Apply custom sorting
        #     # result = sorted(result, key=lambda x: (x.get('parent_id', 0), x.get('id')))
        #     result = sorted(result, key=lambda x: (x.get('parent_id') or 0, x.get('id') or 0))
        #
        #     return result
        #


    #----------------------------------------------------------------------------------------------
#
#
# class ProjectTask(models.Model):
#     _inherit = 'project.task'
#
#     # This field will represent the parent task
#     parent_id = fields.Many2one(
#         'project.task', string="Parent Task", index=True,
#         help="The parent task of this task."
#     )
#
#     # This field represents the child tasks (subtasks)
#     child_ids = fields.One2many(
#         'project.task', 'parent_id', string="Subtasks"
#     )
#
#     # Sequence field to order tasks
#     sequence = fields.Integer(default=10)
#
#     @api.depends('parent_id')
#     def _compute_task_hierarchy(self):
#         """ This method can compute task hierarchy for sorting. """
#         for task in self:
#             if task.parent_id:
#                 task.sequence = task.parent_id.sequence + 1
#             else:
#                 task.sequence = 10
#
#     @api.model
#     def create(self, vals):
#         """ Overriding the create method to manage sequence. """
#         if vals.get('parent_id'):
#             parent_task = self.browse(vals.get('parent_id'))
#             vals['sequence'] = parent_task.sequence + 1
#         return super(ProjectTask, self).create(vals)
#
#     def write(self, vals):
#         """ Ensure task hierarchy is maintained on update. """
#         if 'parent_id' in vals:
#             parent_task = self.browse(vals.get('parent_id'))
#             vals['sequence'] = parent_task.sequence + 1
#         return super(ProjectTask, self).write(vals)
# -------------------------------------------------------------------
#
#     @api.model
#     def get_task_hierarchy(self):
#         """
#         Get a hierarchical structure of tasks and sub-tasks.
#         """
#         # Fetch all tasks
#         tasks = self.search([])
#         task_dict = {}
#
#         # Create a dictionary with task id as key
#         for task in tasks:
#             task_dict[task.id] = {
#                 'task': task,
#                 'children': []
#             }
#
#         # Build the hierarchy
#         for task in tasks:
#             if task.parent_id:
#                 task_dict[task.parent_id.id]['children'].append(task_dict[task.id])
#
#         # Collect the top-level tasks (tasks without a parent)
#         top_level_tasks = [task for task in task_dict.values() if not task['task'].parent_id]
#
#         return top_level_tasks
