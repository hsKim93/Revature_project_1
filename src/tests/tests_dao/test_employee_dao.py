from datetime import date

from src.data_access_layer.implementation_classes.employee_dao import EmployeeDao
from src.entities.reimbursement import Reimbursement

employee_dao = EmployeeDao()

# log in as employee
def test_request_log_in_employee():
    result = employee_dao.request_log_in("employee_test", "123123")
    assert result["role"] == "employee" and result["employeeId"] == 1

# log in as manager
def test_request_log_in_manager():
    result = employee_dao.request_log_in("manager_test", "123123")
    assert result["role"] == "manager" and result["employeeId"] == 2

# submit new reimbursement
def test_submit_new_reim():
    submitted_date = date.today()
    new_reim = Reimbursement(0, 1, 500, "medical bill", "pending", submitted_date)
    result = employee_dao.submit_new_reim(new_reim)
    assert result.employee_id == new_reim.employee_id \
           and result.reim_amount == new_reim.reim_amount \
           and result.reim_reason == new_reim.reim_reason \
           and result.status == new_reim.status

def test_submit_new_reim2():
    submitted_date = date.today()
    new_reim = Reimbursement(0, 1, 50, "food", "pending", submitted_date)
    result = employee_dao.submit_new_reim(new_reim)
    assert result.employee_id == new_reim.employee_id \
           and result.reim_amount == new_reim.reim_amount \
           and result.reim_reason == new_reim.reim_reason \
           and result.status == new_reim.status

# get all my reimbursements
def test_get_my_reims():
    result = employee_dao.get_my_reims(1)
    assert type(result) is list and result[0].employee_id == 1
