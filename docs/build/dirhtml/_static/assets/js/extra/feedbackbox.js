$(document).ready(function() {
    if ($('#fbb_float').length > 0) {
        // Feedback Box
        $('#fbb_float').click(function(e) {
            $('#fbb_window').css('max-height', 'none');
            $('#fbb_float').hide()
            e.stopPropagation();
        });

        $('.fbb_window_btn_close').click(function(e) {
            $('#fbb_window').css('max-height', '0');
            $('#fbb_float').show()
            e.stopPropagation();
        });
        $(document).click(function(e){
            if ($(e.target).parents(".fbb_window_inner").length === 0) {
                $('#fbb_window').css('max-height', '0');
                $('#fbb_float').show()
            }
        });
    }
});
