# -*- coding: utf-8 -*-
###############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2023-TODAY Cybrosys Technologies(<https://www.cybrosys.com>)
#    Author: Junaidul Ansar M (odoo@cybrosys.com)
#
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    (AGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
{
    'name': 'All in One Multi Followers',
    'version': '16.0.1.0.0',
    'category': 'Extra Tools',
    'summary': 'The module used to add or remove the multi followers in the '
               'whole odoo models by dynamic actions.',
    'description': ' The module used to add or remove the multi followers in '
                   'the whole odoo models by dynamic actions.If you want to set'
                   ' a multi followers in your model this is helpful you to '
                   'select the multi followers when clicking the action. '
                   'After adding or removing the followers it will affect'
                   ' the model. So in this way you can add or remove multiple'
                   ' followers in the whole odoo quickly.',
    'author': 'Cybrosys Techno Solutions',
    'company': 'Cybrosys Techno Solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'website': 'https://www.cybrosys.com',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/multi_follower_views.xml',
        'views/res_config_settings_views.xml',
        'wizard/follower_adding_removing_views.xml',
    ],
    'images': ['static/description/banner.jpg'],
    'license': 'AGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False
}
