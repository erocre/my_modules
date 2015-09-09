from openerp import models, fields, api

class HRCourse(models.Model):

    _name = 'hr.course'
    _description = u'hr_course'
    _inherit = 'mail.thread'

    _order = 'name ASC'

    name = fields.Char(
        string='Name',
        required=True,
        help=False,
        size=50,
        translate=True
    )
    date_start = fields.Date(
        string='Date start',
        required=False,
        readonly=False,
        index=False,
        default=False,
        help=False
    )
    date_end = fields.Date(
        string='Date end',
        required=False,
        readonly=False,
        index=False,
        default=False,
        help=False
    )

		
class HRNeed(models.Model):

    _name = 'hr.need'
    _inherit = ['hr.need', 'mail.thread']

    course_id = fields.Many2one(
        string='Courses',
        comodel_name='hr.course',
    )