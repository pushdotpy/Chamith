# -*- coding: utf-8 -*-

{
    "name": "Channel Doctor",
    "author": "",
    "website": "",
    "support": "",
    "category": "Project",
    "summary": "Doctor channeling process for Odoo",
    "description": """
Doctor channeling process for Odoo
""",
    "version": "16.0.1.0.0",
    "depends": [
        'website',
    ],
    "data": [
        'data/website_data.xml',
        'views/channel_doctor_search_templates.xml',
        'views/channel_doctor_available_slots_templates.xml',
        'views/channel_doctor_enter_details_templates.xml',
        'views/channel_doctor_booking_success_templates.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            # SCSS
            'channel_doctor/static/src/scss/channel_doctor_search.scss',
            'channel_doctor/static/src/scss/channel_doctor_available_slots.scss',
            'channel_doctor/static/src/scss/channel_doctor_enter_details.scss',
            'channel_doctor/static/src/scss/channel_doctor_booking_success.scss',
            # JS
            'channel_doctor/static/src/js/channel_doctor_time_slot.js',
            'channel_doctor/static/src/js/channel_doctor_booking_success.js',
        ],
    },
    "application": False,
    "auto_install": False,
    "installable": True,
    "license": 'LGPL-3'
}