odoo.define('channel_doctor.channel_doctor_time_slot', function (require) {
    'use strict';

    let publicWidget = require('web.public.widget');

    publicWidget.registry.channelDoctorTimeSlot = publicWidget.Widget.extend({
        selector: '.channel-doctor-available-slots',
        events: {
            'click .book-appointment': '_onClickBookAppointment',
        },

        /**
         * @private
         * Redirect to the appointment fill details page
         */
        _onClickBookAppointment: function (ev) {
            window.location.href = $(ev.target).data('href');
        },

    })
});