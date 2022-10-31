from datetime import date
from odoo import api, fields, models


class Patient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    

    name = fields.Char(string='Patient Name', tracking=True)
    last_name = fields.Char(string='Patient Last Name', tracking=True)
    identification_num = fields.Integer(string='ID Number')
    patient_reference = fields.Char(string='Reference')
    age = fields.Integer(string='Age', compute='_compute_age', tracking=True)
    birth_date = fields.Date(string='Birth Date')
    gender = fields.Selection(selection=[('m', 'Male'), ('f', 'Female'), ('o', 'Other')], string='Gender', default='m')
    active = fields.Boolean(string='Active', default=True)
    tag_ids = fields.Many2many('patient.tag', string='Tags')

    @api.model
    def create(self, vals):
        #here can be put the names of the field variables of the model and asing as a default value for that field using "vals['field_name'] = 'default value'" method
        vals['patient_reference'] = self.env['ir.sequence'].next_by_code('hospital.patient')
        return super(Patient, self).create(vals)
    
    def write(self, vals): #use it to update vals automaticaly without manualy assing
        if not self.patient_reference:
            vals['patient_reference'] = self.env['ir.sequence'].next_by_code('hospital.patient')
        return super(Patient, self).write(vals)
    
    @api.depends('birth_date')
    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.birth_date:
                rec.age = today.year - rec.birth_date.year - ((today.month, today.day) < (rec.birth_date.month, rec.birth_date.day))
            else:
                rec.age = 0