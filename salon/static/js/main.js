
$(function() {
    setTimeout(function(){
         $('.preloader').fadeOut();
        }, 2000);
});

function scrollDelay(offset){
    offset = Math.round(offset);
    let targetOffset = Math.max(pageYOffset, offset) - Math.min(pageYOffset, offset);
    return Math.round(Math.pow(targetOffset, 0.89));
}
$(document).ready(
    function($) {
        $('.carousel').carousel({interval: 3000});

        $('.loop').owlCarousel({
            center: true,
            items: 3,
            autoWidth:true,
            // stagePadding: 75,
            loop: true,
            margin: 7,

            responsive: {
                0: {
                    items: 1
                },
                700: {
                    items: 2
                }
            }
        });

        $('#form-phone').usPhoneFormat();
        function scrollToSection(event) {
            event.preventDefault();
            let $section = $($(this).attr('href'));
            $('html, body').animate({scrollTop: $section.offset().top - 75}, scrollDelay($section.offset().top));
        }
        $('[data-scroll]').on('click', scrollToSection);
    }(jQuery)
);
$(function() {
    $('form').submit(function(e) {
        let $form = $(this);
        $.ajax({
            type: $form.attr('method'),
            url: $form.attr('action'),
            data: $form.serialize(),
            dataType: 'json'
        }).done(function(data) {
            console.log(data.message);
            console.log('success');
        }).fail(function(data) {
            console.log(data);
            console.log('fail');
        });
        e.preventDefault();
    });
});

new WOW().init();