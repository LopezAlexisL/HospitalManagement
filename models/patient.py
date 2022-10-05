from codecs import charmap_build
from importlib.metadata import files
from odoo import api, fields, models


class Patient(models.Model):
    _name = 'hospital.patient'

    name = fields.Char(string='Patient Name')
    last_name = fields.Char(string='Patient Last Name')
    age = fields.Char(string='Age')
    gender = fields.Selection(selection=[('m', 'Male'), ('f', 'Female'), ('o', 'Other')], string='Gender')
    
