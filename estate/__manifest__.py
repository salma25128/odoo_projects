{
  'name':'RealEstate',
  'depends':['base'],
    'application':True,
    'installable':True,
    'data': [
        'security/ir.model.access.csv',
         'data/sequence.xml',
        'views/estate_property_menu_views.xml',
        'views/estate_property_views.xml',
         'views/estate_property_types.xml',
         'views/estate_tags_views.xml',
          'views/estate_offers.xml',
          'reports/property_reports.xml'
             ],
        'assets': {
                    'web.assets_backend':['estate/static/src/css/property.css']
                     }
}
