

# Makes use of classes and inheritance with an 
# Employee and a Manager
#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
"""
Employee, having attributes:
    Name
    Hire date
    Badge ID number
    Salary
    Workdays (Monday â€“ Friday). They may not work all 5 days.
Manager who is an employee, with the additional attributes of:
    Bonus
    Direct reports â€“ a  dictionary of employees that work for them
    Workdays (Monday â€“ Saturday). They may not work all 6 days
"""

# the Employee class
class Employee(object):
    def __init__(self,name,hire_date,badge,salary,workdays):
        self.__name = name
        self.__hire_date = hire_date
        self.__badge = badge
        self.__salary = salary
        self.__workdays = workdays

    def __eq__(self, other):
        return self.name == other.name
            
    def __le__(self, other):   
        return self.name <= other.name
        
    def __gt__(self, other):
        return self.name >= other.name
    
    @property
    def name(self):
        return self.__name

    @property
    def hire_date(self):
        return self.__hire_date

    @property
    def badge(self):
        return self.__badge

    @property
    def salary(self):
        return self.__salary

    @property
    def workdays(self):
        return self.__workdays

    @name.setter
    def name(self,new_value):
        self.__name = new_value

        
    @hire_date.setter
    def hire_date(self,new_value):
        self.__hire_date = new_value

    @badge.setter
    def badge(self,new_value):
        self.__badge = new_value

    @salary.setter
    def salary(self,new_value):
        self.__salary = new_value

    @workdays.setter
    def workdays(self,new_value):
        if "Sat" in new_value or "Sun" in new_value:
           raise ValueError("Employee work only Mon - Fri")
        self.__workdays = new_value


    def __str__(self):
        return "{} was hired {}, works {}, badge number {}, and salary ${:6,}".format(self.__name,
        self.hire_date,self.workdays,self.badge,self.salary)

class Manager(Employee):
    def __init__(self,name,hire_date,badge,salary,workdays,bonus,direct_reports):
        super(Manager,self).__init__(name,hire_date,badge,salary,workdays)
        self.__bonus = bonus
        self.__direct_reports = direct_reports

    def __eq__(self, other):
        return self.name == other.name
            
    def __le__(self, other):   
        return self.name <= other.name
        
    def __gt__(self, other):
        return self.name >= other.name
    
    def __contains__(self,employee):
        return employee.badge in self.direct_reports
    
    def __add__(self,employee):
        self.direct_reports = employee
    
    @property
    def bonus(self):
        return self.__bonus

    @property
    def direct_reports(self):
        return self.__direct_reports

    @property
    def workdays(self):
        return super(Manager,self).workdays

    @bonus.setter
    def bonus(self,new_value):
        self.__bonus = new_value

    @direct_reports.setter
    def direct_reports(self,new_report):
        self.__direct_reports[new_report.badge] = new_report

    # there is no restriction on a manager's work day
    @workdays.setter
    def workdays(self,new_value):
        super(Manager,self).__workdays = new_value

    def __str__(self):
        return "Manager "+super(Manager,self).__str__() + \
               ", has bonus {}% and direct reports:\n {}"\
                   .format(int(self.bonus*100),
                           '\n'.join(['' if len(self.direct_reports) == 0 else str(self.direct_reports[key]) for key in self.direct_reports]))

#%%
# get all the lines in the file and 
def input_file(filename):
    with open(filename,"r") as fp:
        lines = fp.readlines()

    for i in range(len(lines)):
        lines[i] = lines[i].strip().split(',')
    return lines
def main():
    managers = {}
    man = []
    # get all the managers and set their list of direct
    # reports to the empty dictionary. This dictionary
    # will be indexed by the employee's badge number
    
    for line in input_file("managers-1.txt"):
        print(line)
        man.append(line[2])
        managers[line[2]] = Manager(name=line[0],
                                    hire_date=line[1],
                                    badge=line[2],
                                    salary=float(line[3]),
                                    workdays=line[5:],
                                    bonus=float(line[4]),
                                    direct_reports={})
    
    # using the badge number of the managers add the employee
    # to their manager.
    for line in input_file("employees.txt"):
        print(line)
        managers[line[0]].direct_reports = Employee(name=line[1],
                                                    hire_date=line[2],
                                                    badge=line[3],
                                                    salary=float(line[4]),
                                                    workdays=line[5:])
    
    
    
    Bob = Employee(name= "Bob",
                   hire_date= "08/19/25",
                   badge="#001",
                   salary= 80000,
                   workdays="Mon, Tues, Wed")
    Sally = Employee(name= "Sally",
                     hire_date= "09/19/25",
                     badge="#002",
                     salary= 80001,
                     workdays="Mon, Tues, Wed")
    
    for item in man:
        if Bob in managers[item]:
            print("True")
        else:
            print("False")
         
    #%%
    #show what is stored in the data structure
    print('\n\n'.join([str(managers[i]) for i in managers]))


main()    
#%%
