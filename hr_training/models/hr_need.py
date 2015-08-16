# -*- coding: utf-8 -*-
from openerp import models, fields, api
class hr_need (models.Model):
    """ Needs of training """
    _name = 'hr.need'
    _description = u'Every training need were located here'
    _order = 'date ASC'

    name = fields.Char(
        string='Name',
        required=True,
        readonly=False,
        index=True,
        default=None,
        help=False,
        size=50,
        translate=True
    )
    description = fields.Text(
        string='Description',
        required=False,
        readonly=False,
        index=False,
        default=None,
        help=False,
        translate=True
    )
    date = fields.Date(
        string='Date',
        required=False,
        readonly=False,
        index=False,
        default=fields.Date.today,
        help=False
    )
    active = fields.Boolean(
        string='Active',
        required=False,
        readonly=False,
        index=False,
        default=True,
        help=False
    )

    @api.one
    def need_inactive(self):
    	if self.active == True :
    		self.active = False
    	return True