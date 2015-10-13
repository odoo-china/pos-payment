# -*- coding: utf-8 -*-
##############################################################################
#
#    POS Payment Terminal module for Odoo
#    Copyright (C) 2014 Aurélien DUMAINE
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


{
    'name': 'POS Online Payment',
    'version': '0.1',
    'category': 'Point Of Sale',
    'summary': 'Manage Online Payment from POS front end',
    'description': """

    """,
    'author': 'Odoo CN Community, Jeffery <jeffery9@gmail.com>',
    'depends': ['point_of_sale'],
    'data': [
        'pos_payment.xml',
        'pos_payment_view.xml',
        ],
    'installable': True,

}
