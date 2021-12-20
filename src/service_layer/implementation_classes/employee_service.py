from psycopg.errors import InFailedSqlTransaction, InvalidTextRepresentation

from src.custom_exceptions.invalidArgument import InvalidArgument
from src.data_access_layer.implementation_classes.employee_dao import EmployeeDao
from src.entities.reimbursement import Reimbursement
from src.service_layer.abstract_classes.employee_service_abc import EmployeeServiceAbc


class EmployeeService(EmployeeServiceAbc):

    def __init__(self, employee_dao: EmployeeDao):
        self.employee_dao = employee_dao

    def service_request_log_in(self, log_in_id: str, log_in_pw: str) -> dict:
        try:
            return self.employee_dao.request_log_in(log_in_id, log_in_pw)
        except TypeError:
            raise InvalidArgument("Incorrect credentials")
        except InFailedSqlTransaction:
            raise InvalidArgument("Incorrect credentials")
        except InvalidTextRepresentation:
            raise InvalidArgument("Incorrect credentials")

    def service_submit_new_reim(self, new_reim: Reimbursement) -> Reimbursement:
        try:
            if not isinstance(new_reim, Reimbursement):
                raise InvalidArgument("Invalid type")
            if isinstance(new_reim.reim_amount, str):
                raise InvalidArgument("Invalid input for amount")
            if new_reim.reim_amount <= 0:
                raise InvalidArgument("Amount must be non-zero and non-negative")
            return self.employee_dao.submit_new_reim(new_reim)
        except InFailedSqlTransaction:
            raise InvalidArgument("Invalid request")
        except InvalidTextRepresentation:
            raise InvalidArgument("Invalid request")

    def service_get_my_reims(self, employee_id: int) -> list[Reimbursement]:
        try:
            if not isinstance(employee_id, int):
                raise InvalidArgument("Invalid type")
            return self.employee_dao.get_my_reims(employee_id)
        except InFailedSqlTransaction:
            raise InvalidArgument("Invalid request")
        except InvalidTextRepresentation:
            raise InvalidArgument("Invalid request")
