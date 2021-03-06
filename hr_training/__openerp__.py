# -*- coding: utf-8 -*-
###############################################################################
#
#    Odoo, Open Source Management Solution
#
#    Copyright (c) All rights reserved: Eduardo Rodríguez Crespo
#        (c) 2015  
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses
#
###############################################################################
{
	'name': 'Human Resource Training',
	'description': 'Methology of training',
	'author': 'Eduardo Rodríguez Crespo',
	'depends': ['mail','hr'],
	'category': 'HR',
	'data': [
		'views/hr_training.xml',
		'security/ir.model.access.csv',
	],
	'application': False,
	'installable': True
}