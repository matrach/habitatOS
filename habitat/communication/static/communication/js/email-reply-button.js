(function($) {

    var id = $('div[class~="id"] div.grp-readonly').innerHTML;
    var button = '<li><a href="/communication/email/add/?reply_to='+ id +'/">Reply</a></li>';

    if (id)
        $('ul.grp-object-tools').prepend(button);

})(django.jQuery);
