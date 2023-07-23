function navAlign() {
    var element = document.getElementById('navbarNav');
    if (window.innerWidth <= 992) {
        element.classList.remove('justify-content-end');
        element.classList.add('justify-content-center');
    } else {
        element.classList.remove('justify-content-center');
        element.classList.add('justify-content-end');
    }
};

window.addEventListener('resize', () => {
    var element = document.getElementById('navbarNav');
    if (window.innerWidth <= 992) {
        element.classList.remove('justify-content-end');
        element.classList.add('justify-content-center');
    } else {
        element.classList.remove('justify-content-center');
        element.classList.add('justify-content-end');
    }
})
window.onload = navAlign();

let toTopBtn = document.getElementById('scroll-to-top');
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
    if (document.documentElement.scrollTop > 20 || document.body.scrollTop >20) {
        toTopBtn.style.display = "block";
    } else {
        toTopBtn.style.display = "none";
    }
}

toTopBtn.addEventListener('click', () => {
    window.scrollTo({
        top: 0
    })
})

//enable popover
const popoverTriggerList = document.querySelectorAll('[data-bs-toggle="popover"]')
const popoverList = [...popoverTriggerList].map(popoverTriggerEl => new bootstrap.Popover(popoverTriggerEl))