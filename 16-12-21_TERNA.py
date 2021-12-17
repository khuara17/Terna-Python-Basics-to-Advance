# #variables = containers to store values
# #keywords = reserved words in python
# #identifiers = names given to class or functions.

# #variable naming rules.
# myvar = "apple"
# # 4myvar = "apple" #name cannot start with a digit
# my_var = "apple"
# #my$var = "apple" #only underscore can be used no other special characters
# MYVAR = "apple"
# myvar2 = "apple"
# _my_var = "apple"
# #my var = "apple" # no blank space allowed
# myVar = "apple"
# #$var_No1 = "apple" # $ not allowed

# a , b, c = "apple", "Mango", "Grapes"
# d = e = f ="Pineapple"
# print(a)
# print(b)
# print(c)

fruits = ["apple", "Mango", "Grapes"]
# g, h, i = fruits #right side of equal to is assigned to the left variable
# fruits = g, h, i
# print(d)
# print(e)
# print(f)


# print(g)
# print(h)
# print(i)

# # Basic Datatypes
# # 1.Integers
# # 2.Floating Numbers
# # 3.Strings
# # # 4.Booleans
# # # 5.None

# #Integers
# x = 5
# y = 2558534789
# z = -2547896314

# print(type(x))
# print(type(y))
# print(type(z))

# #Float
# a = 1.548
# b = 1.0
# c = -5.1245
# d = 456e4
# e = 2347E8
# f = -4361e123
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))
# print(type(f))

# #Complex
# g = 6j #j is imaginary
# h = -6j
# i = 6+9j
# print(type(g))
# print(type(h))
# print(type(i))

# #Strings
a = "Hello World"
# b = "Hello"
# c = "H"# Single letter also considered as string i.e.irrespective of length
# print(a)
# print("world")
# print(a[1]) # access the characters
# print(len(b)) #length of the string
print("WORLD" in a) # check if word is present
# print("World" not in b) # check if word is not present

# for x in "lotus":
#     print(x)

#Slicing of string
#    012345678910
d = "Hello World" 
print(d[1:7]) #end index value is skipped