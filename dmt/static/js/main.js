$('a[href*="#"]')
.not('[href="#"]')
.not('[href="#0"]')
.click(function(event) {
    if (
    location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') 
    && 
    location.hostname == this.hostname
    ) {
        var target = $(this.hash);
        target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
        if (target.length) {
            event.preventDefault();
            $('html, body').animate({
            scrollTop: target.offset().top
            }, 500, function() {
            var $target = $(target);
            $target.focus();
            if ($target.is(":focus")) {
                return false;
            } else {
                $target.attr('tabindex','-1'); 
                $target.focus(); 
            };
            });
        }
    }
});
$(document).ready(function() {
    $('.actors_slider').slick({
        focusOnSelect: false,
        slidesToShow: 4,
        rows: 2,
        infinite: false,
        arrows: true,
        prevArrow: '.actors-prev',
        nextArrow: '.actors-next',
        dots: true,
        responsive: [{

            breakpoint: 1024,
            settings: {
                slidesToShow: 4,
            }

            }, {

            breakpoint: 993,
            settings: {
                slidesToShow: 2,
                
            }

            }, {

            breakpoint: 300,
            settings: {
                slidesToShow: 2,
            }

        }]
    });
    $('.repertoire__cards').slick({
        focusOnSelect: false,
        slidesToShow: 2,
        infinite: false,
        arrows: true,
        prevArrow: '.repertoire-prev',
        nextArrow: '.repertoire-next',
        dots: true,
        responsive: [{
            breakpoint: 769,
                settings: {
                    slidesToShow: 1,
                }

            }]
    });
});
$(window).on('resize', function() {
    if (window.innerWidth <= 767 && ($(".nav").css("display") == "flex") && $(".nav").attr("dmt-menu-status") != "active") {
        $(".nav").css("display", "none");
    }
    else if (window.innerWidth > 767 && ($(".nav").css("display") == "flex") && $(".nav").attr("dmt-menu-status") == "active") {
        $(".nav").attr({"dmt-menu-status": "hidden"});
        $(".nav__close-btn").fadeOut(0);
        $(document.body).css({"overflow": "auto", "height": "auto"});
    }
    else if (window.innerWidth > 767 && ($(".nav").css("display") == "none") && ($(".nav").attr("dmt-menu-status") == "hidden")) {
        $(".nav").css("display", "flex");
    };
});
// Открытие полноэкранного меню на устройствах с шириной меньше 767px
$(".menu-icon").click(function(e){
    if (window.innerWidth <= 767) {
        e.preventDefault();
        $(".nav").attr({"dmt-menu-status": "active"}).css("display", "flex").hide().fadeIn();
        $(".nav__close-btn").fadeIn();
        $(document.body).css({"overflow": "hidden", "height": "100%"});
    }
});
$(".nav__close-btn, .nav__link").click(function(e){
    if (window.innerWidth <= 767) {
        e.preventDefault();
        $(".nav").attr({"dmt-menu-status": "hidden"}).fadeOut();
        $(".nav__close-btn").fadeOut();
        $(document.body).css({"overflow": "auto", "height": "auto"});
    }
});
function validate() {
    setTimeout(function() {
      $( "#subscribe" ).removeClass( "btn-subscribe" );
      $( "#subscribe" ).addClass( "btn-success", 450, callback );
    }, 2250 );
  }
function callback() {
    setTimeout(function() {
        $("#subscribe").removeClass( "btn-success" );
        $("#subscribe").addClass( "btn-subscribe");
    }, 1250 );
}
$(document).on('submit', '#mailing__form', function(e) {
    e.preventDefault();
    $( "#subscribe" ).prop( "disabled", true );
    $( "#subscribe" ).empty().append('<i class="fas fa-circle-notch fa-spin"></i>');
    $.ajax({
        type:'POST',
        url: $('#mailing__form').attr('data-url'),
        data: {
            name: $('#mailing__form-name').val(),
            email: $('#mailing__form-email').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            action: 'post'
        },
        success: function(json){
            if (json.success) {
                document.getElementById("mailing__form").reset();
                $('.mailing__form-errors').empty();
                $( "#subscribe" ).empty().toggleClass(["btn-subscribe", "btn-success"]);
                setTimeout(function() {
                    $( "#subscribe" ).toggleClass(["btn-subscribe", "btn-success"]).append('подписаться');
                }, 1500 );
            }
            else {
            }
        },
        error : function(xhr,errmsg,err) {
            $('.mailing__form-errors').empty();
            var json = $.parseJSON(xhr.responseText);
            var fields_name = ['name', 'email'];
            for (var field in json.form_errors) {   
                for (var j = 0; j < json.form_errors[field].length; j++) {
                    $('#mailing__form-' + field + '__errors').append('<li>' + json.form_errors[field][j].message + '</li>');
                    $( "#subscribe" ).empty().append('подписаться');
                };
            };
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        },
    });
    $( "#subscribe" ).prop( "disabled", false );
});
$(window).on('load', function() {
    $('.repertoire__description').each(function(){
        if ($(this).get(0).scrollHeight != $(this).get(0).clientHeight) {
            $(this).after('<a class="more t-white" href="">читать далее</a>')
        }
    });
    $('.flex-text').on('click', '.more', function(e) {
        e.preventDefault();
        var description = $(this).parent().children('.repertoire__description');
        if ($(this).text() != 'скрыть') {
                description.animate({height: description.get(0).scrollHeight});
                $(this).text("скрыть");
        }
        else {
            description.animate({height: "63px"});
            $(this).text("читать далее");
        }
    });
    var resizeTimer;
    $(window).on('resize', function() { 
        clearTimeout(resizeTimer);
        resizeTimer = setTimeout(function() {
            $('.repertoire__description').each(function(index){
                console.log('Элемент №' + index + ', высота - ' + $(this).get(0).scrollHeight + ', вся высота - ' + $(this).get(0).clientHeight + ', ссылка - ' + !$(this).next('.more').length);
                if (($(this).get(0).scrollHeight != $(this).get(0).clientHeight) && !$(this).next('.more').length) {
                    $(this).after('<a class="more t-white" href="">читать далее</a>');
                    console.log('добавлена ссылка: Элемент №' + index + ', высота - ' + $(this).get(0).scrollHeight + ', вся высота - ' + $(this).get(0).clientHeight + ', ссылка - ' + !$(this).next('.more').length);
                }
                else if (($(this).get(0).scrollHeight == $(this).get(0).clientHeight) && $(this).next('.more').length) {
                    $(this).next('.more').remove();
                    console.log('ссылка удалена: Элемент №' + index + ', высота - ' + $(this).get(0).scrollHeight + ', вся высота - ' + $(this).get(0).clientHeight + ', ссылка - ' + !$(this).next('.more').length);
                }
            }); 
        }, 250);
    })
});