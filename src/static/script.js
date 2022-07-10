"use strict";

const donwload_btn = document.querySelector(".btn-download");
donwload_btn.onclick = () => {
    let params = [];
    let selected_tweaks = document.querySelectorAll("*[selected-tweak]");
    for (const tweak of selected_tweaks) {
        params.push(tweak.getAttribute("tweak-name"));
    }

    let link = "/download?" + params.join("&");
    location.href = link;
}

const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]');
const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl));


const tweak_btns = document.querySelectorAll(".tweak .btn");
for (const btn of tweak_btns) {
    btn.onclick = () => {
        if (!btn.hasAttribute("selected-tweak")) {
            btn.setAttribute("selected-tweak", "");
            btn.classList.remove("btn-outline-danger");
            btn.classList.add("btn-success");
            btn.innerHTML = '<i class="bi bi-check-lg flex-shrink-0 me-2"></i>Enabled';
        }
        else {
            btn.removeAttribute("selected-tweak");
            btn.classList.add("btn-outline-danger");
            btn.classList.remove("btn-success");
            btn.innerHTML = '<i class="bi bi-x-lg flex-shrink-0 me-2"></i>Disabled';
        }
    }
}
