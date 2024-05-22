$(function () {
    resize_tab();
});

$(window).resize(function () {
    resize_tab();
}).resize();

function resize_tab() {

    var viewportWidth = $(window).innerWidth();
    var viewportHeight = $(window).innerHeight();

    var width = $('#background_image').width();
    var height = $('#background_image').height();


    if ((viewportWidth / viewportHeight) > (width / height)) {

        $('#background_image').css ({
            'width': '100%',
            'height': 'auto',
            'margin-left': 0 - width / 2,
            'margin-top': 0 - height / 2
        });
    } else {
        $('#background_image').css ({
            'width': 'auto',
            'height': '100%',
            'margin-left': 0 - width / 2,
            'margin-top': 0 - height / 2
        });
    }
}