# import random
#
# import pandas as pd
# import random
#
#
# def get_user_input():
#
#     return random.choice(['mean', 'std', 'minimum', 'maximum'])
#
# def mean(d):
#     return 1
#
# def std(d):
#     return 1
#
# def minimum(d):
#     return 1
#
# def maximum(d):
#     return 1
#
# # Add the missing function references to the function map
# function_map = {
#   'mean': mean,
#   'std': std,
#   'minimum': minimum,
#   'maximum': maximum
# }
#
#
#
# # data = load_data())
#
# data_ = {'height': [72.1, 69.8, 63.2, 64.7], 'weight': [198, 204, 164, 238]}
#
# # Create DataFrame
# data = pd.DataFrame(data_)
#
# # height  weight
# # 0    72.1     198
# # 1    69.8     204
# # 2    63.2     164
# # 3    64.7     238
# print(data)
#
# func_name = get_user_input()
#
# # Call the chosen function and pass "data" as an argument
# function_map['mean'](data)
# ----------------------------------------------------------------
# # Call has_docstring() on the load_and_plot_data() function
# ok = has_docstring(load_and_plot_data)
#
# if not ok:
#   print("load_and_plot_data() doesn't have a docstring!")
# else:
#   print("load_and_plot_data() looks ok")
#
#   # Call has_docstring() on the as_2D() function
#   ok = has_docstring(as_2D)
#
#   if not ok:
#       print("as_2D() doesn't have a docstring!")
#   else:
#       print("as_2D() looks ok")
#
# # Call has_docstring() on the log_product() function
# ok = has_docstring(log_product)
#
# if not ok:
#   print("log_product() doesn't have a docstring!")
# else:
#   print("log_product() looks ok")
#   *
# ----------------------------------------------------------------
# def create_math_function(func_name):
#     if func_name == 'add':
#         def add(a, b):
#             return a + b
#
#         return add
#     elif func_name == 'subtract':
#         # Define the subtract() function
#         def subtract(a, b):
#             return a - b
#
#         return subtract
#     else:
#         print("I don't know that one")
#
#
# add = create_math_function('add')
# print('5 + 2 = {}'.format(add(5, 2)))
#
# subtract = create_math_function('subtract')
# print('5 - 2 = {}'.format(subtract(5, 2)))
# *
# Nice nested function! Now that you've implemented the subtract() function, you can keep going
# to include multiply() and divide(). I predict this game is going to be even bigger than Fortnite!

# Notice how we assign the return value from create_math_function() to the add and subtract
# variables in the script. Since create_math_function() returns a function, we can then call
# those variables as functions.
# ----------------------------------------------------------------
# x = 50
#
# def one():
#   x = 10
#
# def two():
#   global x
#   x = 30  # re-assigns x to be 30, grabs from global scope using keyword "global"
#
# def three():
#   x = 100
#   print(x)  # this prints the local x value, because x is called in the function, hence it prints "100"
#
# for func in [one, two, three]:
#   func()
#   print(x)  # prints 30, because global x has been modified in "two" function
#
#   # hence answer is "50 30 100 30"
# ----------------------------------------------------------------
# call_count = 0
#
#
# def my_function():
#     # Use a keyword that lets us update call_count
#     global call_count
#     call_count += 1
#
#     print("You've called my_function() {} times!".format(
#         call_count
#     ))
#
#
# for _ in range(20):
#     my_function()
#     *
# ----------------------------------------------------------------
# def read_files():
#     file_contents = None
#
#     def save_contents(filename):
#         # Add a keyword that lets us modify file_contents
#         nonlocal file_contents
#         if file_contents is None:
#             file_contents = []
#         with open(filename) as fin:
#             file_contents.append(fin.read())
#
#     for filename in ['1984.txt', 'MobyDick.txt', 'CatsEye.txt']:
#         save_contents(filename)
#
#     return file_contents
#
#
# print('\n'.join(read_files()))
# *
# ----------------------------------------------------------------
# def wait_until_done():
#     def check_is_done():
#         # Add a keyword so that wait_until_done()
#         # doesn't run forever
#         global done
#         if random.random() < 0.1:
#             done = True
#
#     while not done:
#         check_is_done()
#
#
# done = False
# wait_until_done()
#
# print('Work done? {}'.format(done))
# *
# Stellar scoping! By adding global done in check_is_done(), you ensure that the
# done being referenced is the one that was set to False before wait_until_done()
# was called. Without this keyword, wait_until_done() would loop forever because
# the done = True in check_is_done() would only be changing a variable that is
# local to check_is_done(). Understanding what scope your variables are in will
# help you debug tricky situations like this one.
# ----------------------------------------------------------------
# def return_a_func(arg1, arg2):
#     def new_func():
#         print('arg1 was {}'.format(arg1))
#         print('arg2 was {}'.format(arg2))
#
#     return new_func
#
#
# my_func = return_a_func(2, 17)
#
# # Show that my_func()'s closure is not None
# print(my_func.__closure__[0] is not None)
# *
#
# def return_a_func(arg1, arg2):
#     def new_func():
#         print('arg1 was {}'.format(arg1))
#         print('arg2 was {}'.format(arg2))
#
#     return new_func
#
#
# my_func = return_a_func(2, 17)
#
# print(my_func.__closure__ is not None)
#
# # Show that there are two variables in the closure
# print(len(my_func.__closure__) == 2)
# *
#
# def return_a_func(arg1, arg2):
#     def new_func():
#         print('arg1 was {}'.format(arg1))
#         print('arg2 was {}'.format(arg2))
#
#     return new_func
#
#
# my_func = return_a_func(2, 17)
#
# print(my_func.__closure__ is not None)
# print(len(my_func.__closure__) == 2)
#
# # Get the values of the variables in the closure
# closure_values = [
#     my_func.__closure__[i].cell_contents for i in range(2)
# ]
# print(closure_values == [2, 17])
# *

# Case closed! Your niece is relieved to see that the values she passed to return_a_func() are still
# accessible to the new function she returned, even after the program has left the scope of return_a_func().
#
# Values get added to a function's closure in the order they are defined in the enclosing function
# (in this case, arg1 and then arg2), but only if they are used in the nested function. That is,
# if return_a_func() took a third argument (e.g., arg3) that wasn't used by new_func(), then it
# would not be captured in new_func()'s closure.

# ----------------------------------------------------------------
# def my_special_function():
#     print('You are running my_special_function()')
#
#
# def get_new_func(func):
#     def call_func():
#         func()
#
#     return call_func
#
#
# new_func = get_new_func(my_special_function)
#
#
# # Redefine my_special_function() to just print "hello"
#
# def my_special_function():
#     print('hello')
#
#
# new_func()
# # you still get the original message even if you redefine my_special_function() to only print "hello".
# *

# def my_special_function():
#     print('You are running my_special_function()')
#
#
# def get_new_func(func):
#     def call_func():
#         func()
#
#     return call_func
#
#
# new_func = get_new_func(my_special_function)
#
# # Delete my_special_function()
# del my_special_function
#
# new_func()
# *

# def my_special_function():
#     print('You are running my_special_function()')
#
#
# def get_new_func(func):
#     def call_func():
#         func()
#
#     return call_func
#
#
# # Overwrite `my_special_function` with the new function
# my_special_function = get_new_func(my_special_function)
#
# my_special_function()
# *
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# DECORATORS
# ----------------------------------------------------------------
# def my_function(a, b, c):
#   print(a + b + c)
#
# # Decorate my_function() with the print_args() decorator
# my_function = print_args(my_function)
#
# my_function(1, 2, 3)
# *


# # Decorate my_function() with the print_args() decorator using decorator syntax.
# @print_args
# def my_function(a, b, c):
#   print(a + b + c)
#
# my_function(1, 2, 3)
# *
# ----------------------------------------------------------------
# def print_before_and_after(func):
#   def wrapper(*args):
#     print('Before {}'.format(func.__name__))
#     # Call the function being decorated with *args
      # Call the function being decorated and pass it the positional arguments *args.
#     func(*args)
#     print('After {}'.format(func.__name__))
#   # Return the nested function/# Return the new decorated function.
#   return wrapper
#
# @print_before_and_after
# def multiply(a, b):
#   print(a * b)
#
# multiply(5, 10)
# *



# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------