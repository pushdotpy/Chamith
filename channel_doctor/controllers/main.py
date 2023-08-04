# -*- coding: utf-8 -*-

from odoo import http, _
from odoo.http import Controller, route, request


class ChannelDoctor(Controller):

    @http.route('/channel-doctor-search', type='http', auth='public', website=True)
    def channel_doctor_search(self, **kwargs):
        """
        Render channel doctor search view
        """
        values = {}
        return request.render("channel_doctor.channel_doctor_search", values)

    @route('/available-doctors', type='http', auth='public', website=True, methods=['POST'])
    def channel_doctor_available_slots(self, **post):
        """
        Render channel doctor available slots view
        """
        values = {}
        return request.render("channel_doctor.channel_doctor_available_slots", values)

    @http.route(['/doctor-appointment/<int:slot_id>'], type='http', auth='public', website=True)
    def book_appointment(self, slot_id=None, **kwargs):
        """
        Book appointment and redirect to enter details page
        """
        values = {
            'action_url': f'/submit/appointment/{slot_id}'
        }
        return request.render("channel_doctor.channel_doctor_enter_details", values)

    @http.route(['/submit/appointment/<int:slot_id>'], type='http', auth='public', website=True)
    def submit_appointment(self, slot_id=None, **kwargs):
        """
        Submit appointment and redirect to success page
        """
        values = {}
        return request.render("channel_doctor.channel_doctor_booking_success", values)
