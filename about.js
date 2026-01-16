/* MOBILE MENU */
function toggleMenu() {
  document.getElementById("navLinks").classList.toggle("active");
}

/* NAVBAR SCROLL */
window.addEventListener("scroll", () => {
  document.getElementById("nav")
    .classList.toggle("scrolled", window.scrollY > 50);
});

/* ACTIVE LINK */
document.querySelectorAll(".nav-links a").forEach(link => {
  if (link.href === window.location.href) {
    link.classList.add("active");
  }
});

/* SCROLL REVEAL */
const reveals = document.querySelectorAll(".reveal");

const observer = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add("active");
    }
  });
}, { threshold: 0.2 });

reveals.forEach(el => observer.observe(el));
