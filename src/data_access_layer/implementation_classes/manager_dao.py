"""
    manager_dao.py

    Implementation class for Manager DAO

    ******* These functionalities will e handled by the front-end *******
    as a manager, I should be able to log out so my information does not remain available on my computer
"""
from datetime import date

from psycopg.errors import InFailedSqlTransaction

from src.custom_exceptions.invalidArgument import InvalidArgument
from src.data_access_layer.abstract_classes.manager_dao_abc import ManagerDaoAbc
from src.entities.reimbursement import Reimbursement
from src.util.database_connection import connection


class ManagerDao(ManagerDaoAbc):

    # as a manager, I should be able to approve reimbursement requests because they are legitimate
    def approve_reim_by_id(self, reim_id: int, comment: str) -> Reimbursement:
        try:
            sql = "update \"project1\".reimbursement set manager_comment = %s, status = %s, processed_date = %s " \
                  "where reim_id = %s returning *"
            processed_date = date.today()
            cursor = connection.cursor()
            cursor.execute(sql, (comment, "approved", processed_date, reim_id))
            connection.commit()
            reim_record = cursor.fetchone()
            reim = Reimbursement(*reim_record)
            if reim.status == "approved":
                return reim
            else:
                return None
        except InFailedSqlTransaction:
            raise InvalidArgument("Error approving reimbursement")
        finally:
            connection.commit()

    # as a manager, I should be able to deny reimbursement requests because they are illegitimate
    # as a manager, I should be able to leave a comment about my decisions regarding reimbursement
    # -> requests so employees better understand my decisions
    def reject_reim_by_id(self, reim_id: int, comment: str) -> Reimbursement:
        try:
            sql = "update \"project1\".reimbursement set manager_comment = %s, status = %s, processed_date = %s " \
                  "where reim_id = %s returning *"
            processed_date = date.today()
            cursor = connection.cursor()
            cursor.execute(sql, (comment, "rejected", processed_date, reim_id))
            connection.commit()
            reim_record = cursor.fetchone()
            reim = Reimbursement(*reim_record)
            if reim.status == "rejected":
                return reim
            else:
                return None
        except InFailedSqlTransaction:
            raise InvalidArgument("Error rejecting reimbursement")
        finally:
            connection.commit()

    # as a manager, I should be able to view pending reimbursement requests so I can make decisions about them
    # as a manager, I should be able to view past reimbursement requests so I can check previous decisions
    # as a manager, I should be able to view reimbursement statistics so I can keep track of employee activities
    # statistics will be handled in front end
    def get_all_reims(self, order: str) -> list[Reimbursement]:
        if order == "reim":
            sql = "select * from \"project1\".reimbursement order by reim_id"
        else:
            sql = "select * from \"project1\".reimbursement order by employee_id"
        cursor = connection.cursor()
        cursor.execute(sql)
        reim_records = cursor.fetchall()
        reim_list = [Reimbursement(*record) for record in reim_records]
        return reim_list
