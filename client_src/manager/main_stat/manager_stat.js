const role = sessionStorage.getItem("role");
const id = sessionStorage.getItem("employeeId");

const url = "http://127.0.0.1:5000/"
const route = "manager/reimbursements/employee"

const pending = document.getElementById("pending");
const past = document.getElementById("past");
const logout = document.getElementById("logout");

const toPendingPage = () => {
    location.href="../pending/manager_pending.html";
}

const toPastPage = () => {
    location.href="../past/manager_past.html";
}

const toLogout = () => {
    sessionStorage.clear();
    location.href="../../login/index.html";
}

pending.addEventListener("click", toPendingPage);
past.addEventListener("click", toPastPage);
logout.addEventListener("click", toLogout);

const loadStats = async () => {
    const response = await fetch(url + route, {
        method: "GET",
        mode: "cors"
    });

    if (response.status == 200) {
        const reimJson = await response.json();
        createStats(reimJson);
    }
    else {
        const body = await response.json();
    }
}

const createStats = (reim_json) => {
    let tbody = document.getElementById("tableBody");
    let reimList = reim_json.reimbursements;
    reimList = filterList(reimList);
    reimList = sortReimList(reimList);
    
    for (innerList of reimList) {
        tbody.insertRow().innerHTML = createRow(innerList);
    }

}

const filterList = (reimList) => {
    let resultList = [];
    for (reim of reimList){
        if (reim.status === "pending"){
        }
        else {
            resultList.push(reim);
        }
    }
    return resultList;
}

const sortReimList = (reimList) => {
    let returnList = [];
    let innerList = [];
    let id = reimList[0].employeeId;
    for (let reim of reimList) {
        if (id === reim.employeeId){
            innerList.push(reim);
        }
        else {
            returnList.push(innerList);
            innerList = [];
            id = reim.employeeId;
            innerList.push(reim);
        }
    }
    returnList.push(innerList);
    return returnList;
}

const createTd = (id, total, highest, average, numOf, approvalRate) => {
    return `<td class="center">`+ id +`</td>
    <td class="center">$ `+ total + `</td>
    <td class="center">$ `+ highest + `</td>
    <td class="center">$ `+ average + `</td>
    <td class="center">`+ numOf + `</td>
    <td class="center">`+ approvalRate + `</td>`;
}


const createRow = (reimList) => {
    return createTd(
        findId(reimList),
        createTotalAmount(reimList),
        createHighestAmount(reimList),
        createAverageAMount(reimList),
        createNumberOfReim(reimList),
        createApprovalRate(reimList)
    );
}

const findId = (reimList) => {
    return reimList[0].employeeId
}

const createTotalAmount = (reimList) => {
    let total = 0;
    for (reim of reimList) {
        total += parseFloat(reim.reimAmount);
    }
    return total;
}

const createHighestAmount = (reimList) => {
    let highest = 0;
    for (reim of reimList) {
        highest = Math.max(highest, reim.reimAmount);
    }
    return highest;
}

const createAverageAMount = (reimList) => {
    let total = createTotalAmount(reimList);
    let avg = total / reimList.length;
    return (Math.round(avg * 100) / 100);
}

const createNumberOfReim = (reimList) => {
    return reimList.length;
}

const createApprovalRate = (reimList) => {
    let approved = 0;
    let numOfReim = reimList.length;
    for (reim of reimList) {
        if (reim.status === "approved") {
            approved++;
        }
    }
    let rate = approved / numOfReim;
    return (Math.round(rate * 100) / 100) * 100 + " %";
}

loadStats();
