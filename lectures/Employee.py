#An employee is a person + some other properties that are specific to the company / job.
# Therefore, it makes sense to define the class Employee as a child (derived) class of the
# Person class, that becomes the base (super) class. This will save a lot of code rewriting. # Employee adds a few attributes and methods. More could be added here of course ...
#
from Person import Person

class Employee(Person):
    def __init__(self, first, last, sex=None, age=None, staff_num=None, 
                 position=None, since=None):
        Person.__init__(self, first, last, sex, age)
        self.staff_number = staff_num
        self.position = position
        self.since = since
        self.salary_data = []
        
    def get_employee(self):
        return [self.name(), self.staff_number, self.get_age(), 
                self.position, self.since]
             
    def set_education(self, degrees):
        self.bachelor = degrees['bachelor']
        self.master = degrees['master']
        self.doctorate = degrees['doctorate']
        
    def get_education(self):
        return 'Bachelor: {}, Master: {}, Doctorate: {}'.format(self.bachelor,
                                                                self.master, 
                                                                self.doctorate)
   
    def income_data(self, data=None, filename=None):
        if data != None:
            self.salary_data = data[:]
        elif filename != None:
            try:
                f = open(filename)
            except:
                print('Error: File {} is not accessible'.format(filename))
                return False
            for r in f:
                fields = r.split(',')
                period = fields[0]
                salary = float(fields[1])
                self.salary_data.append( (period, salary) )
        else:
            print('Error: an input source needs to be provided!')
            return False
        
    def show_salary_history(self):
        plt.figure(figsize=(6, 4))
        plt.title("Salary historical data")
        periods = []
        salary = []
        for s in self.salary_data:
            periods.append(int(s[0]))
            salary.append(s[1])
        plt.xlabel('Year')
        plt.ylabel('Salary ($)')
        plt.plot(periods, salary)
        plt.show()
        

if __name__ == '__main__':
    # generate a file with random values for the salary in subfolder 'homer_data'
    import random
    subfolder = 'homer_data'
    income_data = os.path.join(subfolder, 'homer_salary.csv')
    if os.path.isdir(subfolder):
        f = open(income_data, 'w')
    else:
        os.mkdir(subfolder)
        f = open(income_file, 'w')
    for i in range(1990, 2020):
        salary = random.gauss(50000, 20000)
        f.write('{}, {:.2f}\n'.format(i, salary))
    f.close()
    
    # create a new employee    
    new_employee = Employee("Homer", "Simpson", 39, "1007", 'troublemaker')
    new_employee.set_education({'bachelor': 'laziness', 'master':'sofalogy', 
                                'doctorate':'still enrolled'})
    print(new_employee.get_employee())
    print(new_employee.get_education())
    
    # get income data and display it
    new_employee.income_data(filename = income_data)
    new_employee.show_salary_history()
    
