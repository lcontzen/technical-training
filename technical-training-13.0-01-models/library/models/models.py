from odoo import api, models, fields

class Book(models.Model):
    _name = 'library.book'
    _description = 'Book'

    name = fields.Char(string='Title')
    author = fields.Many2many('library.person', 'authored_books')
    isbn = fields.Char()


class Person(models.Model):
    _name = 'library.person'
    _description = 'Person'

    name = fields.Char()
    address = fields.Char()
    email = fields.Char()
    authored_books = fields.Many2many('library.book', 'author')

class Rental(models.Model):
    _name = 'library.rental'
    _description = 'Rentals'

    book = fields.Many2many('library.book')
    renter = fields.Many2many('library.person')
    rental_date = fields.Date()
    return_date = fields.Date()
