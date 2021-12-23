from src.data_access_layer.implementation_classes.manager_dao import ManagerDao

manager_dao = ManagerDao()

def test_approve_reim_by_id():
    passed = manager_dao.approve_reim_by_id(2, "accident in company property")
    assert passed

def test_reject_reim_by_id():
    passed = manager_dao.reject_reim_by_id(1, "unauthorized action")
    assert passed

def test_get_all_reims():
    reim_list = manager_dao.get_all_reims("reim")
    assert len(reim_list) >= 2
