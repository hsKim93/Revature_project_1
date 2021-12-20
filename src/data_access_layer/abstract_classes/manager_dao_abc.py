"""
    manager_dao_abc.py

    Abstract class for Manager DAO

    ******* These functionalities will e handled by the front-end *******
    as a manager, I should be able to log out so my information does not remain available on my computer
"""
from abc import ABC, abstractmethod

from src.entities.reimbursement import Reimbursement


class ManagerDaoAbc(ABC):

    # as a manager, I should be able to approve reimbursement requests because they are legitimate
    @abstractmethod
    def approve_reim_by_id(self, reim_id: int, comment: str) -> Reimbursement:
        pass

    # as a manager, I should be able to deny reimbursement requests because they are illegitimate
    # as a manager, I should be able to leave a comment about my decisions regarding reimbursement
    # -> requests so employees better understand my decisions
    @abstractmethod
    def reject_reim_by_id(self, reim_id: int, comment: str) -> Reimbursement:
        pass

    # as a manager, I should be able to view pending reimbursement requests so I can make decisions about them
    # as a manager, I should be able to view past reimbursement requests so I can check previous decisions
    # as a manager, I should be able to view reimbursement statistics so I can keep track of employee activities
    # statistics will be handled in front end
    @abstractmethod
    def get_all_reims(self, order: str) -> list[Reimbursement]:
        pass
