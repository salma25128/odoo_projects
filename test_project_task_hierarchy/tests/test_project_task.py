from odoo.tests import common

class TestProjectTaskOrdering(common.TransactionCase):

    def test_task_ordering(self):
        Task = self.env['project.task']
        # Create tasks and sub-tasks
        parent1 = Task.create({'name': 'Task 1'})
        sub1 = Task.create({'name': 'Sub-task 1.1', 'parent_id': parent1.id})
        parent2 = Task.create({'name': 'Task 2'})
        sub2 = Task.create({'name': 'Sub-task 2.1', 'parent_id': parent2.id})
        sub_sub1 = Task.create({'name': 'Sub-sub-task 1.1.1', 'parent_id': sub1.id})

        ordered_tasks = Task.get_ordered_tasks()

        self.assertEqual(len(ordered_tasks), 5)
        self.assertEqual(ordered_tasks[0]['name'], 'Task 1')
        self.assertEqual(ordered_tasks[1]['name'], 'Sub-task 1.1')
        self.assertEqual(ordered_tasks[2]['name'], 'Sub-sub-task 1.1.1')
