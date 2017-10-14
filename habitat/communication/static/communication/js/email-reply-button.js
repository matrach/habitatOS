document.addEventListener("DOMContentLoaded", function(event) {

    var id = document.querySelectorAll('div[class~="id"] div.grp-readonly')[0].innerText;

    if (Number.isInteger(parseInt(id))) {
        var button = '<li><a href="/communication/email/add/?reply_to='+ id +'">Reply</a></li>';
        var list = document.querySelector('ul.grp-object-tools');
        list.insertAdjacentHTML('afterbegin', button);
    }

});
