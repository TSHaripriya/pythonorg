import pyodbc

server = 'HCL-02-53\SQLEXPRESS04'
database = 'employee'
username = 'capstone'
password = 'Capstone@123'
cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()
class Insert_Exe(Exception):
    def __str__(self):
        return "Project is not in list of projects"
class Id_Exe(Exception):
    def __str__(self):
        return "Id already exist enter new id for employee"
class Bonus_Exception(Exception):
    def __str__(self):
        return "Bonus is very high enter with in range"

class employee():
    def __init__(self):
        self.bonus = 2
        self.project = ["c","java","python"]

    def Insert_EmpDetails(self, emp_id, NameOfEmployee, Salary, Project):
        Search_id = ''' select emp_id from employee_table '''
        Format_for_search_id = Search_id.format(id)
        value_for_search_id = cursor.execute(Format_for_search_id)
        f = False
        for i in value_for_search_id:
            if i.emp_id == id:
                f = True
                break
        if f:
            try:
                raise Id_Exe
            except Id_Exe as id_ex:
                print(id_ex)
        else:
            query = ''' INSERT INTO employee_table (emp_id,NameOfEmployee,Salary,Project) values ({0},'{1}',{2},'{3}') '''
            insertquery = query.format(emp_id, NameOfEmployee, Salary, Project)
            if Project in self.project:
                cursor.execute(insertquery)
                cnxn.commit()
                print("Employee details inserted sucsessfully in db")
            else:
                try:
                    raise Insert_Exe
                except Insert_Exe as ex:
                    print(ex)

    def Update_EmpDetails(self,emp_id,Project=' ',Salary=0):
        if Salary !=0:
            query_for_salary_update= ''' UPDATE employee_table SET Salary = {0} where emp_id = {1} '''
            insertquery_for_salary_update=query_for_salary_update.format(Salary,emp_id)
            cursor.execute(insertquery_for_salary_update)
            cnxn.commit()
            print("Updated Succsesfully")
        if Project:
            query_for_project= ''' UPDATE employee_table SET Project = '{0}' where emp_id = {1} '''
            insertquery_for_project_update = query_for_project.format(Project,emp_id)
            cursor.execute(insertquery_for_project_update)
            cnxn.commit()
            print("update successfully")
    def Display_EmpDetails(self):
        query_for_display_details='''select * from employee_table '''
        values=cursor.execute(query_for_display_details)
        for i in values:
            print("employee id ",i.emp_id," employee name ",i.NameOfEmployee," salary ",i.Salary," project ",i.Project)
    def Delete_EmpDetails(self,emp_id):
        query=''' DELETE from employee_table where emp_id = {0} '''.format(emp_id)
        cursor.execute(query)
        cnxn.commit()
        print("deleted successfully")
    def Add_Bonus(self,id,bonus):
        if bonus > 0 and bonus <= 2:
            query = ''' select Salary from employee_table where emp_id = {}'''.format(id)
            value = cursor.execute(query)
            for i in value:
                Salary = i.Salary
            bonus_bonus = int(Salary + (Salary * bonus))
            query_for_update_bonus = ''' UPDATE employee_table SET Salary = {0} where emp_id = {1} '''.format(
                bonus_bonus, id)
            cursor.execute(query_for_update_bonus)
            cnxn.commit()
            print("Bonus updated sucessfully")
        else:
            try:
                raise Bonus_Exception
            except Bonus_Exception as ex:
                print(ex)
obj = employee()
obj.Insert_EmpDetails(5,'Hari',90000,'c')
obj.Update_EmpDetails(4,'c',40000)
obj.Display_EmpDetails()
obj.Delete_EmpDetails(1)
obj.Add_Bonus(1,2)
