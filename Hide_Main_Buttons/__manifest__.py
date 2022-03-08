# -*- coding: utf-8 -*-
{
    'name': "Hide Main Buttons",
    'version': '14.0.1.0',
    'summary': """This app provide option to hide "Edit"&"Create" button for specific user group.
                        After selecting this option user will not be able to see edit& create buttons
                        In Inventory Or Purchase Apps
                    """,

    'description': """
        Long description of module's purpose
    """,

    'author': "Mohammed Ali",
    'license': 'OPL-1',
    # any module necessary for this one to work correctly
    'depends': ['base','purchase','stock'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'price': 17.00,
    'currency': 'EUR',
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
