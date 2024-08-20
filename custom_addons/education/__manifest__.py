
{
    'name': 'Education',
    'version': '1.0.0',
    'summary': 'Education payment system',
    'description': """
        Payment automation system
    """,
    'author': 'Obidjon',
    'sequence': -100,
    'category': 'Education',
    'depends': ['base'],
    'data': [
        'security/payment_automation_security.xml',
        'security/ir.model.access.csv',
        'views/course_view.xml',
        'views/group_view.xml',
        'views/teacher_view.xml',
        'views/student_view.xml',
        'views/payment_view.xml',
        'views/teacher_payment_views.xml',
    ],
    'installable': True,
    'application': True,
}
