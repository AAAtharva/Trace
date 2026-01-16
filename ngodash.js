document.addEventListener("DOMContentLoaded", () => {

  const tabs = document.querySelectorAll(".tab");
  const contents = document.querySelectorAll(".tab-content");

  tabs.forEach(tab => {
    tab.onclick = () => {
      tabs.forEach(t => t.classList.remove("active"));
      contents.forEach(c => c.classList.remove("active"));
      tab.classList.add("active");
      document.getElementById(tab.dataset.tab).classList.add("active");
    };
  });

  const ctx = document.getElementById("growthChart");
  if (ctx) {
    new Chart(ctx, {
      type: "line",
      data: {
        labels: ["Jan","Feb","Mar","Apr","May","Jun"],
        datasets: [{
          data: [10,20,35,55,80,120],
          borderColor: "#1b7a5a",
          tension: 0.4
        }]
      }
    });
  }

  const modal = document.getElementById("proofModal");
  document.getElementById("openProofModal").onclick = () => modal.style.display = "flex";
  document.getElementById("closeProof").onclick = () => modal.style.display = "none";
});


fetch("/api/ngo/overview/")
  .then(res => res.json())
  .then(data => {
    document.getElementById("totalDonations").textContent = data.total_donations;
    document.getElementById("meritPoints").textContent = data.merit_points;
    document.getElementById("currentRank").textContent = `#${data.rank}`;
  });
