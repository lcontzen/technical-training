from odoo import api, models, fields


class Course(models.Model):
    _name = 'openacademy.course'

    name = fields.Char()
    level = fields.Integer()


class Person(models.Model):
    _name = 'openacademy.person'

    name = fields.Char()
    teaching = fields.One2Many('openacademy.session')
    sessions = fields.Many2many('openacademy.session')


class Session(models.Model):
    _name = 'openacademy.session'

    name = fields.Char()
    course = fields.Many2many('openacademy.course')
    teacher = fields.Many2one('openacademy.person', 'teaching')
    attendees = fields.One2Many('openacademy.person', 'sessions')
    state = fields.Selection([('draft', 'In preparation'), ('wip', 'In progress'), ('archived', 'Archived')])

