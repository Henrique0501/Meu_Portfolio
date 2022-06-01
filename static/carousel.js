const sliders = document.querySelector('.carousel-content')
var scrollPerClick;
var ImagePadding = -2;

showMovieData()

var scrollAmount = 0;

function sliderScrollLeft() {
    sliders.scrollTo({
        top: 0,
        left: (scrollAmount -= scrollPerClick),
        behavior: "smooth",
    });

    if(scrollAmount < 0) {
        scrollAmount = 0;
    }
}

function sliderScrollRight() {
    if(scrollAmount <= sliders.scrollWidth - sliders.clientWidth){
        sliders.scrollTo({
            top: 0,
            left: (scrollAmount += scrollPerClick),
            behavior: "smooth",
    });
}
}

async function showMovieData() {
    scrollPerClick = document.querySelector('.first').clientWidth + ImagePadding;
}