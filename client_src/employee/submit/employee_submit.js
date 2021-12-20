const role = sessionStorage.getItem("role");
const id = sessionStorage.getItem("employeeId");

const url = "http://127.0.0.1:5000/"
const route = "employee/reimbursement"

const main = document.getElementById("pending");
const past = document.getElementById("past");
const logout = document.getElementById("logout");

const submitBtn = document.getElementById("submitBtn");
const reasonInput = document.getElementById("reasonInput");
const amountInput = document.getElementById("amountInput");

const toMainPage = () => {
    location.href = "../main/employee_main.html"
}

const toPastPage = () => {
    location.href = "../past/employee_past.html"
}

const toLogout = () => {
    sessionStorage.clear();
    location.href = "../../login/index.html";
}

main.addEventListener("click", toMainPage);
past.addEventListener("click", toPastPage);
logout.addEventListener("click", toLogout);

const processResult = (message, status) => {
    if (document.getElementById("message")) {
        document.body.removeChild(document.getElementById("message"));
    }

    let div = document.createElement("div");
    div.setAttribute("id", "message");
    let p = document.createElement("p");

    if (status === true) {
        p.setAttribute("id", "success")
    }
    else if (status === false) {
        p.setAttribute("id", "fail")
    }
    p.innerHTML = "* " + message + " *"
    div.appendChild(p);
    document.body.appendChild(div);
}

const submitReim = async () => {
    let amount = amountInput.value;
    let reason = reasonInput.value;

    if (reason === "" ||
        isNaN(amount) ||
        amount <= 0 ||
        amount === "") {
        processResult("Submission Failed. Please make sure you have valid input", false);
    }
    else {
        let bodyContent = {
            employeeId: id,
            reimReason: reason,
            reimAmount: amount
        }

        const response = await fetch(url + route, {
            method: "POST",
            mode: "cors",
            body: JSON.stringify(bodyContent),
            headers: {
                "Content-type": "application/json; charset=UTF-8"
            }
        });

        if (response.status === 201) {
            const reimJson = await response.json();
            processResult("Submission Success", true);
        }
        else {
            const body = await response.json();
            processResult("Submission Failed. Check server status", false);
        }
    }
    reasonInput.value = "";
    amountInput.value = "";
}

submitBtn.addEventListener("click", submitReim);