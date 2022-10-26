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
        'product',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/patient_view.xml',
        'views/female_patient.xml',
        'views/appointment_view.xml'
    ],
    'demo': [
        ''
    ],
    'auto_install': False,
    'assets': {
        
    }
}