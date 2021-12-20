const role = sessionStorage.getItem("role");
const id = sessionStorage.getItem("employeeId");

const url = "http://127.0.0.1:5000/"
const route = "manager/reimbursements/employee"
const approve = "/manager/approve/reimbursement"
const reject = "/manager/reject/reimbursement"

const home = document.getElementById("home");
const past = document.getElementById("past");
const logout = document.getElementById("logout");

const toMainPage = () => {
    location.href="../main_stat/manager_stat.html"
}

const toPastPage = () => {
    location.href="../past/manager_past.html"
}

const toLogout = () => {
    sessionStorage.clear();
    location.href="../../login/index.html";
}

home.addEventListener("click", toMainPage);
past.addEventListener("click", toPastPage);
logout.addEventListener("click", toLogout);

const loadPending = async () => {
    const response = await fetch(url + route, {
        method: "GET",
        mode: "cors"
    });

    if (response.status == 200) {
        const reimJson = await response.json();
        createPendings(reimJson);
    }
    else {
        const body = await response.json();
    }
}

const createPendings = (reim_json) => {
    let tbody = document.getElementById("tableBody");
    let reimList = reim_json.reimbursements;
    reimList = filterList(reimList);
    console.log(reimList)
    
    for (reim of reimList) {
        tbody.insertRow().innerHTML = createRow(reim);
        addEvents(reim.reimId);
    }
}

const filterList = (reimList) => {
    let resultList = [];
    for (reim of reimList){
        if (reim.status === "pending"){
            resultList.push(reim);
        }
    }
    return resultList;
}

const createRow = (reim) => {
    return createTd(
        reim.employeeId,
        reim.reimAmount,
        reim.reimReason,
        reim.submittedDate,
        reim.reimId
    );
}

const createTd = (id, amount, reason, date, reimId) => {
    return `<td class="center">`+ id +`</td>
    <td class="center">$ `+ amount + `</td>
    <td class="center">`+ reason + `</td>
    <td class="center">`+ date + `</td>
    <td class="center">
    <input id="` + reimId + `t" type="text">
    </td>
    <td class="center">
    <button id="` + reimId + `a" class="btn btn-success btn-w">approve</button>
    <button id="` + reimId + `r" class="btn btn-danger btn-w">reject</button>
    </td>`;
}

const addEvents = (id) => {
    let aButton = document.getElementById(id + "a");
    let rButton = document.getElementById(id + "r");
    let text = document.getElementById(id + "t").textContent;
    aButton.addEventListener("click", approveReim);
    rButton.addEventListener("click", rejectReim);
}
const approveReim = async (e) => {
    let btnId = e.target.id.substring(0, e.target.id.length-1);
    let text = document.getElementById(btnId+"t").value
    let bodyContent = {
        reimId: btnId,
        comment: text,
        status: "pending"
    }
    const response = await fetch(url + approve, {
        method: "POST",
        mode: "cors",
        body: JSON.stringify(bodyContent),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    });
    if (response.status === 200){
        let p = document.getElementById(btnId+"t").parentNode.parentNode;
        p.parentNode.removeChild(p);
        processResult("Request processed successfully", true);
    }
    else {
        processResult("Error processing request", false);
    }
}

const rejectReim = async (e) => {
    let btnId = e.target.id.substring(0, e.target.id.length-1);
    let text = document.getElementById(btnId+"t").value;
    let bodyContent = {
        reimId: btnId,
        comment: text,
        status: "pending"
    }
    const response = await fetch(url + reject, {
        method: "POST",
        mode: "cors",
        body: JSON.stringify(bodyContent),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    });
    if (response.status === 200){
        let p = document.getElementById(btnId+"t").parentNode.parentNode;
        p.parentNode.removeChild(p);
        processResult("Request processed successfully", true);
    }
    else {
        processResult("Error processing request", false);
    }
}


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

loadPending();
