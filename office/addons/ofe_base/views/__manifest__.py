#-*- coding:utf-8 -*-
{
    'name': 'Office Base',
    'category': 'Office Management System',
    'version': '13.0',
    'sequence': 1,
    'author': 'Office',
    'summary': 'Office',
    'description': "Office",
    'depends': [
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/office_views.xml',
        'views/menus.xml',
    ],
    'qweb':[],
    'images': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
