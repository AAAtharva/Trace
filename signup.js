/* SLIDE TOGGLE */
const sliderPanel = document.querySelector(".form-slider");
document.getElementById("donorBtn").onclick = () => {
  sliderPanel.style.transform = "translateX(0)";
};
document.getElementById("ngoBtn").onclick = () => {
  sliderPanel.style.transform = "translateX(-50%)";
};

/* OTP MOCK */
let generatedOTP = null;

function sendOTP() {
  generatedOTP = Math.floor(100000 + Math.random() * 900000);
  document.getElementById("otpStatus").textContent =
    "OTP sent successfully (demo)";
  document.getElementById("otpStatus").className = "success";
  console.log("OTP (demo):", generatedOTP);
}

/* DARPAN AI CHECK (MOCK) */
function validateDarpan() {
  const id = document.getElementById("darpanId").value;
  const status = document.getElementById("darpanStatus");

  if (id.length < 10) {
    status.textContent = "Invalid DARPAN ID";
    status.className = "error";
  } else {
    status.textContent = "DARPAN ID verified ✓";
    status.className = "success";
  }
}

/* INDIA STATE / DISTRICT DATA */
const indiaData = {
  Maharashtra: ["Pune", "Mumbai"],
  Karnataka: ["Bangalore Urban", "Mysuru"],
  Delhi: ["Central Delhi", "South Delhi"]
};

function handleCountryChange() {
  const country = document.getElementById("ngoCountry").value;
  const state = document.getElementById("ngoState");
  const district = document.getElementById("ngoDistrict");

  state.innerHTML = "<option value=''>State</option>";
  district.innerHTML = "<option value=''>District</option>";

  if (country === "India") {
    state.style.display = "block";
    district.style.display = "block";

    Object.keys(indiaData).forEach(s => {
      state.innerHTML += `<option>${s}</option>`;
    });

    state.onchange = () => {
      district.innerHTML = "<option value=''>District</option>";
      indiaData[state.value].forEach(d =>
        district.innerHTML += `<option>${d}</option>`
      );
    };
  } else {
    state.style.display = "none";
    district.style.display = "none";
  }
}

/* AI FORM CHECK */
document.querySelectorAll("form").forEach(form => {
  form.onsubmit = e => {
    e.preventDefault();
    alert("Account created successfully (demo)");
  };
});

/* BACK */
function goBack() {
  document.referrer
    ? (window.location.href = document.referrer)
    : (window.location.href = "index.html");
}
