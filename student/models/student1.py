from odoo import models, fields, api


class student_student1(models.Model):
    _name = 'student.student1'
    _description = 'school student'

    name = fields.Char(string='student Name',required='True')
    age = fields.Integer(string='Age')
    student_class= fields.Char(string='Class')