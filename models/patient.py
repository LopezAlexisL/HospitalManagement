from datetime import date
from odoo import api, fields, models


class Patient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    

    name = fields.Char(string='Patient Name', tracking=True)
    last_name = fields.Char(string='Patient Last Name', tracking=True)
    identification_num = fields.Integer(string='ID Number')
    age = fields.Integer(string='Age', compute='_compute_age', tracking=True)
    birth_date = fields.Date(string='Birth Date')
    gender = fields.Selection(selection=[('m', 'Male'), ('f', 'Female'), ('o', 'Other')], string='Gender', default='m')
    active = fields.Boolean(string='Active', default=True)
    
    @api.depends('birth_date')
    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.birth_date:
                rec.age = today.year - rec.birth_date.year - ((today.month, today.day) < (rec.birth_date.month, rec.birth_date.day))
            else:
                rec.age = 0