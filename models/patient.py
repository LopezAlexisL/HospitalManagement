from odoo import api, fields, models


class Patient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']


    name = fields.Char(string='Patient Name')
    last_name = fields.Char(string='Patient Last Name')
    identification_num = fields.Integer(string='ID Number')
    age = fields.Integer(string='Age')
    gender = fields.Selection(selection=[('m', 'Male'), ('f', 'Female'), ('o', 'Other')], string='Gender')
    active = fields.Boolean(string='Active', default=True)
    
