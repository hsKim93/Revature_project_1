# Project One

## Database

- ###User Schema

  - First Name: string
  - Last Name: string
  - Id: int primary key
  - Role: string (manager or employee)
  - user_name: string
  - password: string


- ###Reimbursements
  - id: primary
  - employee_id: refers to id in employee table
  - expense_name: string
  - expense_amount: float
  - expense_reason: string
  - status: string (past, pending, accepted)
  - date: date.now()
  - accepted_date: date.now()
  - reject_reason: string