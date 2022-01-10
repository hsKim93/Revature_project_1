# Reimbursement App

## Project Description

This app allows employees to submit reimbursement requests and view their reimbursement history, and allows managers to manage employees' reimbursement requests as well as view history and statistics.

## Technologies Used

* Python - version 3.9.9
* Flask - version 2.0.2
* Selenium - version 4.1.0
* behave - version 1.2.6
* pytest - version 6.2.5
* Psycopg - version 3.0.5
* DBeaver - version 21.3.1
* PostgreSQL - version 9.6
* HTML5
* CSS3
* Javascript

## Features

* Log in feature for both employee and manager
* Reimbursement submission feature for employee
* Reimbursement history feature for employee and manager
* Reimbursement management feature for manager

## Getting Started
   
1. Set up PostgreSQL data base
```
create table employee (
	employee_id serial primary key,
	fisrt_name varchar(20),
	last_name varchar(20),
	employee_role varchar(8),
	employee_log_in_id varchar(20) unique,
	employee_log_in_pw varchar(20)
);

create table reimbursement (
	reim_id serial primary key,
	employee_id int references employee(employee_id) on delete cascade,
	reim_amount decimal,
	reim_reason text,
	status varchar(8) default 'pending',
	submitted_date varchar(40),
	processed_date varchar(40) default NULL,
	manager_comment text default NULL
);
```
2. Add your database environment variables to your main.py
3. Run main.py
4. Run index.html
