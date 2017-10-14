(function($) {
    $(document).ready(function() {

        function showHideSleepInterrupts() {
            var interrupted = document.getElementById('id_sleep_interrupted_1');

            if (interrupted.checked) {
               $('.sleep-interruptions').show();
            } else {
               $('.sleep-interruptions').hide();
            }
        }

        var sleep_interrupted = document.getElementById('id_sleep_interrupted');
        sleep_interrupted.addEventListener("click", showHideSleepInterrupts);

        showHideSleepInterrupts();

    });
})(django.jQuery);
