function toggleMenu() {
  document.getElementById("navLinks").classList.toggle("active");
}

/* SCROLL REVEAL (STAGGERED) */
const revealItems = document.querySelectorAll(".process-card, .trust-card");

const observer = new IntersectionObserver(
  entries => {
    entries.forEach((entry, index) => {
      if (entry.isIntersecting) {
        setTimeout(() => {
          entry.target.style.opacity = "1";
          entry.target.style.transform = "translateY(0)";
        }, index * 120);
      }
    });
  },
  { threshold: 0.2 }
);

revealItems.forEach(item => observer.observe(item));
