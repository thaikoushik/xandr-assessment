XANDR Assignment 
==============================
This project is a coding assignment for Xandr, which hosts few endpoints for adding and updating employees information and their salaries.  
### Project Structure
    .
    ├── DockerFile              # Dockerfile contains list of commands
    ├── src                     # Source files
    	├── server.py           
    	├── db                  # Database files - create/update
    		├── db_helper.py 
		├── data.txt    # Database file 
    ├── License
    └── README.md
	

Getting Started
------------
This project hosted the below endoints 
- /save(POST) - pass ane employee object with parameters (name, dob, role, salary, joindate) to save an employee
- /getallemployees(GET) - Use this route to get all the employees from the DB
- /updatesalary/<empid>(PUT) - Use this route to update an employee salary by 5%, pass employee id in URL
- /getemployee/<empid> (GET) - Use this route to get employee info using employee id

Sample Employee object:
```` 
[
    {
        "id": "1",
        "name": "kk",
        "dob": "06/28/2021",
        "role": "sde",
        "salary": "55125.0",
        "joindate": "06/28/2021"
    },
    {
        "id": "2",
        "name": "Koushik",
        "dob": "06/28/2021",
        "role": "sde",
        "salary": "73500.0",
        "joindate": "06/28/2021"
    }
]
```` 
To run the project using docker file, run the below dockers commands which will create and run image
- Clone the repo
- In the project directory - 
`docker build -t xandr-assignment .`

- Run the below command to see the list of the images
`docker image`

- Copy the image id associated to the Repository xandr-assignment
`docker run -d -p 5000:5000 <IMAGE ID copied from the above command>`

- Below command will show the list of the running containers 
`docker ps` 

- Use the below commands to stop and remove container
`docker stop <IMAGE ID>`
`docker rm <IMAGE ID>`
