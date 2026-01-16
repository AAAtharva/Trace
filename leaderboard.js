
/* RESET COUNTDOWN */
function daysUntilReset() {
  const now = new Date();
  const reset = new Date(now.getFullYear(), now.getMonth() + 1, 1);
  return Math.ceil((reset - now) / (1000 * 60 * 60 * 24));
}

document.getElementById("resetDays").innerText = daysUntilReset();

/* SEARCH */
document.getElementById("searchNGO").addEventListener("input", e => {
  const value = e.target.value.toLowerCase();
  document.querySelectorAll(".table-row").forEach(row => {
    row.style.display = row.innerText.toLowerCase().includes(value)
      ? "grid"
      : "none";
  });
});

/* PROFILE MODAL (DEMO) */
function openProfile() {
  alert("NGO Profile Modal (demo)");
}
