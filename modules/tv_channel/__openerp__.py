# -*- coding: utf-8 -*-
{
    'name': "tv_channel",
    'summary': """TV channel model""",
    'description': """TV channel model""",
    'author': "Ilyas",
    'website': "https://github.com/ilyasProgrammer",
    'category': 'Custom',
    'version': '0.1',
    'depends': ['contacts'],
    'external_dependencies': {"python": ['Tkinter']},
    # sudo apt-get install python-tk
    'data': [
        # 'data.xml',
        'views/channel.xml',
        'views/contacts_view_alter.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
}