################### Functions ############
# Syntax
'''
def function_name(inut parameter):
    Body of function
'''

# Function defination
def addition(a,b):   
    c = a + b
    print(c)
    return c


a = 66
b = 4
c = 23

# res = addition(c,b)   # Function Call

# print(res)


####### Exercise ##########
'''
Create a application called Calculator (Function name :- Calculator) , 
Where you will take 3 values from user as input para
3 inputs :- no1, no2, opertor 

On the basis of opertor :- + , - , * , /

return the operation result.
'''



# Input 
# Program Logic 
# Result 

a=int(input("enter the number 1 "))
b=int(input("enter the number 2 "))
c=input("enter the operator +,-,*,/ ")

def calculator(a,b,c):
    if(c=='+'):
        sum = a+b
    elif(c=='-'):
        sum = a-b
    elif c == '*':
        sum = a * b
    elif c == '/':
        sum = a / b
    else:
        sum = 'Invalid Option selected'

    return sum

res=calculator(a,b,c)
print(res)
