#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time
def infinite_regress (n):
    print("At", n)
    time.sleep(0.01)  # this makes the process "sleeping" for the given amount of seconds
    infinite_regress(n-1)


# In[ ]:


infinite_regress(5)
# need to interrupt the kernel to stop the running process that would never 
# end, in theory. 
# In practice it will end when the memory stack for calling the function will get full
# When this happens we get the following error:
# RecursionError: maximum recursion depth exceeded while calling a Python object
#


# In[ ]:


def factorial(n):
    # Base case: 1! = 1
    if n == 1 or n == 0:
        return 1

    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial(n-1)


# In[ ]:


for i in range(n):
    print('{}: {}'.format(i, factorial(i)))


# In[ ]:


def factorial_verbose(n):
    print("factorial has been called with n =", n)
    if n == 1 or n == 0:
        return 1
    else:
        res = n * factorial(n-1)
        print("intermediate result for {} * factorial({}): {}".format(n, n-1,res))
        return res

print(factorial_verbose(5))


# In[ ]:


factorial(100)
# The number of digits in an integer number is only limited by the OS memory. Numbers can
# grow a lot. The same isn't in general true for floats.


# In[ ]:


import sys
sys.getrecursionlimit()
#sys.setrecursionlimit(4500)


# In[ ]:


def factorial_it(n):
    v = 1
    for i in range(2, n+1):
        v *= i
    return v


# In[ ]:


import time
def compare_running_times(experiments, trials, algorithms, args=None):
    '''Takes as input two functions/algorithms and compares their running times
       over a given number of experiments/tests (+1). Each experiment consists of a number
       of trials, whose results are averaged. The results of the comparisons are printed out.
       Inputs: experiments (integer) specifies the number of tests, where the index of each 
               experiment is used as input for the algorithms. trials (integer) specifies 
               how many times each experiment is repeated, accounting for random variability. 
               The running times observed in each trial are averaged to compute the average 
               running time for each experiment. algorithms (list) is a list
               of two lists, where each list element contains in turn two elements, the
               first one is a string with the name of the algorithm, and the second is a
               variable holding the reference to a function (that implements the algorithm), e.g.,
               algorithms = [ ['label alg 1', function_alg_1],['label alg 2', function_alg_2] ].
               args (list) is a list of two lists with the additional arguments to pass to the
               two functions, if any. e.g. args = [x, y], or arg = [x, None] if the second algorithm
               doesn't take any additional parameter.
        Output: None is returned. However, for each trial, a summary of the observed running
                times for the two algorithms, as well as their ratio, is printed out.
    '''
    for n in range(experiments + 1):
        total = []
        msg = 'n={}, '.format(n)
        for a in (0,1):
            observed_times = []
            for r in range(trials):
                start = time.process_time()
                algorithm = algorithms[a][1]
                if args == None:
                    algorithm(n)
                else:
                    if args[a] != None:
                        algorithm(n, args[a])
                    else:
                        algorithm(n)
                end = time.process_time()
                observed_times.append(end - start)
            average_time = sum(observed_times) / trials
            total.append(average_time)
            msg += '{:s}: {:.9f}, '.format(algorithms[a][0], total[-1])
        msg += 'ratio: {:.3f}'.format(total[0] / total[1])
        print(msg)

compare_running_times(40, 30, [ ['factorial recursion', factorial], ['factorial iteration', factorial_it] ])


# In[ ]:


def exponentiate(x, n):
    if n == 0:
        return 1
    else: 
        return x * exponentiate(x, n - 1)


# In[ ]:


exponentiate(0, 10)


# In[ ]:


def summation(n):
    if n == 0:
        return 0
    else: 
        return n + summation(n - 1)


# In[ ]:


n = 100
print(summation(n), (n * (n+1))/2)


# In[ ]:


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


# In[ ]:


for i in range(20):
    print(fibonacci(i))


# In[ ]:


def fibonacci_iteration(n):
    past_state, new_state = 0, 1
    if n == 0:
        return 0
    for i in range(n-1):
        past_state, new_state = new_state, past_state + new_state
    return new_state


# In[ ]:


compare_running_times(35, 20, [ ['fibonacci recursion', fibonacci], ['fibonacci iteration', fibonacci_iteration]])


# In[ ]:


computed = {0:0, 1:1}
def fibonacci_memoization(n, computed):
    if n not in computed:
        computed[n] = fibonacci_memoization(n-1, computed) + fibonacci_memoization(n-2, computed)
    return computed[n]

fibonacci_memoization(40, computed)

def fibonacci_memoization_g(n):
    global computed
    if n not in computed:
        computed[n] = fibonacci_memoization_g(n-1) + fibonacci_memoization_g(n-2)
    return computed[n]

fibonacci_memoization_g(50)


# In[ ]:


computed = {0:0, 1:1}
compare_running_times(40, 10, [ ['fibonacci rec+memoization', fibonacci_memoization], 
                                ['fibonacci iteration', fibonacci_iteration]], [computed, None])


# In[ ]:


def exponent_divide(x, n): 
    global count
    count += 1
    # Base Cases 
    if (n == 0): 
        return 1
    if (x == 0): 
        return 0
      
    # If n is even 
    if (n % 2 == 0): 
        y = exponent_divide(x, n/2) 
        return y * y
      
    # If n is odd 
    else: 
        y = exponent_divide(x, (n-1)/2)  
        return  x * (y * y)


# In[ ]:


import math
n = 1000
x = 5
count = 0
print(exponent_divide(x,n), count/2, math.log(n)) 


# In[ ]:


def nested_sum(l):
    total = 0
    for element in l:
        if (type(element) != type([])):
            total += element
        else:
            total += nested_sum(element)
    return total
print( "Sum is:", nested_sum([ 1,2, [1,2,3], [3,4, [1,2,[3,2]]] ]))


# In[ ]:


def binary_search(values, start_pos, end_pos, key):
    '''Search key in list values from index (start_pos) to index (end_pos - 1).
        Returns the index of the key in the list, or -1 if not found.'''
    if not start_pos < end_pos:
        return -1
    mid = (start_pos + end_pos) // 2
    if values[mid] < key:
        return binary_search(values, mid + 1, end_pos, key)
    elif values[mid] > key:
        return binary_search(values, start_pos, mid, key)
    else:
        return mid
 


# In[ ]:


v = [3,4,5,39,54,78,109]
binary_search(v, 0, len(v), 78)


# In[ ]:


binary_search(v, 0, len(v), 32)

