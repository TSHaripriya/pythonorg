import pyodbc

server = 'HCL-02-53\SQLEXPRESS04'
database = 'employee'
username = 'capstone'
password = 'Capstone@123'
cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()

class Table_CreationError(Exception):
    def __str__(self):
        return "table created"
class Employee_Schema():
    def create_table(self):
        try:
            query='''
                    create table employee_table
                    (
                    emp_id int NOT NULL,
                    NameOfEmployee varchar(50),
                    Salary int,
                    Project varchar(50),
                    PRIMARY KEY(emp_id)
                     )
                '''
            cursor.execute(query)
            cnxn.commit()
        except Table_CreationError as h:
            print(h)
obj=Employee_Schema()
obj.create_table()



