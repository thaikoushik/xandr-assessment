import os
import json
import pandas as pd

def save_data(json_data):
    """

    This method saves the employee details into a pipe delimitted file.
        id - gets created based on number of records in the file
        name
        dob
        role
        salary
        joindate
    return:
        it returns a dictionary object with exception(error or none), status(True or False) and data (none or data)
    """
    #get data from json
    data = json_data.to_dict()
    emp_count = 0

    #Get cound of  number of records to calculate new employee id
    with open(os.getcwd()+'/db/data.txt', "r") as file:
        for _ in file:
            emp_count += 1

    #create a data str with pipe delimitted file
    data_str = str(emp_count)+"|"+data['name']+"|"+data['dob']+"|"+data['role']+"|"+data['salary']+"|"+data['joindate']
    try:
        with open(os.getcwd()+'/db/data.txt', 'a') as write_object:
            write_object.write("\n"+data_str)
        #create a record with id
        data['id'] = emp_count
        return {'exception':None, 'status':True, 'data':data}
    except Exception as exception:
        return {'exception': str(exception), 'status':False, 'data':''}
###################################################################################################
def update_salary(emp_id):
    """
    This method updates an employee salary for the given id by 5%

     return:
        it returns a dictionary object with exception(error or none), status(True or False)
        and data with updated salary by 5% (none or data)
    """
    try:
        #employee id
        emp_id = int(emp_id if emp_id else 0)
        #read db file into pandas dataframe
        df = pd.read_csv(os.getcwd()+'/db/data.txt', sep="|", index_col=False)
        #Update salary by 5% for the employee id
        df.loc[df['id'] == emp_id, ['salary']] = (df.loc[df['id'] == emp_id, ['salary']]) + \
                (df.loc[df['id'] == emp_id, ['salary']] * 0.05)
        #ccreate a db file with pip seperator
        df.to_csv(os.getcwd()+'/db/data.txt', sep="|", index=False)
        #extract the employee data
        data = df.loc[df['id'] == emp_id]
        return{'exception':None, 'status':True, 'data': data.to_json(orient="records")}
    except Exception as exception:
        return {'exception': str(exception), 'status':False, 'data':[]}
###################################################################################################
def get_employees():
    """
    This method returns all the employees in the db

    return:
        it returns a dictionary object with exception(error or none), status(True or False)
        and data with updated salary by 5% (none or data)
    """
    try:
        #Convert the pipe delimitted data into JSON
        dl = []
        #Open data file
        with open(os.getcwd()+'/db/data.txt', "r") as file:
            for line in file:
                dl.append(line.strip().split("|"))
        #create data dictionary
        data = [dict(zip(dl[0],row)) for row in dl]
        data.pop(0)
        #COnvert dictionary indo JSON
        json_data = json.dumps(data)
        return{'exception':None, 'status':True, 'data': json_data}#json_data
    except Exception as exception:
        return{'exception': str(exception), 'status':False, 'data': []}
###################################################################################################
def get_employee_info(emp_id):
    """
    This method returns the employee infor for the employee id

    return:
        it returns a dictionary object with exception(error or none), status(True or False)
        and data with updated salary by 5% (none or data)
    """
    try:
        #load data file into dataframe
        df = pd.read_csv(os.getcwd()+'/db/data.txt', sep="|", index_col=False)
        #Convert employee id into int
        emp_id = int(emp_id if emp_id else 0)
        #Get the record wihthe mployee id
        data = df.loc[df['id'] == emp_id]
        return {'exception':None, 'status':True, 'data': data.to_json(orient="records")}
    except Exception as exception:
        return {'exception': str(exception), 'status':False, 'data':[]}