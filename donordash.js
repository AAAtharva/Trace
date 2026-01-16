/* MOBILE NAV */
function toggleMenu() {
  document.getElementById("navLinks").classList.toggle("active");
}

/* TABS */
document.querySelectorAll(".tab").forEach(tab => {
  tab.onclick = () => {
    document.querySelectorAll(".tab").forEach(t => t.classList.remove("active"));
    document.querySelectorAll(".tab-content").forEach(c => c.classList.remove("active"));

    tab.classList.add("active");
    document.getElementById(tab.dataset.tab).classList.add("active");
  };
});

/* COUNTER */
document.querySelectorAll(".counter").forEach(counter => {
  const target = +counter.dataset.target;
  let current = 0;

  const update = () => {
    current += Math.ceil(target / 50);
    counter.innerText = current >= target ? target : current;
    if (current < target) requestAnimationFrame(update);
  };
  update();
});

/* SCROLL REVEAL */
const observer = new IntersectionObserver(entries => {
  entries.forEach(e => e.isIntersecting && e.target.classList.add("active"));
}, { threshold: 0.2 });

document.querySelectorAll(".reveal").forEach(el => observer.observe(el));

/* DJANGO API */
fetch("/api/donor/overview/")
  .then(res => res.json())
  .then(data => {
    document.querySelectorAll(".counter")[0].dataset.target = data.total_donated;
    document.querySelectorAll(".counter")[1].dataset.target = data.ngos_supported;
  });
