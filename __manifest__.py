{
    'name': 'Brainvire-Website-Sale',
    'version': '1.0',
    'category': 'Website Sales',
    'description': """
        This module helps link the sale distributors from sales screen through website orders payment screen
         to select the specific distributor.
    """,
    'website': 'https://www.brainvire.com/',
    'depends': ['base', 'website_sale'],
    'data': [
        'views/views.xml',
        'views/template.xml'
    ],
    'assets': {
            'web.assets_frontend': [
                'brainvire/static/src/js/website_sale_custom.js'
            ]
    },
    'auto_install': False,
}
