const verifiedNGOs = [
  {
    name: "Helping Hands Foundation",
    darpanId: "MH/2021/0123456"
  },
  {
    name: "Seva Trust",
    darpanId: "DL/2020/0098765"
  },
  {
    name: "Udaan NGO",
    darpanId: "KA/2019/0043210"
  }
];

let generatedOTP = null;

function showForm(type) {
  document.getElementById("ngoForm").classList.remove("active");
  document.getElementById("donorForm").classList.remove("active");

  document.querySelectorAll(".tab").forEach(tab => tab.classList.remove("active"));

  if (type === "ngo") {
    document.getElementById("ngoForm").classList.add("active");
    document.querySelectorAll(".tab")[0].classList.add("active");
  } else {
    document.getElementById("donorForm").classList.add("active");
    document.querySelectorAll(".tab")[1].classList.add("active");
  }
}

function isValidDarpanId(darpanId) {
  const darpanPattern = /^[A-Z]{2}\/\d{4}\/\d{7}$/;
  return darpanPattern.test(darpanId);
}


// Mock OTP system
function sendOTP() {
  const contact = document.getElementById("donorContact").value;
  if (!contact) {
    alert("Please enter mobile number or email");
    return;
  }
  generatedOTP = Math.floor(100000 + Math.random() * 900000);
  alert("OTP sent successfully!\n(Mock OTP: " + generatedOTP + ")");
}

// NGO Login Submit
document.getElementById("ngoForm").addEventListener("submit", function (e) {
  e.preventDefault();

  const ngoName = document.getElementById("ngoName").value.trim();
  const darpanId = document.getElementById("darpanId").value.trim();
  const statusText = document.getElementById("ngoStatus");

  // Step 1: Format validation
  if (!isValidDarpanId(darpanId)) {
    statusText.style.color = "red";
    statusText.innerText = "❌ Invalid DARPAN ID format";
    return;
  }

  // Step 2: Verify against database
  const ngoFound = verifiedNGOs.find(
    ngo => ngo.darpanId === darpanId
  );

  if (!ngoFound) {
    statusText.style.color = "red";
    statusText.innerText = "❌ NGO not found in DARPAN database";
    return;
  }

  // Step 3: Successful authentication
  statusText.style.color = "green";
  statusText.innerText = "✅ NGO verified successfully via DARPAN";

  setTimeout(() => {
    alert(`Welcome ${ngoFound.name}! NGO login successful.`);
  }, 500);
});


// Donor Login Submit
document.getElementById("donorForm").addEventListener("submit", function (e) {
  e.preventDefault();
  const enteredOTP = document.getElementById("otpInput").value;

  if (enteredOTP == generatedOTP) {
    alert("Donor login successful!");
  } else {
    alert("Invalid OTP");
  }
});
