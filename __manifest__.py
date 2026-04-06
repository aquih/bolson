# -*- encoding: utf-8 -*-

{
    'name' : 'Bolson',
    'version' : '2.2',
    'category': 'Custom',
    'description': """Manejo de cajas chicas y liquidaciones ( obsoleto, ya no usar )""",
    'author': 'aquíH',
    'website': 'http://www.aquih.com/',
    'depends' : [ 'account' ],
    'data' : [
        'views/report.xml',
        'views/bolson_view.xml',
        'views/reporte_bolson.xml',
        'security/ir.model.access.csv',
        'security/bolson_security.xml',
    ],
    'license': 'Other OSI approved licence',
    'installable': True,
    'certificate': '',
}
