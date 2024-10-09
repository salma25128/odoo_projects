# -*- coding: utf-8 -*-
{
    'name': "test product is mrp",
    'summary':""" Automatically update product names to include the MRP tag if the route is set to Manufacturing. """,
    'description': """ Add [mrp] tag to product has mrp route """,
    'author': "Salma Mohamed",
    'website': "https://www.tag.com",
   'contributors': ['Salma Mohamed <https://github.com/salma25128>'],
    'category': 'mrp',
    'version': '17.0.1.2',
    'license': 'OPL-1',
    'depends': ['base','mrp'],
    'data': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    # "uninstall_hook": 'uninstall_hook',
}