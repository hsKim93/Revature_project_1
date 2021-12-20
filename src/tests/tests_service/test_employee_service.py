from datetime import date

from src.custom_exceptions.invalidArgument import InvalidArgument
from src.data_access_layer.implementation_classes.employee_dao import EmployeeDao
from src.entities.reimbursement import Reimbursement
from src.service_layer.implementation_classes.employee_service import EmployeeService

employee_dao = EmployeeDao()
employee_service = EmployeeService(employee_dao)

# request_log_in
def test_service_request_log_in_fail_wrong_id():
    try:
        employee_service.service_request_log_in("employee_testt", "12312")
        assert False
    except InvalidArgument as e:
        assert str(e) == "Incorrect credentials"

def test_service_request_log_in_fail_wrong_pw():
    try:
        employee_service.service_request_log_in("employee_test", "12312")
        assert False
    except InvalidArgument as e:
        assert str(e) == "Incorrect credentials"

def test_service_request_log_in_fail_wrong_credentials():
    try:
        employee_service.service_request_log_in("", "")
        assert False
    except InvalidArgument as e:
        assert str(e) == "Incorrect credentials"

# submit_new_reim
def test_service_submit_new_reim():
    try:
        employee_service.service_submit_new_reim(5)
        assert False
    except InvalidArgument as e:
        assert str(e) == "Invalid type"

# invalid amount
def test_service_submit_new_reim_neg():
    try:
        now = date.today()
        reim = Reimbursement(0, 0, -500, "hi", "hi", now)
        employee_service.service_submit_new_reim(reim)
        assert False
    except InvalidArgument as e:
        assert str(e) == "Amount must be non-zero and non-negative"

# invalid amount
def test_service_submit_new_rim_nan():
    try:
        now = date.today()
        reim = Reimbursement(0, 0, "wow", "hi", "hi", now)
        employee_service.service_submit_new_reim(reim)
        assert False
    except InvalidArgument as e:
        assert str(e) == "Invalid input for amount"

# get_my_reims
def test_service_get_my_reims():
    try:
        employee_service.service_get_my_reims("5")
        assert False
    except InvalidArgument as e:
        assert str(e) == "Invalid type"

