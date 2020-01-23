from odoo import api, models, fields


class Course(models.Model):
    _name = 'openacademy.course'

    name = fields.Char()
    level = fields.Integer()
    sessions = fields.Many2many('openacademy.session', 'course')


class Person(models.Model):
    _name = 'openacademy.person'

    name = fields.Char()
    teaching = fields.One2many('openacademy.session', 'teacher')
    sessions = fields.Many2many('openacademy.session', 'attendees')


class Session(models.Model):
    _name = 'openacademy.session'

    name = fields.Char()
    course = fields.Many2many('openacademy.course')
    teacher = fields.Many2one('openacademy.person', 'teaching')
    attendees = fields.One2many('openacademy.person', 'sessions')
    state = fields.Selection([('draft', 'In preparation'), ('wip', 'In progress'), ('archived', 'Archived')])

