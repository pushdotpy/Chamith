odoo.define('channel_doctor.booking_success', function (require) {
    'use strict';

    let publicWidget = require('web.public.widget');

    publicWidget.registry.channelDoctorBookingSuccess = publicWidget.Widget.extend({
        selector: '.channel-doctor-booking-success',
        events: {
            'click .btn-back-home': '_onclickBackHome'
        },

        /**
         * @private
         * Redirect back to the homepage
         */
        _onclickBackHome: function (ev) {
            window.location.href = '/';
        },

    })
});