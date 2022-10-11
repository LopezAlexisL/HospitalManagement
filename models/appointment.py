from odoo import api, fields, models


class Appointment(models.Model):
    _name = 'hospital.appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description='Hospital Appointment'
    _rec_name = 'patient_id'

    patient_id= fields.Many2one(comodel_name='hospital.patient', string='Patient')
    appointment_time = fields.Datetime(string='Appointment Time', default=fields.Datetime.now)
    booking_time = fields.Date(string='Booking Date', default=fields.Date.context_today)
    gender = fields.Selection(related='patient_id.gender')
    identification_num = fields.Char(string='DNI') #funciona tambien con un related='patient_id.identification_number'


    @api.onchange('patient_id')
    def onchange_patient_id(self):
        self.identification_num = self.patient_id.identification_num
