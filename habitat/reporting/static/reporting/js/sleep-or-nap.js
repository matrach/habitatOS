(function($) {
    $(document).ready(function() {

        function showHideSleepReport() {
            var nap = document.getElementById('id_type_1');

            if (nap.checked) {
               $('.sleep-report').hide();
            } else {
               $('.sleep-report').show();
            }
        }

        var type = document.getElementById('id_type');
        type.addEventListener("click", showHideSleepReport);

        showHideSleepReport();

    });
})(django.jQuery);
