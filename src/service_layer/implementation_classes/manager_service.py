from psycopg.errors import InFailedSqlTransaction, InvalidTextRepresentation

from src.custom_exceptions.invalidArgument import InvalidArgument
from src.data_access_layer.implementation_classes.manager_dao import ManagerDao
from src.entities.reimbursement import Reimbursement
from src.service_layer.abstract_classes.manager_service_abc import ManagerServiceAbc


class ManagerService(ManagerServiceAbc):

    def __init__(self, manager_dao: ManagerDao):
        self.manager_dao = manager_dao

    def service_approve_reim_by_id(self, reim_id: int, comment: str, status: str) -> Reimbursement:
        if status != "pending":
            raise InvalidArgument("This reimbursement has already been processed")
        try:
            return self.manager_dao.approve_reim_by_id(reim_id, comment)
        except InFailedSqlTransaction:
            raise InvalidArgument("Error approving reimbursement")
        except InvalidTextRepresentation:
            raise InvalidArgument("Error approving reimbursement")

    def service_reject_reim_by_id(self, reim_id: int, comment: str, status: str) -> Reimbursement:
        if status != "pending":
            raise InvalidArgument("This reimbursement has already been processed")
        try:
            return self.manager_dao.reject_reim_by_id(reim_id, comment)
        except InFailedSqlTransaction:
            raise InvalidArgument("Error rejecting reimbursement")
        except InvalidTextRepresentation:
            raise InvalidArgument("Error rejecting reimbursement")

    def service_get_all_reims(self, order: str) -> list[Reimbursement]:
        if order == "employee" or order == "reim":
            return self.manager_dao.get_all_reims(order)
        else:
            raise InvalidArgument("Invalid sort type")
