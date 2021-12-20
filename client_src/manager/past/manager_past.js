const role = sessionStorage.getItem("role");
const id = sessionStorage.getItem("employeeId");

const url = "http://127.0.0.1:5000/"
const route = "manager/reimbursements/reim"

const pending = document.getElementById("pending");
const home = document.getElementById("home");
const logout = document.getElementById("logout");

const toPendingPage = () => {
    location.href="../pending/manager_pending.html"
}

const toMainPage = () => {
    location.href="../main_stat/manager_stat.html"
}

const toLogout = () => {
    sessionStorage.clear();
    location.href="../../login/index.html";
}

pending.addEventListener("click", toPendingPage);
home.addEventListener("click", toMainPage);
logout.addEventListener("click", toLogout);

const loadPast = async () => {
    const response = await fetch(url + route, {
        method: "GET",
        mode: "cors"
    });

    if (response.status == 200) {
        const reimJson = await response.json();
        createPasts(reimJson);
    }
    else {
        const body = await response.json();
    }
}

const createPasts = (reim_json) => {
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
        if (reim.status !== "pending"){
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
        reim.status,
        reim.submittedDate,
        reim.processedDate,
        reim.managerComment
    );
}

const createTd = (id, amount, reason, status, subDate, proDate, comment) => {
    return `<td class="center">`+ id +`</td>
    <td class="center">$ `+ amount + `</td>
    <td class="center">`+ reason + `</td>
    <td class="center">`+ status + `</td>
    <td class="center">`+ subDate + `</td>
    <td class="center">`+ proDate + `</td>
    <td class="center">` + comment + `</td>`;
}


const processFailed = () => {
    let div = document.createElement("div");
    let p = document.createElement("p");
    p.innerHTML = "* Error loading reimbursements *"
    div.appendChild(p);
    document.body.appendChild(div);
}

loadPast();