"use strict";

const donwload_btn = document.querySelector(".btn-download");
donwload_btn.onclick = function (event) {
    let params = [];
    const checkboxes = document.querySelectorAll(".form-check-input");
    for (const checkbox of checkboxes) {
        if (checkbox.checked) {
            params.push(checkbox.id);
        }
    }

    let link = "/download?" + params.join("&");
    location.href = link;
}
