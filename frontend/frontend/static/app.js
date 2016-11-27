var project = {};

(function (namespace, _, $) {

    "use strict";

    // Global events
    var globalSubmit = "globalSubmit";

    /**
     * Search form UI
     * @constructor
     *
     * Public methods:
     *
     * .enable()
     * .disable()
     * .getValues()
     *
     */
    function SearchForm() {
        this._carId = $("#car_id");
        this._certificateId = $("#certificate_id");
        this._submitButton = $("#submit_button_id");

        this._fields = [this._carId, this._certificateId, this._submitButton];

        this._disabledClassName = "disable";
        this._keyUp = "keyUp";

        this._loadData();

        this._certificateId.on(this._keyUp, $.proxy(this._saveData, this));
        this._carId.on(this._keyUp, $.proxy(this._saveData, this));
        this._submitButton.on("click", $.proxy(this._submit, this));
    }

    SearchForm.prototype = {

        /**
         * Load form data from cookies
         * @private
         */
        _loadData: function () {
            this._carId.val(Cookies.get('car_id'));
            this._certificateId.val(Cookies.get('certificate_id'));
        },

        /**
         * Save all form data to cookies
         * @private
         */
        _saveData: function () {
            Cookies.set('car_id', this._carId.val());
            Cookies.set('certificate_id', this._certificateId.val());
        },

        /**
         *
         * @private
         */
        _submit: function () {
            $(document).trigger(globalSubmit);
            this.disable();
        },

        /**
         * Disable form controls
         */
        disable: function () {
            _.forEach(this._fields, $.proxy(function (field) {
                field.addClass(this._disabledClassName)
            }), this);
        },

        /**
         * Enable form controls
         */
        enable: function () {
            _.forEach(this._fields, $.proxy(function (field) {
                field.removeClass(this._disabledClassName)
            }), this);
        },

        /**
         * Get current form values
         * @returns {{carId, certificateId}}
         */
        getValues: function () {
            return {
                carId: this._carId.val(),
                certificateId: this._certificateId.val()
            }
        },

        /**
         * Validate field contents
         *
         * @param field
         * @returns {boolean}
         * @private
         */
        _validateField: function (field) {

            var errorClassName = "invalid";

            if (field.val().replace(" ", "") !== "") {
                field.removeClass(errorClassName);
                return true
            } else {
                field.addClass(errorClassName);
                return false;
            }
        },

        /**
         * Check if entered form values are valid
         *
         *  @returns {boolean}
         */
        isValid: function () {
            if (this._validateField(this._carId) && this._validateField(this._certificateId)) {
                return true;
            }
            return false;
        }

    };


    /**
     * Result table UI
     * @constructor
     */
    function ResultTable () {
        this._container = $("#table-container");
        this._months = [3, 6, 9, 12];
        this._template = _.template('' +
            '<table class="deep-purple-text">' +
            '   <thead>' +
            '       <tr>' +
            '           <th data-field="provider">' +
            '               Apdrošinātājs' +
            '           </th>' +
            '               <% _.forEach(months, function(item) { %>' +
            '                   <th class="center" data-field="<%- item %>months">' +
            '                       <%- item %> mēneši' +
            '                   </th>' +
            '               <% }); %>' +
            '       </tr>' +
            '    </thead>' +
            '    <tbody>' +
            '       <% _.forEach(rows, function(row) { %>' +
            '           <tr>' +
            '               <% _.forEach(row, function(col) { %>' +
            '                   <td class="center" data-field="' +
            '                       <% if (col !== null && typeof col === "object") { %>' +
            '                           <%- col %>months' +
            '                       <% } else { %>' +
            '                           provider ' +
            '                       <% } %>">' +
            '                       <% if (col !== null && typeof col === "object") { %>' +
            '                           <a href="<%- col.website %>" class="waves-effect waves-light btn-flat">' +
            '                               <i class="material-icons right">open_in_new</i>' +
            '                               <%- col.name %>' +
            '                           </a>' +
            '                       <% } else { %>' +
            '                           <%- col %> EUR' +
            '                       <% } %>' +
            '                   </td>' +
            '               <% }); %>' +
            '           </tr>' +
            '       <% }); %>' +
            '   </tbody>' +
            '</table>');
        this._data = [];
    }

    ResultTable.prototype = {

        /**
         *
         * @param rowData - array containing all row values
         */
        addRow: function(rowData) {
            this._data.push(rowData);
            this.render()
        },

        /**
         * Render table html
         */
        render: function(){
            this._container.html(this._template({
                months: this._months,
                rows: this._data
            }))
        }

    };

    function OCTARobot() {

        this._form = new SearchForm();
        this._table = new ResultTable();

        this._loader = $("#loader");

        this._providerDetails = {
            baltikums: {
                name: "Baltikums",
                website: "https://www.polise24.lv/lv/octa-online/"
            },
            compensa: {
                name: "Compensa",
                website: "http://online.compensa.lv/lv/Octa"
            },
            gjensidige: {
                name: "Gjensidige",
                website: "https://www.gjensidige.lv/pirkt-octa/online-service"
            },
            seesam: {
                name: "Seesam",
                website: "https://www.seesam.lv/polise/"
            },
            if_company: {
                name: "IF",
                website: "https://web.if.lv/mansif/if/policies/Mtpl/entry.aspx"
            }
        };

        $(document).on(globalSubmit, $.proxy(this._fetchResults, this));

    }

    OCTARobot.prototype = {

        /**
         * Fetch results and feed to the table class
         */
        _fetchResults: function () {

            var table = this._table,
                loader = this._loader,
                providers = this._providerDetails,
                form = this._form,
                values = form.getValues(),
                rowsLoaded = 0,
                rowsTotal = _.keys(this._providerDetails).length;

            // Don't do anything if invalid form data
            if (!form.isValid()){
                return;
            }

            loader.show();

            _.forEach(_.keys(providers), function (item) {
                $.ajax({
                    dataType: "json",
                    url: "/api/provider-check/" + item + "/" + values.carId + "/" + values.certificateId + "/",
                    timeout: 30000,  // 30 seconds
                    success: function (data) {
                        table.addRow([providers[item]].concat(data));
                        rowsLoaded++;
                        if (rowsLoaded === rowsTotal){
                            loader.hide();
                        }
                    }
                });
            });
        }
    };

    namespace.start = function () {
        new OCTARobot();
    }

})(project, _, $);
