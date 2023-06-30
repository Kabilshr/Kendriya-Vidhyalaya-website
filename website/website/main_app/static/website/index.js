let toTopBtn = document.getElementById('scroll-to-top');
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
    if (document.documentElement.scrollTop > 20 || document.body.scrollTop >20) {
        toTopBtn.style.display = "block";
    } else {
        toTopBtn.style.display = "none";
    }
}

function scrollTop() {
    document.body.scrollTop = 0;//Safari
    document.documentElement.scrollTop = 0;//Chrome, Firefox, Opera
}

toTopBtn.addEventListener('click', () => {
    window.scrollTo({
        top: 0
    })
})

//enable popover
const popoverTriggerList = document.querySelectorAll('[data-bs-toggle="popover"]')
const popoverList = [...popoverTriggerList].map(popoverTriggerEl => new bootstrap.Popover(popoverTriggerEl))