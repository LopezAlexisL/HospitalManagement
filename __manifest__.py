{
    'name': 'Hospital Management',
    'version': '1.0.0',
    'sequence': '-100',
    'description': '',
    'summary': '',
    'author': '',
    'website': '',
    'license': 'LGPL-3',
    'category': 'Hospital Management',
    'depends': [
        'base',
        'mail',
        'sale',
        'product',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/patient_tag_data.xml',
        'data/sequence_data.xml',
        'data/patient.tag.csv',
        'wizard/cancel_appointment_view.xml',
        'views/menu.xml',
        'views/patient_view.xml',
        'views/female_patient.xml',
        'views/appointment_view.xml',
        'views/patient_tag_view.xml',
        'views/sale_order_view.xml',
    ],
    'demo': [
        ''
    ],
    'auto_install': False,
    'assets': {
        
    }
}