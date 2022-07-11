"use strict";

const ICON_CHECK_LG = '<i class="bi bi-check-lg flex-shrink-0 me-2"></i>';
const ICON_X_LG = '<i class="bi bi-x-lg flex-shrink-0 me-2"></i>';


// Download
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

// Buttons
const tweak_btns = document.querySelectorAll(".tweak .btn");
for (const btn of tweak_btns) {
    btn.onclick = () => {
        if (!btn.hasAttribute("selected-tweak")) {
            btn.setAttribute("selected-tweak", "");
            btn.classList.remove("btn-outline-danger");
            btn.classList.add("btn-success");
            btn.innerHTML = `${ICON_CHECK_LG}Enabled`;
        }
        else {
            btn.removeAttribute("selected-tweak");
            btn.classList.add("btn-outline-danger");
            btn.classList.remove("btn-success");
            btn.innerHTML = `${ICON_X_LG}Disabled`;
        }
    }
}
