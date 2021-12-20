from datetime import date


class Reimbursement:
    def __init__(
            self,
            reim_id: int,
            employee_id: int,
            reim_amount: float,
            reim_reason: str,
            status: str,
            submitted_date: date,
            processed_date: date = None,
            comment: str = None
    ):
        self.reim_id = reim_id
        self.employee_id = employee_id
        self.reim_amount = reim_amount
        self.reim_reason = reim_reason
        self.status = status
        self.submitted_date = submitted_date
        self.processed_date = processed_date
        self.manager_comment = comment

    def make_dictionary(self):
        return {
            "reimId": self.reim_id,
            "employeeId": self.employee_id,
            "reimAmount": self.reim_amount,
            "reimReason": self.reim_reason,
            "status": self.status,
            "submittedDate": self.submitted_date,
            "processedDate": self.processed_date,
            "managerComment": self.manager_comment
        }