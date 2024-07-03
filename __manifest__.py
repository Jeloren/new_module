# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': "FirstModule",
    'summary': "This is my First Module",
    'description': "",
    'category': 'FirstModule/FirstModule',
    'version': '1.0',
    'depends': [
       
    ],
    'data': [
        "views/view_model1.xml",
        "views/view_groups.xml",
        "views/view_prepods.xml",
        "views/view_journal.xml",
        "views/view_grades.xml",
        "views/view_subject.xml",
        "views/menu.xml",
        "security/my_group.xml",
        "security/ir.model.access.xml",
    ],
    #'demo': [
   #     'demo/account_peppol_demo.xml',
   # ],
    'license': 'LGPL-3',
}
