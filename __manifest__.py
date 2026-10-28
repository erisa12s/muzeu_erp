{
    'name': 'Muzeu ERP',
    'version': '1.0',
    'summary': 'Sistemi per Menaxhimin e Muzeut',
    'category': 'Management',
    'author': 'Your Name',
    'depends': ['base'],
    'data': [
        'security/muzeu_security.xml',
        'security/ir.model.access.csv',
        'report/muzeu_bileta_report.xml',
        'views/muzeu_demtimet_views.xml',  # <-- MË PARË KËTU!
        'views/muzeu_artisti_views.xml',
        'views/muzeu_bileta_views.xml',
        'views/muzeu_kati_views.xml',
        'views/muzeu_lloji_biletes_views.xml',
        'views/muzeu_stafi_views.xml',
        'views/muzeu_itinerari_views.xml',
        'views/muzeu_vizitori_views.xml',
        'views/muzeu_vepra_views.xml',     # <-- PAS DEMTIMET!
        'views/muzeu_views.xml',
    ],
    'installable': True,
    'application': True,
}