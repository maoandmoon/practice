function scrollDelay(offset){
    offset = Math.round(offset);
    let targetOffset = Math.max(pageYOffset, offset) - Math.min(pageYOffset, offset);
    return Math.round(Math.pow(targetOffset, 0.89));
}
$(document).ready(
    function($) {
        $('.carousel').carousel({interval: 3000});
        $('#form-phone').usPhoneFormat();
        function scrollToSection(event) {
            event.preventDefault();
            var $section = $($(this).attr('href'));
            $('html, body').animate({scrollTop: $section.offset().top - 75}, scrollDelay($section.offset().top));
        }
        $('[data-scroll]').on('click', scrollToSection);
    }(jQuery)
);
new WOW().init();