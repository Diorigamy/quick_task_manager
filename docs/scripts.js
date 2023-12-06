/*JavaScript*/
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();

        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

let slideIndex = 0;

function showSlides() {
    let slides = document.getElementsByClassName("demo-image");
    for (let i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    slideIndex++;
    if (slideIndex > slides.length) {
        slideIndex = 1;
    }
    slides[slideIndex - 1].style.display = "block";
    setTimeout(showSlides, 2000); // Change slide every 2 seconds
}

showSlides();

document.querySelectorAll('.team-member').forEach(member => {
    member.addEventListener('click', function () {
        this.classList.toggle('active');
    });
});

document.querySelector('footer p').innerHTML += new Date().getFullYear();
