// EduGenie Frontend Script

document.addEventListener("DOMContentLoaded", () => {

    console.log("EduGenie Loaded Successfully");

    const form = document.querySelector("form");

    if (form) {

        form.addEventListener("submit", () => {

            const button = document.querySelector("button");

            button.disabled = true;

            button.innerHTML = "Generating...";

        });

    }

});


function showLoading() {

    const resultBox = document.getElementById("result");

    if (resultBox) {

        resultBox.innerHTML = `
            <div style="padding:20px;">
                Generating response...
            </div>
        `;
    }
}


function copyResult() {

    const result = document.getElementById("result");

    if (!result) return;

    navigator.clipboard.writeText(result.innerText)
        .then(() => {

            alert("Result copied successfully!");

        })
        .catch(() => {

            alert("Copy failed!");

        });

}


function clearInput() {

    const textarea = document.querySelector("textarea");

    if (textarea) {

        textarea.value = "";

    }

}


function resetForm() {

    const form = document.querySelector("form");

    if (form) {

        form.reset();

    }

}