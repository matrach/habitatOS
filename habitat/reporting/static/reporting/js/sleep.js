(function($) {
    $(document).ready(function() {

        var type = document.getElementById('id_type');
        var nap = document.getElementById('id_type_1');

        type.addEventListener("click", function() {

            if (nap.checked) {
               $('.sleep-report').hide();
            } else {
               $('.sleep-report').show();
            }

        });




    });
})(django.jQuery);
