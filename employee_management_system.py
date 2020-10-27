import sqlite3
from employee import Employee

class EMS:
    def  __init__(self):
        ## initialize  the database connection
        self.conn = sqlite3.connect('main_db.db')
        self.c = self.conn.cursor()

    def addEmployee(self, uid, fname, lname, job, pay, address):
        ## add an employee object to the database
        emp = Employee(uid, fname, lname, job, pay, address)
        try:
            self.c.execute("INSERT INTO emp_details VALUES (:uid, :fname, :lname, :job, :pay, :addr)",
                           {'uid': emp.getUID(),
                            'fname': emp.getfname(),
                            'lname': emp.getlname(),
                            'job': emp.getJob(),
                            'pay': emp.getPay(),
                            'addr': emp.getAddress()})
            print("\nEntry Added to Database!!!\n")
        except sqlite3.IntegrityError:
            print('UNIQUE FIELDS CANNOT HAVE DUPLICATE VALUES!!!')
        finally:
            self.conn.commit()


    def updateEmployee(self, emp_id, updates):
        ## update the pay of a particular employee
        filtered_updates = {}
        for i in updates:
            if updates[i] != 'N':
                filtered_updates[i] = updates[i]
        try:
            self.c.execute("UPDATE emp_details SET firstname = :fname, lastname = :lname, job_desc = :job, pay=:pay, address=:addr"
                           " WHERE EMP_ID = :emp_id", {'fname':filtered_updates[up_fname], 'lname' : filtered_updates[up_lname],
                                                       'job' : filtered_updates[up_job],
                                                       'pay' : filtered_updates[up_pay],
                                                       'addr' : filtered_updates[up_add]})
            print("\nEmployee Updated!!!\n")
        except Exception as e:
            ## print(e)
            pass
        finally:
            self.conn.commit()


    def getEmployee(self, emp_id):
        ## get all details about  a particular employee

        self.c.execute("SELECT * FROM emp_details WHERE EMP_ID=:emp_id", {'emp_id' : emp_id})
        res = self.c.fetchall()
        if len(res) == 0:
            print("\nNo Matches Found!!!\n")
        else:
            print(res[0])
        self.conn.commit()

    def removeEmployee(self, emp_id):
        ## delete a particular employee record from the database
        try:
            self.c.execute("DELETE FROM emp_details WHERE EMP_ID=:emp_id", {'emp_id' : emp_id})
            print("\nRecord Deleted SuccessFully\n")
        except Exception as e:
            print(e)
        finally:
            self.conn.commit()

    def terminateConnections(self):
        self.conn.close()

    def displayEntireTable(self):
        ## displays the entire table
        self.c.execute("SELECT * FROM emp_details")
        for tuple in self.c.fetchall():
            print(tuple)
        self.conn.commit()

    def createTable(self):
        ## Create the employee table
        self.c.execute("""CREATE TABLE IF NOT EXISTS emp_details(EMP_ID integer PRIMARY KEY, firstname text, lastname text, job_desc text, pay integer, address text)""")

if __name__ == "__main__":
    ems = EMS()
    while True:
        print("\nEnter your Choice !! ")
        print("1.Create Table\n2.Add Employee\n3.Get Employee Details\n4.Update Employee Pay\n5.Delete Record\n6.Display Table\n7.Exit\n")
        choice = int(input())
        if choice == 1:
            ems.createTable()
        elif choice == 2:
            uid = input("Enter Employee UID :- ")
            fname = input("Enter First Name :- ")
            lname = input("Enter Last Name :- ")
            job = input("Enter Job Description :- ")
            pay = input("Enter Pay :-  ")
            address = input("Enter Permanent Address :- ")
            ems.addEmployee(uid, fname, lname, job, pay, address)
        elif choice == 3:
            emp_id = input("Enter Employee ID :- ")
            ems.getEmployee(emp_id)
        elif choice == 4:
            emp_id = input("Enter Employee ID :- ")
            print("\nEnter all data to be updates.\nFor a field to be updated, enter the  updated value.\nIf you dont want to update a particular field enter N\n")
            up_fname = input("\nEnter updated first Name :- ")
            up_lname = input("\nEnter updated last name :- ")
            up_job = input("\nEnter updated Job Description :- ")
            up_pay = input("\nEnter updated Pay :- ")
            up_add = input("\nEnter updated address :- ")
            updates = {'up_fname' : up_fname,
                       'up_lname' : up_lname,
                       'up_job' : up_job,
                       'up_pay' : up_pay,
                       'up_addr' : up_add}
            ems.updateEmployee(emp_id,updates)
        elif choice == 5:
            emp_id = input("Enter Employee ID :- ")
            ems.removeEmployee(emp_id)
        elif choice == 6:
            ems.displayEntireTable();
        elif  choice == 7:
            print("Thank you for using our EMS!!!")
            ems.terminateConnections()
            exit()






