const role = sessionStorage.getItem("role");
const id = sessionStorage.getItem("employeeId");

const url = "http://127.0.0.1:5000/"
const route = "employee/reimbursement/"

const submit = document.getElementById("submit");
const past = document.getElementById("past");
const logout = document.getElementById("logout");

const toSubmitPage = () => {
    location.href="../submit/employee_submit.html"
}

const toPastPage = () => {
    location.href="../past/employee_past.html"
}

const toLogout = () => {
    sessionStorage.clear();
    location.href="../../login/index.html";
}

submit.addEventListener("click", toSubmitPage);
past.addEventListener("click", toPastPage);
logout.addEventListener("click", toLogout);

const loadPending = async () => {
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
    for (reim of reimList){
        if (reim.status === "pending"){
            resultList.push(reim);
        }
    }
    return resultList;
}

const createRow = (reim) => {
    return createTd(
        reim.reimAmount,
        reim.reimReason,
        reim.submittedDate,
    );
}

const createTd = (amount, reason, subDate) => {
    return `<td class="center">$ `+ amount + `</td>
    <td class="center">`+ reason + `</td>
    <td class="center">`+ subDate + `</td>`;
}


const processFailed = () => {
    let div = document.createElement("div");
    let p = document.createElement("p");
    p.innerHTML = "* Error loading reimbursements *"
    div.appendChild(p);
    document.body.appendChild(div);
}

loadPending();