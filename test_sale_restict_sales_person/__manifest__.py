# -*- coding: utf-8 -*-
{
    'name': "test sale restict sales person",
    
    'summary':"""restricting visibility based on the user's assigned sales team.""",
        
    'description': """Implement record-level access control for sale orders, restricting visibility based on the user's assigned sales team.
    """,

    'author': "Salma Mohamed",
    'website': "https://www.test.com",
    'contributors': ['Salma Mohamed <https://github.com/salma25128>'],
    'category': 'Sales/Template',
    'version': '17.0.1.2',
    'license': 'OPL-1',
    'depends': ['base','sale_management'],
    
    # always loaded
    'data': [
        "security/security.xml",
        "security/ir.model.access.csv",

    ],
        
    'installable': True,
    'application': True,
    'auto_install': False,
    # "uninstall_hook": 'uninstall_hook',
}
