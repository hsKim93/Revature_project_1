from abc import ABC, abstractmethod
from src.entities.reimbursement import Reimbursement


class ManagerServiceAbc(ABC):

    @abstractmethod
    def service_approve_reim_by_id(self, reim_id: int, comment: str, status: str) -> Reimbursement:
        pass

    @abstractmethod
    def service_reject_reim_by_id(self, reim_id: int, comment: str, status: str) -> Reimbursement:
        pass

    @abstractmethod
    def service_get_all_reims(self, order: str) -> list[Reimbursement]:
        pass
