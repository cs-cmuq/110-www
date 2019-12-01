
from IPython.display import display, Image

import matplotlib.pyplot as plt

class Person:

    def __init__(self, first, last, sex=None, age=None):
        self.firstname = first
        self.lastname = last
        self.age = age
        self.sex = sex
        self.family = {'partner':None, 'children': set()}
        self.residency = {}

    def name(self):
        return self.lastname + ", " + self.firstname
   
    def set_age(self, age):
        self.age = age
        
    def get_age(self):
        return self.age
    
    def set_sex(self, sex):
        self.sex = sex
        
    def get_sex(self):
        return self.sex
    
    def add_photo(self, filename):
        try:
            f = open(filename, 'rb')
        except:
            print('Error: File {} is not accessible'.format(filename))
            return False
        else:
            self.photo = f.read()
            return True
    
    def show_photo(self):
        display(Image(data=self.photo))
        
    
    def add_partner(self, person):
        self.family['partner'] = person
        
    def add_child(self, person):
        self.family['children'].add(person)
        
    def get_family_information(self):
        print('Family composition of {}:'.format(self.name()))
        
        if self.family['partner'] != None:
            print('  Partner is ', self.family['partner'].name())
        
        if len(self.family['children']) > 0:
            print('  Children are: ', end='')
            for i in self.family['children']:
                print('{}; '.format(i.name()), end='')
            print('\n')
          
    def add_residency_info(self, filename):
        try:
            f = open(filename, 'r')
        except:
            print('Error: File {} is not accessible'.format(filename))
            return False
        
        f.readline()
        for r in f:
            fields = r.split(',')
            from_year = int(fields[0])
            to_year   = int(fields[1])
            places = ','.join(fields[2:])
            self.residency[(from_year, to_year)] = places.replace('\n', '')
    
    def show_residency_info(self):
        if len(self.residency) == 0:
            print('No residency info were added so far')
            return False
        
        print('{} has lived in the following places:'.format(self.name()))
        sorted_residency = sorted(self.residency.items())
        for r in sorted_residency:
            print('From {} to {}: {}'.format(r[0][0], r[0][1], r[1]))
        return True
    
    def get_longest_stay(self):
        longest = [-1, 0, 0]
        for y in self.residency:
            if (y[1] - y[0]) >  longest[0]:
                longest = [y[1] - y[0], y[0], y[1]]
        return (longest[0], self.residency[(longest[1], longest[2])])
    
    def graphic_display_of_residency(self):
        xsize = 6
        ysize = 6
        plt.figure(figsize=(xsize, ysize))
        plt.title("A Pie Chart of Residency")
        years = []
        info_labels = []
        for y in self.residency:
            years.append(y[1]-y[0])
            info_labels.append('{}-{}, {}'.format(y[0], y[1], self.residency[y]))
            
        plt.pie(years, labels=info_labels) 
        plt.show()
     
    def income_data(self):
        print('Nothing to say')
        
    def show_income_history(self):
        pass
    

if __name__ == '__main__':
    
    marge = Person('Marge', 'Simpson', 'F')
    homer = Person('Homer', 'Simpson', 'M', 39)
    bart = Person('Bart', 'Simpson', 'M', 10)
    lisa = Person('Lisa', 'Simpson', 'F', 8)
    
    lisa.add_photo('lisa.png')
    lisa.show_photo()
    
    marge.add_child(bart)
    marge.add_child(lisa)
    marge.add_partner(homer)
    marge.get_family_information()
    
    homer.add_residency_info('homer_residency.csv')
    homer.show_residency_info()
    
    print('\nLongest stay for {} was: {}'.format(homer.name(), 
                                               homer.get_longest_stay()))
    homer.graphic_display_of_residency()


