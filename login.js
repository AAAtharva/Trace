const donorBtn = document.getElementById("donorBtn");
const ngoBtn = document.getElementById("ngoBtn");
const slider = document.querySelector(".slider");

const donorForm = document.getElementById("donorForm");
const ngoForm = document.getElementById("ngoForm");

donorBtn.onclick = () => {
  donorBtn.classList.add("active");
  ngoBtn.classList.remove("active");
  slider.style.left = "4px";
  donorForm.classList.add("active");
  ngoForm.classList.remove("active");
};

ngoBtn.onclick = () => {
  ngoBtn.classList.add("active");
  donorBtn.classList.remove("active");
  slider.style.left = "50%";
  ngoForm.classList.add("active");
  donorForm.classList.remove("active");
};


