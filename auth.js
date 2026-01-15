async function login() {
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;

  const res = await apiRequest("/auth/login", "POST", { email, password });

  if (res.token) {
    localStorage.setItem("token", res.token);
    window.location.href = "dashboard.html";
  } else {
    document.getElementById("loginError").innerText = res.message;
  }
}

function logout() {
  localStorage.removeItem("token");
  window.location.href = "login.html";
}

function checkAuth() {
  if (!localStorage.getItem("token")) {
    window.location.href = "login.html";
  }
}
