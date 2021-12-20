const url = "http://127.0.0.1:5000/"
const route = "login"
const submitBtn = document.getElementById('submitBtn');
sessionStorage.clear();

let counter = 0;

const loginFailed = (errorMessage) => {
    const div = document.getElementById("formContainer")
    const message = document.createElement("p");
    message.setAttribute("id", "loginFailed");
    message.textContent = errorMessage;
    div.appendChild(message);
    document.body.appendChild(div);
}

const requestLogin = async () => {
    const id = document.getElementById("userId");
    const pw = document.getElementById("userPw");

    const credential = { loginId: id.value, loginPw: pw.value }

    const response = await fetch(url + route, {
        method: "POST",
        mode: "cors",
        body: JSON.stringify(credential),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    });

    if (response.status === 200) {
        const body = await response.json();
        sessionStorage.setItem("employeeId", body.employeeId);
        sessionStorage.setItem("role", body.role);
        const role = sessionStorage.getItem("role");
        if (role === "employee") {
            location.href = "../employee/main/employee_main.html";

        }
        else if (role === "manager") {
            location.href = "../manager/main_stat/manager_stat.html";
        }
        else {
            loginFailed("Something is not quite right");
        }
    }
    else {
        const body = await response.json();
        console.log(body);
        if (counter === 0) {
            loginFailed("* " + body.errorMessage + " *");
            counter++;
        }
    }
    id.value = "";
    pw.value = "";
}

submitBtn.addEventListener("click", requestLogin);

document.getElementById('userId').onkeydown = function (e) {
    if (e.keyCode === 13) {
        requestLogin();
    }
};

document.getElementById('userPw').onkeydown = function (e) {
    if (e.keyCode === 13) {
        requestLogin();
    }
};

