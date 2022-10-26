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
    identification_num = fields.Char(string='DNI', help='Patient ID Number') #funciona tambien con un related='patient_id.identification_number'
    prescription = fields.Html(string='Prescription')
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'Very High')], string='Priority')
    state = fields.Selection(selection=[
        ('draft', 'Draft'),
        ('in_consultation', 'In consultation'),
        ('done', 'Done'),
        ('canceled', 'Canceled')], default='draft', string='Status', required=True)
    doctor = fields.Many2one(comodel_name='res.users', string='Doctor')
    pharmacy_ids = fields.One2many('appointment.pharmacy', 'appointment_id', string='Pharmacy Lines')
    hide_price = fields.Boolean(string='Hide Price')


    @api.onchange('patient_id')
    def onchange_patient_id(self):
        self.identification_num = self.patient_id.identification_num

    def action_button(self):
        return {
            'effect': {
                'fadeout': 'slow',
                'message': 'Done Succesfully',
                'type': 'rainbow_man'
            }
        }

    def action_in_consultation(self):
        for rec in self:
            rec.state = 'in_consultation'
    
    def action_done(self):
        for rec in self:
            rec.state = 'done'

    def action_canceled(self):
        for rec in self:
            rec.state = 'canceled'

    def action_draft(self):
        for rec in self:
            rec.state = 'draft'



class Appointment_Pharmacy(models.Model):
    _name = 'appointment.pharmacy'
    _description = 'Appointments Pharmacy Lines'

    product_id = fields.Many2one('product.product', required=True)
    qty = fields.Integer(string='Quantity', default=1)
    price_unit = fields.Float(string='Price', related='product_id.list_price')
    appointment_id = fields.Many2one('hospital.appointment', string='Appointment')