odoo.define('brainvire.website_sale_custom', require => {
    'use strict';

    const checkoutForm = require('payment.checkout_form');
    const manageForm = require('payment.manage_form');

    const PaymentMixin = {

        //--------------------------------------------------------------------------
        // Private
        //--------------------------------------------------------------------------

        /**
         * Add `distributor` to the transaction route params if it is provided & then send it to
         * `sale.order` form when processing payment.
         *
         * @override method from payment.payment_form_mixin
         * @private
         * @param {string} code - The provider code of the selected payment option.
         * @param {number} paymentOptionId - The id of the selected payment option.
         * @param {string} flow - The online payment flow of the selected payment option.
         * @return {object} The extended transaction route params.
         */
        _prepareTransactionRouteParams: function (code, paymentOptionId, flow) {
            const transactionRouteParams = this._super(...arguments);
            var distributor = document.querySelector('input[name="distributor"]:checked').value;;
            return {
                ...transactionRouteParams,
                'distributor': distributor
            };
        },

    };

    checkoutForm.include(PaymentMixin);
    manageForm.include(PaymentMixin);

});
