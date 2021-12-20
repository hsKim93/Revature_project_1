"""
    employee_dao_abc.py

    Abstract class for Employee DAO

    ******* These functionalities will e handled by the front-end *******
    as an employee, I should be able to logout so my information does not remain available on my computer
"""
from abc import ABC, abstractmethod
from src.entities.reimbursement import Reimbursement


class EmployeeDaoAbc(ABC):

    # as a manager, I should be able to login so I can approve or deny reimbursements
    # as an employee, I should be able to login so I can manage my reimbursements
    @abstractmethod
    def request_log_in(self, log_in_id: str, log_in_pw: str) -> dict:
        pass

    # as an employee, I should be able to submit new reimbursement requests so I can get money back from the company
    @abstractmethod
    def submit_new_reim(self, new_reim: Reimbursement) -> Reimbursement:
        pass

    # as an employee, I should be able to review my reimbursement requests so I can know if they are approved or denied
    @abstractmethod
    def get_my_reims(self, employee_id: int) -> list[Reimbursement]:
        pass
