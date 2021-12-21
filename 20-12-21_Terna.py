######## Def ##########

# mystr = 'hi'

# mystr = '''
# fhjsdfhsdjfsdjsdfkljsdfkljsdf
#fgdf
# '''

# print(len(mystr))

###### String Slicing ##

# If you are accessing the single index and it is our of index then you will get error
# If you are using string slicing and out of index, then it will go till last element

# print(mystr[2:8])
# print(mystr[8])

# print(mystr[::-1])
mystr = "python"

# print(mystr[-3:-1])

######### String Formatting ########

### Method 1 #####

age = 23
friendage = 289

# print("My age is {}  and my friends age is {}".format(45,friendage))

#### Method 2 #####

# print("My age is {1}  and my friends age is {0}".format(45,friendage))

#### Method 3 ####

# print(f"My age is {age}  and my friends age is {1}")



####### Methods ########

a = "fg"

# print(a.upper())
# print(a.lower())
# print(a.replace("l","B"))
# print(a.count('l'))
# print(a)
# print(a.strip())
# print(a.split(","))
# print(a.islower())
# print(a.capitalize())
# print(a.isdigit())


#### Join #####

# Join method takes all the elements from iterables and convert them into a string

# a = ["Hi","Python","is","best",6]

# x = "->".join(str(i) for i in a)

# print(x)

###### Escapae characters #########

a = "Hi , This is very \"Import\""
a = "Hi , This is very \nImport"
a = "Hi , This is very \tImport"
a = "Hi , This is very \\Import"

# print(a)





######## Operators ###########

#   Operators are used to perform operations on variables and values.

# 2 + 3  = 5


#1. Python Arithmetic Operators
'''
Arithmetic operators are used with numeric values to perform common mathematical operations:

Operator	Name	    Example	
+	    Addition	    x + y	
-	    Subtraction	    x - y	
*	    Multiplication	x * y	
/	    Division	    x / y	
%	    Modulus	        x % y	
**	    Exponentiation	x ** y	
//	    Floor division	x // y	
'''
a = 5
b = 2
'''
  2.5
2)5 
- 4
____
  1



2^2  
'''
# print(a//b)




#  Python Comparison Operators
'''
Comparison operators are used to compare two values:

Operator	Name						Example	
==			Equal						x == y	
!=			Not equal					x != y	
>			Greater than				x > y	
<			Less than					x < y	
>=			Greater than or equal to	x >= y	
<=			Less than or equal to		x <= y	

'''
# a = 4
# b = 4
# print(a >= b)







'''
Python Logical Operators
Logical operators are used to combine conditional statements:

Operator	Description														                    Example	
and 		  Returns True if both statements are true						      x < 5 and  x < 10	
or			  Returns True if one of the statements is true					    x < 5 or x < 4	
not			  Reverse the result, returns False if the result is true		not(x < 5 and x < 10)

'''
x = 7
print(not(x < 5 or  x < 10))

