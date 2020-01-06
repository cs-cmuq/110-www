import time

#n = 100000000 # good value for testing
n = 1000000
large_dict = {}
large_list = []
large_set = {0}
type_str = {type({}): "Dict:", type([]): "List", type({1}): "Set:"}

def initialize(data_struct, num):
    if len(data_struct) > 1:
            data_struct.clear()
    start = time.process_time()
    if type(data_struct) == dict:
        for i in range(num):
            data_struct[i] = i
    elif type(data_struct) == list:
        for i in range(num):
            data_struct.append(i)
       
    elif type(data_struct) == set:
        for i in range(num):
            data_struct.add(i)
    else:
        print("Error in data type!")
        return
    
    end = time.process_time()
    print(type_str[type(data_struct)], end - start, flush=True)

def find_value(val, where): 
    start = time.process_time()
    check = val in where
    end = time.process_time()
    print(type_str[type(where)], check, end - start, flush=True)

initialize(large_dict, n)
initialize(large_list, n)

find_value(n-1, large_dict)
find_value(n-1, large_list)
######################## 

########################
phone_numbers = {'Ann': 5461, 'Paul': 5472, 'Mark': 3541, 'Liz': 2451}

numbers = {1: 'r', 2: 'p', 3:'p', 4:'r', 5:'p', 6:'r'}

accounts = [ ['J. Smith', 35672, 'M', 'USA'], ['M. Saleh', 27623, 'M', 'Jordan'], 
	  ['F. Dupont', 17623, 'F', 'France'] ]

by_name = {'J. Smith': [35672, 'M', 'USA'], 'M. Saleh': [27623, 'M', 'Jordan'], 
     'F. Dupont': [17623, 'F', 'France']}

by_country = {'USA': [35672, 'M', 'J. Smith'], 'Jordan': [27623, 'M', 'M. Saleh'], 
              'France': [17623, 'F', 'F. Dupont']}
############################

word_list = [ ('Hello', 5), ('this', 4), ('is', 2), ('a',1), ('list',4) ]
word_dict = dict(word_list)

parabola = dict( [ (0,0), (0.5, 0.25), (1,1), (1.5, 2.25) ] ) 

v = dict( [ ('USA', [35672, 'M', 'J. Smith']), ('Jordan', [27623, 'M', 'M. Saleh']), 
           ('France', [17623, 'F', 'F. Dupont']) ] )
############################

list_of_words = ["This", "is", "a", "list", "of", "key", "strings"]
dict_of_words = dict.fromkeys(list_of_words, 0)

keys = {'a', 'e', 'i', 'o', 'u'}
keys = (1,2,3,4)
vowels = dict.fromkeys(keys)

primes = [2, 3, 5, 7, 11, 13]
dict_of_primes = dict.fromkeys(primes, 'p')
###############################

list_of_keys = [1, 2, 3, 4, 5, 6]
list_of_values = ['r', 'p', 'p', 'r', 'p', 'r' ]
numbers = dict(zip(list_of_keys, list_of_values))
##############################

numbers = {1: 'r', 2: 'p', 3:'p', 4:'r', 5:'p', 6:'r'}
new_dict_same_content = numbers.copy()
new_dict_same_content[36] = 'r'
if 36 not in numbers:
    print("Change in the new dictionary didn't affected previous dictionary")

alias_dict = numbers
alias_dict[36] = 'r'
if 36 in numbers:
    print("Change in the new dictionary affected previous dictionary!")
#################################
    
accounts = {'J. Smith': [35672, 'M', 'USA'], 'M. Saleh': [27623, 'M', 'Jordan'], 
            'F. Dupont': [17623, 'F', 'France']}
phone_numbers = {'Ann': 5461, 'Paul': 5472, 'Mark': 3541, 'Liz': 2451}
numbers = {1: 'r', 2: 'p', 3:'p', 4:'r', 5:'p', 6:'r'}

accounts['Y. Honda'] = [75643, 'F', 'Japan']
phone_numbers['Luc'] = 6653

a = accounts['Y. Honda']
p= phone_numbers['Luc']

accounts['J. Smith'] = [35672, 'M', 'Canada']
accounts['J. Smith'][2] = 'Qatar'
##################################

len(accounts)  
len(numbers)   

list(accounts)  
list(phone_numbers) 
list(numbers) 

is_in = 3 in numbers
is_in = 'Jim' not in phone_numbers 

numbers.keys()
l = list(numbers)  
##################################

numbers = {1: 'r', 2: 'p', 3:'p', 4:'r', 5:'p', 6:'r'}
keys_now_in_dict = list(numbers)
keys_view = numbers.keys()
numbers[13] = 'p'
print("Is 13 in dict? From static list copy:", (13 in keys_now_in_dict) )
print("Is 13 in dict? From dynamic view:", (13 in keys_view) )
######################################

numbers = {1:'r', 2:'p', 3:'p', 4:'r', 5:'p', 6:'r'}
numbers.values()
numbers.items()
##########################

for k in numbers:
  print('Key:', k)

for i in numbers.items():
  print('Pair (key, value):', i[0], i[1])
####################
  
numbers = {1:'r', 2:'p', 3:'p', 4:'r', 5:'p', 6:'r'}
key = 3
x = numbers.get(key)
if x != None:
	print('Value associated to key', key, 'is:', x)

#x = numbers['key']
################################

numbers = {1:'r', 2:'p', 3:'p', 4:'r', 5:'p', 6:'r'}
key = 3
x = numbers.pop(key)
if x != None:
	print('Removed pair (', key, x, ')')
    
#key = 11
#del numbers[key]
##################################

numbers = {1:'r', 2:'p', 3:'p', 4:'r', 5:'p', 6:'r'}
x = numbers.popitem()
if len(numbers) > 0:
    print('Removed the last inserted key-value pair (', x, ')')
    print('New size of the dictionary:', len(numbers))
#####################################
    
numbers = {1:'r', 2:'p', 3:'p', 4:'r', 5:'p', 6:'r'}
numbers.clear()
print('Removed all elements')
###################################

numbers = {1:'r', 2:'p', 3:'p', 4:'r', 5:'p', 6:'r'}
some_primes = {13:'p', 17:'p', 23:'p'}
numbers.update(some_primes)
print('Updated dictionary:', numbers)

new_entry= {12:'r'}
numbers.update(new_entry)
print('Dictionary updated with a new single entry')

l = [(10, 'r'), (12, 'r')]
numbers.update(l)
print('Dictionary updated with a list of entries')
############################

val = numbers.setdefault(30, 'r')
val = numbers.setdefault(30, 'rr')

new_dict = {}
for i in range(10):
    new_dict.setdefault(i)
#####################################

accounts = {'J. Smith': [35672, 'M', 'USA'], 'M. Saleh': [27623, 'M', 'Jordan'], 
	         'F. Dupont': [17623, 'F', 'France'] } 
numbers = {1: 'r', 2: 'p', 3:'p', 4:'r', 5:'p', 6:'r'}

x = accounts == numbers
accounts2 = accounts.copy()
x = accounts == accounts2
###################################

numbers = {1: 'p', 2: 'p', 3:'p', 4:'r', 5:'p', 6:'r'}
sorted_keys = sorted(numbers) 
sorted_keys = sorted(numbers.keys())

sorted_values = sorted(numbers.values()) 

keys_to_be_sorted = list(numbers.keys())
keys_to_be_sorted.sort()

sorted_dict_list = sorted(numbers.items())
#####################################

numbers = {1: 'p', 2: 'p', 3:'p', 4:'r', 5:'p', 6:'r'}
max_key_val = max(numbers)
min_key_val = min(numbers)
max_key_val = max(numbers.keys())
min_key_val = min(numbers.keys())

max_values = max(numbers.values())
min_values = min(numbers.values())

key_sum = sum(numbers)
key_sum = sum(numbers.keys())
#values_sum = sum(numbers.values())
######################################

new_set = {1, 2, 3, 4.5, 5.3, True, (1,2), 'Hello'}
print(new_set, type(new_set))

#new_set = {1, 2, 3, [1,2]}
 ##################################
 
l = [1, 2, 3, 4.5, 5.3, True, (1,2)]
new_set = set(l)
print(new_set, type(new_set))

numbers = {1: 'p', 2: 'p', 3:'p', 4:'r', 5:'p', 6:'r'}
new_set = set(numbers)
new_set = set(numbers.values())
new_set = set("apple")
new_set = set(["apple"]) 
empty_set = set()                                           # empty set
############################################
    
my_set = {1,3,5}
my_set.add(2)
print(my_set, '\n')
my_set.add(1)  
print(my_set, '\n')

my_set = {1,3,5}
print(my_set, '\n')
my_set.update([2,3,4]) 
print(my_set, '\n')       # my_set now contains {1,2,3,4,5}
my_set.update({2,2,2}) 
print(my_set, '\n')       # my_set is left unchanged, it still contains {1,2,3,4,5}
my_set.update({'c':1, 'b':2})
print(my_set, '\n') # my_set now contains {1, 2, 3, 4, 5, 'b', 'c'}
my_set.update("apple")
print(my_set, '\n')         
###################################

my_set = {1,3,5}
my_set.discard(3)   # my_set is now {1,5} 
my_set.discard(4)  

my_set = {1,3,5}
my_set.remove(3)  # my_set is now {1,5} 
#my_set.remove(4)  
###################################

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(A | B)
#Output: {1, 2, 3, 4, 5, 6, 7, 8}
#####################

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(A & B)
#Output: {4, 5}
#####################

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(A - B)
#Output: {1, 2, 3}

print(B - A)
#Output: {6, 7, 8}
####################

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(A ^ B)
#Output: {1, 2, 3, 6, 7, 8}
######################

my_set = set("apple")    # my_set  is {'e', 'a', 'l', 'p'}
in_set = 'a' in my_set   # in_set  is  True
in_set = 2 in my_set     

my_set = set("apple")
for letter in my_set:     # for loop with letter taking the values in {'e', 'a', 'l', 'p’}
   print(letter)
##############################















