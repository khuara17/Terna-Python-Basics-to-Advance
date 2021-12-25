
###########  Passing a List as an Argument  #######
'''
You can send any data types of argument to a function (string, number, list, dictionary etc.),
and it will be treated as the same data type inside the function.

E.g. if you send a List as an argument, it will still be a List when it reaches the function:

'''

# mylist = [7,8.7,'hi',(3,4)]
# mytuple = (4,5)
# def printo(mylist,mytuple):
#     for i in mylist:
#         print(i)

# printo(mytuple,mylist)



##########  Keyword Arguments  ###########
'''
You can also send arguments with the key = value syntax.

This way the order of the arguments does not matter.

'''


# def my_function(a,b,c):
#     print(f"youngest one is {b}")

# my_function(b = 'Ajit',c = 'sujit',a = 'manjit')



############ Default Parameter Value  ########
'''
If we call the function without argument, it uses the default value:

'''

# def my_function(a,b,c):
#     print(f"youngest one is {b}")

# my_function('g','h','f','t')  # TypeError: my_function() takes 3 positional arguments but 4 were given
 
def my_function(firstname,lastname,age=0):
    print(f"youngest one is {firstname,age}")

# my_function('rohit','sharma')


########### Arbitrary Arguments, *args  #######
'''

If you do not know how many arguments that will be passed into your function, 
add a * before the parameter name in the function definition.

This way the function will receive a tuple of arguments, and can access the items accordingly:
'''
 
def my_function(child1,*child):
    print(f"youngest one is {child,child1}")

# my_function('Luffy','Naruto','Zoro','sasuke')


#############   Arbitrary Keyword Arguments, **kwargs  ###########

'''
If you do not know how many keyword arguments that will be passed into your function,
add two asterisk: ** before the parameter name in the function definition.

This way the function will receive a dictionary of arguments, and can access the items accordingly:

'''
def myfunction(**name):
    print(name)

# myfunction(fname= 'dksl',lname='gggf',ftname ="dsds")

########### The pass Statement  #######
'''
function definitions cannot be empty, but if you for some reason have a function definition with no content,
put in the pass statement to avoid getting an error.

# '''
# def f():
#     pass


############# passing function to another function ############
'''
_ __ body ____    ____exp_______ 
100      110       111       120

   square x
'''


'''

___5 __
   100
   x z
'''

x = 5
z = x

# x = square
# x^2 + 1

# (a+b)^2 = a^3 + 2ab + b^3
def exp(x,a,b):
    # print(x)
    c = x(a) + 2*a*b + x(b)
    return c


def square(n):
    return n**2

# def x(n):
#     return n**2

def cube(n):
    return n ** 3



# print(square(3))
res = exp(cube,2,3)
print(res)


##############  Quesions ##################

'''
Q1. Create a function that takes a number as its parameter and returns another function. 
The returned function must take a list of numbers as its parameter, 
and return a list of the numbers divided by the number that was passed into the first function.

Examples
first = factory(15)
# returns a function first.

lst = [30, 45, 60]
# 30 / 15 = 2, 45 / 15 = 3, 60 / 15 = 4

first(lst) ➞ [2, 3, 4]

'''
