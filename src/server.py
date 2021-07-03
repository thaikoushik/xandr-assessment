from flask import Flask
from flask import request, redirect, url_for
from flask import Blueprint
from db.db_helper import *

server = Flask(__name__)

#server = Blueprint("", __name__)

@server.route("/readme")
def read_me():
    txt = """Hera are the available routes -
            1. /save(POST) - pass ane employee object with parameters (name, dob, role, salary, joindate) to save an employee
            2. /getallemployees(GET) - Use this route to get all the employees from the DB
            3. /updatesalary/<empid>(PUT) - Use this route to update an employee salary by 5%, pass employee id in URL
            4. /getemployee/<empid> (GET) - Use this route to get employee info using employee id"""
    return txt
###################################################################################################
@server.route('/', defaults={'path': ''}, methods=['GET','POST','PUT','DELETE'])
@server.route('/<path:path>')
def catch_all(path):
    # returns a 200 (not a 404) with the following contents:
    return redirect(url_for('read_me'))

###################################################################################################
@server.route("/save", methods=["POST"])
def save_employee():
    """
    This route saves one employee record into the flat file DB
    json Object:
        {"name":"Ex","dob":"06/28/2021","role":"SDE","salary":500000,"joindate":"07/01/2021"}
    return:
        message
    """
    #Get form data
    data = request.form
    #Call DB_helper method to save data. returns stata which has messag, status and data
    state = save_data(data)
    #if error return appropriate message
    if not state['status']:
        return {"message":"Data not Insterted", "error": state['exception']}
    #Return data if there is no error
    return {"message":"Data Insterted Successfully", "data":state["data"]}
###################################################################################################
@server.route("/getallemployees", methods=['GET'])
def get_all_employees():
    """
    This route gets all the employees in the db and returns all the information
    return:
        returns the employee details in JSON
    """
    #Call the method in db_helper
    state = get_employees()
    #Based on status retuen appropriate message
    if not state['status']:
        return {"message":"No data Available", "error": state['exception']}
    return state['data']
###################################################################################################
@server.route("/updatesalary/<empid>", methods=["PUT"])
def update_salaries(empid):
    """
    This route updates the employee salary by 5% and return the update employee record
    return:
        it returns the employee information in JSON
    """
    #Call the method in db_helper
    state = update_salary(empid)
    #return data or message if the id is present
    if not state['status']:
        return {"message":"Employee records not updated", "error": state['exception']}
    return state["data"]
###################################################################################################
@server.route("/getemployee/<empid>", methods=["GET"])
def get_employee_data(empid):
    """
    This route gets all the employee details for the given id
    return:
        it returns the employee info if ID is found else return message
    """
    #Call the method in db_helper
    state = get_employee_info(empid)
    #return data or message if the id is present
    if not state['status']:
        return {"message":"Employee not found"}
    return state["data"]
###################################################################################################
if __name__ == "__main__":
   server.run(host='0.0.0.0', port=5000, debug=True)