// center nav bar content according to screen size
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

// scroll animations
const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        console.log(entry);
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

//use scroll wheel to navigate events
// slider.addEventListener('wheel', (e) => {
//     e.preventDefault();
//     slider.scrollLeft += e.deltaY;
// });

// function snapToNearestSlide() {
//     const slideWidth = slider.offsetWidth;
//     const slideIndex = Math.round(slider.scrollLeft / slideWidth);
//     const scrollToX = slideIndex * slideWidth;
//     // slider.scrollTo({
//     //     left: scrollToX,
//     //     behavior: 'smooth',
//     // });
// }

// scroll animation
// const boxes = document.querySelectorAll('.scroll');
// const observerOptions = {
//     root: null,
//     rootMargin: '0px',
//     threshold: 0.5 // When 50% of the element is visible
// };

// function handleIntersect(entries, observer) {
//     entries.forEach(entry => {
//         if (entry.isIntersecting) {
//             entry.target.classList.add('fade-in-up');
//             observer.unobserve(entry.target);
//         }
//     });
// }

// const animateObserver = new IntersectionObserver(handleIntersect, observerOptions);

// boxes.forEach(box => {
//     observer.observe(box);
// });


//enable popover
const popoverTriggerList = document.querySelectorAll('[data-bs-toggle="popover"]')
const popoverList = [...popoverTriggerList].map(popoverTriggerEl => new bootstrap.Popover(popoverTriggerEl))