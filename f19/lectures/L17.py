#!/usr/bin/env python
# coding: utf-8

# Today we will talk about using the CSV data format for reading/writing/sharing text files. CSV stands for Comma Separated Values. It's quite flexible and compact, it's around since long time, and it's the main format used by popular spreadsheet programs such as Excel. Many data repositories make use of CSV as one their standard formats for data. 

# <img src="csv/excel.png" width="700">

# The file reports the monthly evolution of the Amazon's stock market prices at Nasdaq. Data are dowloaded from Yahoo! Finance https://finance.yahoo.com/quote/AMZN/history?period1=1521362028&period2=1552898028&interval=1mo&filter=history&frequency=1mo

# How the file looks like? Let's open it with a regular text editor:

# 
# <img src="csv/amazon_emacs.png" width="600">

# CSV (comma separated values) is a format commonly used to hold in a file data that
# can be naturally represented in tabular form (e.g., excel-like): 
# M data records/rows, each consisting of (at most) N ordered fields/columns
# 
# row 1: column 1, column 2, column 3, .... , column N
# 
# row 2: column 1, column 2, column 3, .... , column N
# 
# row 3: column 1, column 2, column 3, .... , column N
# 
# ......
# 
# row M: column 1, column 2, column 3, .... , column N
# 
# In practice, data is represented as matrix where each column refers to a common object
# and each row is a different data entry. 
# 
# Column data are separated by a given delimiter. The default delimiter is a comma, but
# other characters can be used as a delimiter
# 
# E.g.: columns are metereological measurements an N different metereological stations,
# where each row reports the measures for a different day
# 
# E.g.: columns are personal data, such as name, address, and ID, where each row of data
# refers to a different person
# 
# E.g., each column is the student grade for a specific course, where each row reports
# the set of grades for a different student
# 
# It is common, but not strictly required, that the first row/record in a csv file
# contains strings with the names/meanings of the columns (the legend for the file)
# 
# E.g., name, address, id, age, sex
# 
# J. Smith, Falcon Tower West-Bay, 532720 , 38, M  
# 
# A. White, Tower 99 The Pearl, 33145, 29, F  

# In[3]:


import csv
# The csv module provides a number of methods to effectively and efficiently deal with the 
# basic reading and writing operations on CSV files


# In[4]:


file_path = '/Users/giannidicaro/.spyder-py3/csv/Mall_Customers.csv'
file_name = file_path.split('/')[-1]
#print(file_name)
f_csv = open(file_path)
csv_data = csv.reader(f_csv, delimiter=',')
#
# csv_data is an iterator: at each call will return the next line in the file
# data are read into lists of strings, where each list element is a string with 
# a filed value, identified based on the given delimiter


# In[5]:


csv_data


# In[6]:


#f = open(file_path)
#cnt = 0
#for ff in f:
#    print(ff)
#    cnt += 1
#    if cnt > 10:
#        break

f_csv.seek(0)
# Let's print out what's in the file
line_count = 0
for row in csv_data:
    print('Row {:d}: {} (length: {})'.format(line_count, row, len(row)))
    next(csv_data)
    # another way to make the same print
    #print('Line: {}'.format(' - '.join(row)))
    line_count += 1
# it looks like most of the column fields are nicely separated by commas, but som fields
# have extra spaces: should we worry about it? Let's re-read the file and let's use the data


# In[7]:


# csv.reader() is an iterator: we have already reached the end, therefore, if we want
# to read it again, we have to restart from the beginning
# The function line = next(f_csv) can be used for to go to the next line, 
# it returns the current line
f_csv.seek(0)


# In[8]:


# this time let's get more info about the file and let's print output in a more structured way
line_count = 0
for row in csv_data:
    if line_count == 0:
        columns = len(row)
        print('File {} contains {:d} columns: {:s}'.format(file_name, columns, ' - '.join(row)))
    else:
        print('ID {} is a {:>6s} of {:2d} years making {:3d}$/year and has a spending score of {:3d}'.format(int(row[0]), row[1], int(row[2]), 
              int(row[3]), int(row[4])))
    line_count += 1
f_csv.close()
# output is correct: the int() function does a good job getting rid of all extra spaces 
# however, extra spaces in string fields stay there, because a space is a valid character!


# In[9]:


# is , the only allowed delimiter? It is the most common one, but we are not restricted to it
# let's deal with a file with the same content but different delimiter
file_path = '/Users/giannidicaro/.spyder-py3/csv/Mall_Customers-d2.csv'
f2_csv = open(file_path)
csv_data = csv.reader(f2_csv, delimiter=';')
line_count = 0
for row in csv_data:
    print('Line: {}'.format(' '.join(row)))
    line_count += 1
f2_csv.close()
# no problems at all, we get the same output!


# In[10]:


# what about a delimiter with more than one single character?
file_path = '/Users/giannidicaro/.spyder-py3/csv/Mall_Customers-d3.csv'
f3_csv = open(file_path)
try:
    csv_data = csv.reader(f3_csv, delimiter='--')
except:
    print("Delimiter must be 1-charater string!")
else:
    line_count = 0
    for row in csv_data:
        print('Line: {}'.format(' '.join(row)))
        line_count += 1
finally:
    f3_csv.close()
# TypeError! delimiter must be 1-character string!


# In[11]:


# What if I want to use commas but the fields contain commas in their data?
# Let's look at file employee_adresses.csv
# each record contains three fields:
# name, adress, date joined
# Unfortunately, the field address contains commas, as it is common defining addresses
# What happens if we try to read the file?
file_path = '/Users/giannidicaro/.spyder-py3/csv/employee_addresses.csv'
f_csv = open(file_path)
csv_data = csv.reader(f_csv, delimiter=',')
line_count = 0
for row in csv_data:
    print('Line: {} (#fields: {})'.format(' - '.join(row), len(row)))
    line_count += 1
f_csv.close()
# as expected, the number of fields in each row is 4 instead of being 3, since every comma
# in the row is interpreted as a field separator


# In[12]:


# How do we deal with this issue?
# Three possible strategies, all requiring modifying the original csv file:
# 1. Use a different delimiter in the csv file (e.g., ';')
# 2. Wrap the data containing commas in quotes: the string between the quotes is not 
#      evaluated for the delimiter. The character used for quoting needs to be specified by
#      the quotechar optional parameter if different from " which is the default 
# 3. Escape the delimiter character in the data: adding \ "protects" the character from 
#          being evaluated as a delimiter. If an escape character is used, it must be 
#          specified using the escapechar optional parameter.
# Strategy 1:         
file_path = '/Users/giannidicaro/.spyder-py3/csv/employee_addresses-d2.csv'
f_csv = open(file_path)
csv_data = csv.reader(f_csv, delimiter=';')
line_count = 0
for row in csv_data:
    print('Line: {} (#fields: {})'.format(' - '.join(row), len(row)))
    line_count += 1
f_csv.close()
# it works as expected!


# In[13]:


# Strategy 2:
file_path = '/Users/giannidicaro/.spyder-py3/csv/employee_addresses-quotes.csv'
f_csv = open(file_path)
csv_data = csv.reader(f_csv, delimiter=',', quotechar='"')
line_count = 0
for row in csv_data:
    print('Line: {} (#fields: {})'.format(' - '.join(row), len(row)))
    line_count += 1
f_csv.close()
# it works! however, some attention needs to be devoted to the presence of spaces 
# before or after the quoting character, that would prevent from letting the 
# character being properly interpreted


# In[14]:


# Strategy 3:
file_path = '/Users/giannidicaro/.spyder-py3/csv/employee_addresses-escape.csv'
f_csv = open(file_path)
csv_data = csv.reader(f_csv, delimiter=',', escapechar='\\')
line_count = 0
for row in csv_data:
    print('Line: {} (#fields: {})'.format(' - '.join(row), len(row)))
    line_count += 1
f_csv.close()


# In[15]:


# A csv file can be seen as a dictionary: each column has a label, 
# hence, we can read the csv data file (or, more generically, tabular data)
# into an 'ordered dictionary', an dictionary that preserves/remembers the order for entering
# the keys. The keays are sorted by the order associated to their entrance in the dictionary.
# Each row is an ordered dictionary with respect to the keys/columns
# An ordered dictionary is a data type from the module 'collections' that can be constructed
# with od = collections.OrderedDict()
#
file_path = '/Users/giannidicaro/.spyder-py3/csv/biometric_simple.csv'
f_csv = open(file_path)
csv_data = csv.DictReader(f_csv)
print("Type of object csv_data: {}\n".format(type(csv_data)))


# In[16]:


#
# The csv dictionary reader object csv_data is constructed from the first row
# of the csv file, that specifies the names of the fields, that is, the common label/key
# of each field / column.
#
# Based on the definition of the keys, csv data are read into an ordered dictionary
# where each row is stored in an ordered dictionary of strings: the keys are the strings
# defined in the header row and the values are strings representing the column values
# 
# The number and names of the fields/keys can be retrieved by accessing the list .fieldnames
# of the dictionary reader
#
import os 

num_of_keys = len(csv_data.fieldnames)
keys = csv_data.fieldnames
stat = os.stat(file_path)
size = stat.st_size


# In[17]:


# What is the number of records? the reader doesn't know at this stage, 
# we must read the data first! But we can print out the number of records
# and maybe the size of the entire file, to get an idea of how big it will be
#
print('File {} has size {} bytes and contains {:d} keys: {:s}\n'.format(file_name, 
                                                   size, num_of_keys, ' - '.join(keys)))


# In[18]:


# After the creation of the ordered dictionary object, the iterator is positioned at
# the first row with actual data
# Now we can read / print each line, which is a ordered dictionary with N keys
# Let's use the (known) names of columns to make a nice printing
line_count = 1
for row in csv_data:
    print('Row {} has type {} and {} keys'.format(line_count, type(row), len(row)))    
    print('{:<8s} has ID {:5d}, is {:2d} years old, {:4.2f}m tall, and weights {:5.2f}kg\n'.
          format(row['name'], int(row['id']), int(row['age']), 
                 float(row['height'])/100, float(row['weight'])))
    line_count += 1
#f_csv.close()


# In[19]:


# Can we get the same nice printing without first opening the file and reading the labels?
#
# First, let's notice that since we have read the entire file, we need to rewind it, 
# to go back to the first record. In fact, the instance csv_data is an iterator. 
# An iterator emits a unit of data on each explicit/implicit invocation of next() on it,
# and with the above instructions we have performed an implicit next() call at each
# step of the for loop. Therefore, now the iterator is at the end of the file
# and it is necessary to rewind the file, and skip the header
f_csv.seek(0)
next(csv_data) 


# In[20]:


# variable keys above is a list with all dictionary keys in order of column insertion, 
# and we know that in each row keys always keep the same order
# print(keys)
#
line_count = 1
for row in csv_data:
    print('{:<8s} has ID {:5d}, is {:2d} years old, {:4.2f}m tall, and weights {:5.2f}kg\n'.
          format(row[keys[1]], int(row[keys[0]]), int(row[keys[2]]), 
                 float(row[keys[3]])/100, float(row[keys[4]])))
    line_count += 1
#f_csv.close()


# In[21]:


# Let's rewind the file again and skip the header
f_csv.seek(0)
next(csv_data) 


# In[22]:


# csv data are tabular data, therefore a 'natural' way to address the data could be:
# my_data[row][label/column] which is what we used for instance for matrices, that are tables
# We can get this representation by reading all data into a list of ordered dictionaries
# and then address individua data based on record/row and label/column
#
tabular_csv = list(csv_data)  
# tabular_csv is a list of records in the form of ordered dictionaries
# How do we access the value of field 'name' in record 1?
print(tabular_csv[1]['name'])

# Using the keys we can also make adopt a label agnostic, more "pure" matrix representation:
print(tabular_csv[1][keys[1]])


# In[23]:


# Let's print out all data in the file using this notation, and let's print everything
# as it is in the dictionary, that is, as strings. Setting a predefined length in the
# format specifier it allows to have a decently nice formatting
#
for i in range(len(tabular_csv)):
    for k in range(num_of_keys):
        print('{:9s} '.format(tabular_csv[i][keys[k]]), end='')
    print('\n')

f_csv.close()

