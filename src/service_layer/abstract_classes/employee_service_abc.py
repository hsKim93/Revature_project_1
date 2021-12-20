from abc import ABC, abstractmethod

from src.entities.reimbursement import Reimbursement


class EmployeeServiceAbc(ABC):

    @abstractmethod
    def service_request_log_in(self, log_in_id: str, log_in_pw: str) -> dict:
        pass

    @abstractmethod
    def service_submit_new_reim(self, new_reim: Reimbursement) -> Reimbursement:
        pass

    @abstractmethod
    def service_get_my_reims(self, employee_id: int) -> list[Reimbursement]:
        pass
