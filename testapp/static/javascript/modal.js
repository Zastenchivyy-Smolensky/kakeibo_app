"use strict";

{
  const open = document.getElementById("modal-open");
  const container = document.getElementById("modal-container");
  const modalBg = document.getElementById("modal-bg");
  const close = document.getElementById("modal-close");
  const submit = document.getElementById("submit");
  open.addEventListener("click", function () {
    container.classList.add("active");
    modalBg.classList.add("active");
  });
  close.addEventListener("click", function () {
    container.classList.remove("active");
    modalBg.classList.remove("active");
    modalBg.classList.remove("active");
  });
  modalBg.addEventListener("click", function () {
    container.classList.remove("active");
    modalBg.classList.remove("active");
  });
}
