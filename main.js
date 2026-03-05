// DOM Elements
const audio = document.getElementById("audioPlayer");
const loader = document.getElementById("preloader");

// Settings Toggle Functionality
function settingtoggle() {
    document.getElementById("setting-container").classList.toggle("settingactivate");
    document.getElementById("visualmodetogglebuttoncontainer").classList.toggle("visualmodeshow");
    document.getElementById("soundtogglebuttoncontainer").classList.toggle("soundmodeshow");
}

// Sound Toggle Functionality
function playpause() {
    const soundSwitch = document.getElementById("switchforsound");
    if (!soundSwitch.checked) {
        audio.pause();
    } else {
        audio.play();
    }
}

// Visual Mode (Light/Dark) Toggle
function visualmode() {
    document.body.classList.toggle("light-mode");
    // Invert elements that need inversion in light mode (like specific icons or text)
    document.querySelectorAll(".needtobeinvert").forEach((el) => {
        el.classList.toggle("invertapplied");
    });
}

// Preloader & Initial Animations
window.addEventListener("load", () => {
    const isFirstLoad = !sessionStorage.getItem("siteLoaded");

    if (loader) {
        if (isFirstLoad) {
            // Show the cyber phonk loader for 2.5s then fade out
            setTimeout(() => {
                loader.classList.add("fade-out");
                sessionStorage.setItem("siteLoaded", "true");
                setTimeout(() => {
                    loader.style.display = "none";
                }, 800);
            }, 2500);
        } else {
            // Instant hide for subsequent loads in the same session
            loader.style.display = "none";
        }
    }

    const heyPopup = document.querySelector(".hey");
    if (heyPopup) {
        heyPopup.classList.add("popup");
    }
});

// Mobile Navigation Toggle
const emptyArea = document.getElementById("emptyarea");
const mobileTogglemenu = document.getElementById("mobiletogglemenu");

function hamburgerMenu() {
    document.body.classList.toggle("stopscrolling");
    document.getElementById("mobiletogglemenu").classList.toggle("show-toggle-menu");
    document.getElementById("burger-bar1").classList.toggle("hamburger-animation1");
    document.getElementById("burger-bar2").classList.toggle("hamburger-animation2");
    document.getElementById("burger-bar3").classList.toggle("hamburger-animation3");
}

function hidemenubyli() {
    document.body.classList.toggle("stopscrolling");
    document.getElementById("mobiletogglemenu").classList.remove("show-toggle-menu");
    document.getElementById("burger-bar1").classList.remove("hamburger-animation1");
    document.getElementById("burger-bar2").classList.remove("hamburger-animation2");
    document.getElementById("burger-bar3").classList.remove("hamburger-animation3");
}

// Active Nav Link on Scroll
const sections = document.querySelectorAll("section");
const navLi = document.querySelectorAll(".navbar .navbar-tabs .navbar-tabs-ul li");
const mobilenavLi = document.querySelectorAll(".mobiletogglemenu .mobile-navbar-tabs-ul li");

window.addEventListener("scroll", () => {
    let current = "";
    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        if (window.pageYOffset >= sectionTop - 200) {
            current = section.getAttribute("id");
        }
    });

    mobilenavLi.forEach(li => {
        li.classList.remove("activeThismobiletab");
        if (li.classList.contains(current)) {
            li.classList.add("activeThismobiletab");
        }
    });

    navLi.forEach(li => {
        li.classList.remove("activeThistab");
        if (li.classList.contains(current)) {
            li.classList.add("activeThistab");
        }
    });
});

console.log("%c Designed and Developed by Sanny Prajapati. ", "background-image: linear-gradient(90deg,#8000ff,#6bc5f8); color: white;font-weight:900;font-size:1rem; padding:20px;");

// Back to Top Button
const mybutton = document.getElementById("backtotopbutton");

function scrollFunction() {
    if (document.body.scrollTop > 400 || document.documentElement.scrollTop > 400) {
        if (mybutton) mybutton.style.display = "block";
    } else {
        if (mybutton) mybutton.style.display = "none";
    }
}

function scrolltoTopfunction() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}

window.addEventListener("scroll", scrollFunction);

// Prevent Right-Click on Images
document.addEventListener("contextmenu", (e) => {
    if (e.target.nodeName === "IMG") {
        e.preventDefault();
    }
}, false);

// Footer Eye Animation (Pupil tracking mouse)
const Pupils = document.getElementsByClassName("footer-pupil");
const pupilsArr = Array.from(Pupils);

const pupilStartPoint = -10;
const pupilRangeX = 20;
const pupilRangeY = 15;

let mouseXStartPoint = 0;
let mouseXEndPoint = window.innerWidth;
let currentXPosition = 0;
let fracXValue = 0;

let mouseYEndPoint = window.innerHeight;
let currentYPosition = 0;
let fracYValue = 0;

let mouseXRange = mouseXEndPoint - mouseXStartPoint;

const mouseMove = (e) => {
    currentXPosition = e.clientX - mouseXStartPoint;
    fracXValue = currentXPosition / mouseXRange;
    currentYPosition = e.clientY;
    fracYValue = currentYPosition / mouseYEndPoint;

    const t = pupilStartPoint + (fracXValue * pupilRangeX);
    const o = pupilStartPoint + (fracYValue * pupilRangeY);

    pupilsArr.forEach((pupil) => {
        pupil.style.transform = `translate(${t}px, ${o}px)`;
    });
};

const windowResize = () => {
    mouseXEndPoint = window.innerWidth;
    mouseYEndPoint = window.innerHeight;
    mouseXRange = mouseXEndPoint - mouseXStartPoint;
};

window.addEventListener("mousemove", mouseMove);
window.addEventListener("resize", windowResize);
