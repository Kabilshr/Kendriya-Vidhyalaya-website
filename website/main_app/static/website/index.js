// center nav bar content according to screen size
function navAlign() {
    var element = document.getElementById('navbarNav');
    if (window.innerWidth <= 1400) {
        element.classList.remove('justify-content-end');
        element.classList.add('justify-content-center');
    } else {
        element.classList.remove('justify-content-center');
        element.classList.add('justify-content-end');
    }
};

window.addEventListener('resize', () => {
    var element = document.getElementById('navbarNav');
    if (window.innerWidth <= 1200) {
        element.classList.remove('justify-content-end');
        element.classList.add('justify-content-center');
    } else {
        element.classList.remove('justify-content-center');
        element.classList.add('justify-content-end');
    }
})
window.onload = navAlign();

//scroll to top button
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

//date 
// Create a new Date object
var currentDate = new Date();

// Access the current date and time
var year = currentDate.getFullYear();
var month = currentDate.getMonth() + 1; // Months are zero-based (0 = January)
var day = currentDate.getDate();

var displayDate = day + " / " + month + " / " + year;

document.getElementById('date').innerHTML = displayDate;

// scroll animations
const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        if (entry.isIntersecting) {
            entry.target.classList.add('fade-in-up');
            observer.unobserve(entry.target);
        }
    });
},{
    threshold: 0.3 // animate after 30% of element is visible
});

const hiddenElements = document.querySelectorAll('.hidden'); // Corrected selector
hiddenElements.forEach((el) => observer.observe(el));

//event scroll
const slider = document.getElementById('event-container');
let isDown = false;
let startX;
let scrollLeft;

slider.addEventListener('mousedown', (e) => {
    isDown = true;
    startX = e.pageX - slider.offsetLeft;
    scrollLeft = slider.scrollLeft;
});

slider.addEventListener('touchstart', (e) => { // Touchstart event
    isDown = true;
    startX = e.touches[0].pageX - slider.offsetLeft;
    scrollLeft = slider.scrollLeft;
});

slider.addEventListener('mouseleave', () => {
    isDown = false;
});

slider.addEventListener('mouseup', () => {
    isDown = false;
    snapToNearestSlide();
});

slider.addEventListener('touchend', () => { // Touchend event
    isDown = false;
    snapToNearestSlide();
});

slider.addEventListener('mousemove', (e) => {
    if (!isDown) return;
    e.preventDefault();
    const x = e.pageX - slider.offsetLeft;
    const walk = (x - startX) * 3; // Adjust scroll speed as needed
    slider.scrollLeft = scrollLeft - walk;
});

slider.addEventListener('touchmove', (e) => { // Touchmove event
    if (!isDown) return;
    e.preventDefault();
    const x = e.touches[0].pageX - slider.offsetLeft;
    const walk = (x - startX) * 3; // Adjust scroll speed as needed
    slider.scrollLeft = scrollLeft - walk;
});

const eventContainer = document.getElementById('event-container')
function updateEventProgressBar(){
    const scrollTop = eventContainer.scrollLeft;
    const scrollWidth = eventContainer.scrollWidth;
    const scrollPercentage = scrollTop / (scrollWidth - eventContainer.clientWidth) * 100 + '%';
    
    document.querySelector('#progress-bar').style.setProperty('--progress-percent', scrollPercentage);
}

(eventContainer).addEventListener('scroll', updateEventProgressBar);

//enable popover
const popoverTriggerList = document.querySelectorAll('[data-bs-toggle="popover"]')
const popoverList = [...popoverTriggerList].map(popoverTriggerEl => new bootstrap.Popover(popoverTriggerEl))