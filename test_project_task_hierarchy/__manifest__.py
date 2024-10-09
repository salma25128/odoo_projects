# -*- coding: utf-8 -*-
# Author: test
{
    'name': "test project task hierarchy",
    'summary': """Manage task and sub-task hierarchy with dynamic tree view. """,
    'description': """
        tasks and sub-tasks maintain a hierarchical order in the tree view, with sub-tasks indented beneath parent tasks.
    """,
    'author': "Salma Mohamed",
    'website': "https://www.tag.com",
    'contributors': ['Salma Mohamed <https://github.com/salma25128>'],
    'version': '17.0.1.2',
    'license': 'OPL-1',
    'depends': ['base', 'project'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/project_task_views.xml',
    ],

    'assets': {
        'web.assets_backend': [
            'test_project_task_hierarchy/static/src/js/task_hierarchy_component.js',
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,

}
