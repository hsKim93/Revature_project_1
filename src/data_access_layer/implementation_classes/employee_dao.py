"""
    employee_dao.py

    Implementation class for Employee DAO

    ******* These functionalities will e handled by the front-end *******
    as an employee, I should be able to logout so my information does not remain available on my computer
"""
from psycopg.errors import InFailedSqlTransaction

from src.custom_exceptions.invalidArgument import InvalidArgument
from src.data_access_layer.abstract_classes.employee_dao_abc import EmployeeDaoAbc
from src.entities.reimbursement import Reimbursement
from src.util.database_connection import connection


class EmployeeDao(EmployeeDaoAbc):

    # as a manager, I should be able to login so I can approve or deny reimbursements
    # as an employee, I should be able to login so I can manage my reimbursements
    def request_log_in(self, log_in_id: str, log_in_pw: str, ) -> dict:
        try:
            sql = "select employee_role, employee_id from \"project1\".employee where employee_log_in_id = %s " \
                  "and employee_log_in_pw = %s"
            cursor = connection.cursor()
            cursor.execute(sql, (log_in_id, log_in_pw))
            record = cursor.fetchone()
            return {
                "role": record[0],
                "employeeId": record[1]
            }
        except InFailedSqlTransaction:
            raise InvalidArgument("Invalid request")
        finally:
            connection.commit()

    # as an employee, I should be able to submit new reimbursement requests so I can get money back from the company
    def submit_new_reim(self, new_reim: Reimbursement) -> Reimbursement:
        try:
            sql = "insert into \"project1\".reimbursement values(default, %s, %s, %s, %s," \
                  " %s, default, default) returning *"
            cursor = connection.cursor()
            cursor.execute(sql, (new_reim.employee_id,
                                 new_reim.reim_amount,
                                 new_reim.reim_reason,
                                 new_reim.status,
                                 new_reim.submitted_date
                                 ))
            connection.commit()
            reim_record = cursor.fetchone()
            result_reim = Reimbursement(*reim_record)
            return result_reim
        except InFailedSqlTransaction:
            raise InvalidArgument("Invalid request")
        finally:
            connection.commit()

    # as an employee, I should be able to review my reimbursement requests so I can know if they are approved or denied
    def get_my_reims(self, employee_id: int) -> list[Reimbursement]:
        sql = "select * from \"project1\".reimbursement where employee_id = %s order by reim_id"
        cursor = connection.cursor()
        cursor.execute(sql, [employee_id])
        reim_records = cursor.fetchall()
        result = []
        for reim_record in reim_records:
            result.append(Reimbursement(*reim_record))
        return result
