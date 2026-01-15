const API_BASE = "http://localhost:5000/api";

async function apiRequest(endpoint, method = "GET", data = null) {
  const token = localStorage.getItem("token");

  const res = await fetch(API_BASE + endpoint, {
    method,
    headers: {
      "Content-Type": "application/json",
      "Authorization": token ? `Bearer ${token}` : ""
    },
    body: data ? JSON.stringify(data) : null
  });

  return res.json();
}
