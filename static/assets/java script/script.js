
$(document).ready(function () {
    $('.slider_main').owlCarousel({
        loop: true,
        margin: 10,
        autoplay: true,
        nav: true,
        dots: false,
        responsiveClass: true,
        responsive: {
            0: {
                items: 1,
                nav: true,
                stagePadding: 50,

            },
            600: {
                items: 1,
                nav: true,
                stagePadding: 150,
            },
            1000: {
                items: 1,
                stagePadding: 450,
                nav: true
            },
        }
    });

    $('.activity_body').owlCarousel({
        loop: true,
        center: true,
        margin: 10,
        autoplay: true,
        nav: true,
        dots: false,
        responsiveClass: true,
        navText: ["<i class='fa-solid fa-chevron-left'></i>", "<i class='fa-solid fa-chevron-right'></i>"],
        responsive: {
            0: {
                items: 1,
                nav: true,
            },
            600: {
                items: 2,
                nav: true,
            },
            1000: {
                items: 3,
                nav: true
            },
        }
    });

    $('.slider_box').owlCarousel({
        loop: true,
        center: true,
        margin: 10,
        autoplay: true,
        nav: true,
        dots: false,
        responsiveClass: true,
        navText: ["<i class='fa-solid fa-chevron-left'></i>", "<i class='fa-solid fa-chevron-right'></i>"],
        responsive: {
            0: {
                items: 1,
                nav: true,
            },
            600: {
                items: 2,
                nav: true,
            },
            1000: {
                items: 1,
                nav: true
            },
        }
    });
});

let nav = document.querySelector(".main_header");
window.onscroll = function () {
    if (document.documentElement.scrollTop > 50) {
        nav.classList.add("header");
    } else {
        nav.classList.remove("header");
    }
};

function startCounterAnimation() {
    var counterElement = document.getElementById('counter');
    var targetValue = parseInt(counterElement.innerText);
    var currentValue = 0;

    var interval = setInterval(function () {
        counterElement.innerText = ++currentValue;
        if (currentValue === targetValue) {
            clearInterval(interval);
        }
    }, 10);
}

window.addEventListener('scroll', function () {
    var element = document.querySelector('.counter_bg');
    var position = element.getBoundingClientRect();
    if (position.top >= 0 && position.bottom <= window.innerHeight) {
        startCounterAnimation();
    }
});

const links = document.querySelectorAll('.list_bg a');

links.forEach(link => {
    link.addEventListener('click', function (event) {
        links.forEach(link => {
            link.classList.remove('active');
        });
        this.classList.add('active');
    });
});

















