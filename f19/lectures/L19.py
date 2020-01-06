#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# So far we have been using the built-in Python's data types. 
# Each data type (e.g., int, str, list, set, file) represents a certain set of values,
# it holds information. Also, each data type had a set of associated operations, via function
# types, that allowed to manipulate the information. 
# In a sense, we treated data as passive entities that were manipulated and combined via 
# active operations. This is a traditional way to view computation. 
# To build complex (software) systems, however, it helps to take a richer view of the 
# relationship between data and operations.
# Object-oriented (OO) design and development is one way to tackle modeling of and interaction
# with complex systems.


# In[ ]:


# The basic idea of object-oriented (OO) design is to view a complex system as the 
# interaction of simpler objects. The word objects is being used here in a specific technical 
# sense. An OO "object" is a sort of active data type that combines both data and operations. 
# Objects hold information, know stuff (they contain data), and they can act upon their and
# other information data, they can do stuff (they have operations). 
# Objects interact by sending each other messages. A message is simply a request for an 
# object to perform one of its operations.


# In[ ]:


# Example: management system for a university ... it's definitely a complex system!
# Let's start from the basics: information about the enrolled students
# Each student is an "object" of the university system.
# Each student object must hold various information, including, for instance: name, ID number, 
# courses taken, campus address, home address, GPA, etc. 
# Each student object must be able to respond to specific requests (messages) from the 
# management system: it must be equipped with operations that can be invoked.
# For instance, to send out a postal mail to all students, the management system
# would need to get the address of each student being printed on a label.
# In this case, a student object would include a method that when invoked does
# the job of printing the student's address on the label.
# Courses are also objects of the university system. 
# A course object would hold various information, including: who the instructor is, 
# what students are in the course, what the prerequisites are, and when and where the 
# course classes happen.
# One example operation for a course object would consist in adding a student. 
# When invoked with a student object as an argument, this method would cause 
# the enrollment of the student in the course. 
# Teachers would be represented by another type of objects.
# Also rooms, facilities, etc. would be represented by other types of objects ...
# Overall, the software system would grow quite complex, since it has to model and
# deal with a complex real-world system such as a university.
#


# In[ ]:


# Let's consider the simple class to represent and interact with a dog 
# (e.g., an animated or a robotic one). 
# The attributes of interest include: color, eye color, height, length, weight, name, 
# status ('sitting', 'laying down', 'shaking', 'near me')
# The methods to interact with the dog objects are: sit(), lay_down(), shake(), come()


# In[36]:


class Dog:
    def __init__(self, color=None, eyes=None, 
                 height=None, length=None, weight=None, name=None):
        self.color = color
        self.eyes = eyes
        self.height = height
        self.length = length
        self.weight = weight
        self.name = name
        self.status = None
        
    def sit(self):
        if self.status != 'sitting':
            print('Sit!')
            # tell the dog to sit
            self.status = 'sitting'
        else:
            print("It's sitting already!")
        
    def lay_down(self):
        if self.status != 'laying down':
            print('Lay down!')
            # tell the dog to lay down
            self.status = 'laying down'
        else:
            print("It's laying down already!")
        
    def shake(self):
        if self.status != 'shaking':
            print('Shake hands!')
            # tell the dog to shake hands
            self.status = 'shaking'
        else:
            print("It's shaking hands already!")
        
    def come(self):
        if self.status != 'near me':
            print('Come here!')
            # tell the dog to come close
            self.status = 'near me'
        else:
            print("It's here already!")
    
    def get_info(self):
        info = '{} has {} fur and {} eyes, {}in tall, {}in long, {}kg weight'.format(
                self.name, self.color, self.eyes, self.height, self.length, self.weight)
        print(info)
        return info
    
    def get_object_data(self):
        print(self, type(self))
        return type(self)
    


# In[37]:


rayne = Dog('gray', 'blue', 18, 36, 30, 'Rayne')
rayne.come()
rayne.come()
s = rayne.get_info()
print(s)
rayne.get_object_data()


# In[38]:


skinny = Dog('black', 'brown', 19, 38, 27, 'Skinny')
skinny.get_object_data()
# self values (i.e, ids of the two class objects) are different: skynny abd rayne are two different instances of 
# the same abstract class, Dog


# In[41]:


bully = Dog(name='Bully')
bully.eyes = skinny.eyes
print(bully.eyes)
#
# It is in general possible to access an internal variable directly, using the name of the class variable, 
# however this is not a good practice in terms of information hiding and code safety
# A better way to proceed is by defining methods to access and set the values of internal attributes
# e.g., in this case, the following two methods would do the work:
#
# def get_eyes():
#    return self.eyes
#
# def set_eyes(eyes_color):
#    self.eyes = eyes_color
# 
# If a user needs to access / modify eyes' color, it can do it by using these easy to use methods, without messing
# up with iternal variable names and types (that could be even difficult to ascertain from the code in some cases)

