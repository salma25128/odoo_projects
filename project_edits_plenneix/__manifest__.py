{
    'name':'plennix_project_addons',
    'author':'salma mohamed',

    'depends':['base','project','hr'],
    'installable':True,
    'category':'Project',
    'application':True,

    'data': [

             'security/ir.model.access.csv',
              'data/sequence.xml',
             'views/project_views.xml',
             'views/project_collaborators.xml',
            'views/project_task_views.xml',
             'reports/project_reports.xml'
    ]
}