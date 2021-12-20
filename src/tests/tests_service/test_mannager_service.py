from src.custom_exceptions.invalidArgument import InvalidArgument
from src.data_access_layer.implementation_classes.manager_dao import ManagerDao
from src.service_layer.implementation_classes.manager_service import ManagerService

manager_dao = ManagerDao()
manager_service = ManagerService(manager_dao)


# incorrect parameter
def test_service_approve_reim_by_id_wrong_type():
    try:
        manager_service.service_approve_reim_by_id("hi", "hi", "pending")
        assert False
    except InvalidArgument as e:
        assert str(e) == "Error approving reimbursement"


# already processed
def test_service_approve_reim_by_id_not_pending():
    try:
        manager_service.service_approve_reim_by_id(5, "hi", "approved")
        assert False
    except InvalidArgument as e:
        assert str(e) == "This reimbursement has already been processed"


# incorrect parameter
def test_service_reject_reim_by_id_wrong_type():
    try:
        manager_service.service_reject_reim_by_id("hi", "hi", "pending")
        assert False
    except InvalidArgument as e:
        assert str(e) == "Error rejecting reimbursement"


# already processed
def test_service_reject_reim_by_id_not_pending():
    try:
        manager_service.service_reject_reim_by_id(5, "hi", "rejected")
        assert False
    except InvalidArgument as e:
        assert str(e) == "This reimbursement has already been processed"


# wrong sort type
def test_service_get_all_reims():
    try:
        manager_service.service_get_all_reims("hi")
        assert False
    except InvalidArgument as e:
        assert str(e) == "Invalid sort type"
