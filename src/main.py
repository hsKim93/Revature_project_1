from datetime import date
from flask import Flask, request, jsonify
from flask_cors import CORS
import logging
from src.custom_exceptions.invalidArgument import InvalidArgument
from src.data_access_layer.implementation_classes.employee_dao import EmployeeDao
from src.data_access_layer.implementation_classes.manager_dao import ManagerDao
from src.entities.reimbursement import Reimbursement
from src.service_layer.implementation_classes.employee_service import EmployeeService
from src.service_layer.implementation_classes.manager_service import ManagerService

logging.basicConfig(filename="records.log", level=logging.DEBUG, format=f"%(asctime)s %(levelname)s %(message)s")

app: Flask = Flask(__name__)
CORS(app)

employee_service = EmployeeService(EmployeeDao())
manager_service = ManagerService(ManagerDao())


##################
# Employee route #
##################

@app.post("/login")
def request_log_in():
    try:
        data = request.get_json()
        result = employee_service.service_request_log_in(
            data["loginId"],
            data["loginPw"]
        )
        return jsonify(result), 200
    except InvalidArgument as e:
        error_message = {
            "errorMessage": str(e)
        }
        return jsonify(error_message), 400
    except KeyError:
        error_message = {
            "errorMessage": "Invalid JSON was received"
        }
        return jsonify(error_message), 400


@app.post("/employee/reimbursement")
def submit_new_reim():
    try:
        data = request.get_json()
        result = employee_service.service_submit_new_reim(Reimbursement(
            0,
            data["employeeId"],
            float(data["reimAmount"]),
            data["reimReason"],
            "pending",
            date.today()
        ))
        return jsonify(result.make_dictionary()), 201
    except InvalidArgument as e:
        error_message = {
            "errorMessage": str(e)
        }
        return jsonify(error_message), 400
    except KeyError:
        error_message = {
            "errorMessage": "Invalid JSON was received"
        }
        return jsonify(error_message), 400


@app.get("/employee/reimbursement/<employee_id>")
def get_my_reims(employee_id: str):
    try:
        result = employee_service.service_get_my_reims(int(employee_id))
        result_list = []
        for reim in result:
            result_list.append(reim.make_dictionary())
        result_dict = {
            "reimbursements": result_list
        }
        return jsonify(result_dict), 200
    except InvalidArgument as e:
        error_message = {
            "errorMessage": str(e)
        }
        return jsonify(error_message), 400


#################
# Manager route #
#################

@app.post("/manager/approve/reimbursement")
def approve_reim_by_id():
    try:
        data = request.get_json()
        result = manager_service.service_approve_reim_by_id(int(data["reimId"]), data["comment"], data["status"])
        if result:
            return jsonify(result.make_dictionary()), 200
    except TypeError as e:
        error_message = {
            "errorMessage": str(e)
        }
        return jsonify(error_message), 400
    except KeyError:
        error_message = {
            "errorMessage": "Invalid JSON was received"
        }
        return jsonify(error_message), 400
    except InvalidArgument as e:
        error_message = {
            "errorMessage": str(e)
        }
        return jsonify(error_message), 400


@app.post("/manager/reject/reimbursement")
def reject_reim_by_id():
    try:
        data = request.get_json()
        result = manager_service.service_reject_reim_by_id(int(data["reimId"]), data["comment"], data["status"])
        if result:
            return jsonify(result.make_dictionary()), 200
    except TypeError as e:
        error_message = {
            "errorMessage": str(e)
        }
        return jsonify(error_message), 400
    except KeyError:
        error_message = {
            "errorMessage": "Invalid JSON was received"
        }
        return jsonify(error_message), 400
    except InvalidArgument as e:
        error_message = {
            "errorMessage": str(e)
        }
        return jsonify(error_message), 400


@app.get("/manager/reimbursements/<order_type>")
def get_all_reims(order_type: str):
    try:
        result = manager_service.service_get_all_reims(order_type)
        if result:
            result_list = []
            for reim in result:
                result_list.append(reim.make_dictionary())
            result_dict = {
                "reimbursements": result_list
            }
            return jsonify(result_dict), 200
    except TypeError as e:
        error_message = {
            "errorMessage": str(e)
        }
        return jsonify(error_message), 400
    except InvalidArgument as e:
        error_message = {
            "errorMessage": str(e)
        }
        return jsonify(error_message), 400


app.run()
