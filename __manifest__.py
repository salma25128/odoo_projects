{
    'name':'Real Estate',
    'depends':['base'],
    'application':True,
    'installable':True,

    'data':[
            'security/ir.model.access.csv',
            'views/estate_property_menu_views.xml',
            'views/estate_property_views.xml',
             'views/estate_property_types.xml',
             'views/estate_tags_views.xml',
              'views/estate_offers.xml'
            ]
}
