const role = sessionStorage.getItem("role");
const id = sessionStorage.getItem("employeeId");

const url = "http://127.0.0.1:5000/"
const route = "employee/reimbursement/"

const submit = document.getElementById("submit");
const main = document.getElementById("pending");
const logout = document.getElementById("logout");

const toSubmitPage = () => {
    location.href = "../submit/employee_submit.html"
}

const toMainPage = () => {
    location.href = "../main/employee_main.html"
}

const toLogout = () => {
    sessionStorage.clear();
    location.href = "../../login/index.html";
}

submit.addEventListener("click", toSubmitPage);
main.addEventListener("click", toMainPage);
logout.addEventListener("click", toLogout);

const loadPast = async () => {
    const response = await fetch(url + route + id, {
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
    }
}

const filterList = (reimList) => {
    let resultList = [];
    for (reim of reimList) {
        if (reim.status !== "pending") {
            resultList.push(reim);
        }
    }
    return resultList;
}

const createRow = (reim) => {
    return createTd(
        reim.status,
        reim.submittedDate,
        reim.processedDate,
        reim.reimReason,
        reim.reimAmount,
        reim.managerComment
    );
}

const createTd = (status, subDate, proDate, reason, amount, comment) => {
    return `<td class="center">` + status + `</td>
    <td class="center">`+ subDate + `</td>
    <td class="center">`+ proDate + `</td>
    <td class="center">`+ reason + `</td>
    <td class="center">$ `+ amount + `</td>
    <td class="center">`+ comment + `</td>`;
}


const processFailed = () => {
    let div = document.createElement("div");
    let p = document.createElement("p");
    p.innerHTML = "* Error loading reimbursements *"
    div.appendChild(p);
    document.body.appendChild(div);
}

loadPast();