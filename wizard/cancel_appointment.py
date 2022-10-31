import datetime
from odoo import api, fields, models


class CancelAppointment(models.TransientModel):
    _name = 'cancel.appointment.wizard'
    _description = 'Cancel Appointment Wizard'

    @api.model
    def default_get(self, fields):
        res = super(CancelAppointment, self).default_get(fields)
        res['cancelation_date'] = datetime.date.today()
        return res

    appointment_id = fields.Many2one('hospital.appointment', string='Appointment')
    reason = fields.Text(string='Reason for the cancelation')
    cancelation_date = fields.Date(string='Cancelation Date')

    def action_cancel(self):
        return