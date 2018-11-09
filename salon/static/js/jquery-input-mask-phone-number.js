(function ($) {
    $.fn.usPhoneFormat = function () {
            $(this).on('keypress', function (e) {
                if (e.which != 8 && e.which != 0 && (e.which < 48 || e.which > 57)) {
                    return false;
                }
                var curchr = this.value.length;
                var curval = $(this).val();
                if (curchr == 1 && e.which != 8 && e.which != 0 ) {
                    if (curval == 7 || curval == 8){
                        $(this).val("+7 (");
                    } else {
                        $(this).val("+7 (" + curval);
                    }
                }
                else if (curchr == 7 && e.which != 8 && e.which != 0) {
                    $(this).val(curval + ')' + " ");
                }
                else if (curchr == 12 && e.which != 8 && e.which != 0) {
                    $(this).val(curval + "-");
                }
                else if (curchr == 15 && e.which != 8 && e.which != 0) {
                    $(this).val(curval + "-");
                }
                $(this).attr('maxlength', '18');
            });
            $(this).bind('paste', function (e) {
                e.preventDefault();
                var inputValue = e.originalEvent.clipboardData.getData('Text');
                if (!$.isNumeric(inputValue)) {
                    return false;
                } else {
                    inputValue = String(inputValue.replace(/(\d)*(\d{3})(\d{3})(\d{2})(\d{2})/, "+7 ($2) $3-$4-$5"));
                    $(this).val(inputValue);
                    $(this).val('');
                    inputValue = inputValue.substring(0, 18);
                    $(this).val(inputValue);
                }
            });
        }
}(jQuery));