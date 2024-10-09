{
    'name':'test sale order notifications',
    'installable':True,
    'application':True,
    'summary': 'automated action to send an email to the salesperson when a sale order moves to the "Invoiced" stage.',
    'depends': ['sale', 'mail'],
    'data': [
        'views/sale_order_views.xml',
        'data/email_templates.xml',  # Email template
    ],
    'author': "Salma Mohamed",
    'contributors': ['Salma Mohamed <https://github.com/salma25128>'],
}