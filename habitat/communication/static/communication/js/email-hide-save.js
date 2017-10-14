document.addEventListener("DOMContentLoaded", function(event) {

    var id = document.querySelectorAll('div[class~="id"] div.grp-readonly')[0].innerText;

    if (Number.isInteger(parseInt(id))) {
        var submitRow = document.querySelector(".submit-row");
        if (submitRow)
            submitRow.style.display = 'none';

        var footer = document.querySelector("footer");
        if (footer)
            footer.style.display = 'none'
     }

});
