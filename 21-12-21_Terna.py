'''
Python Identity Operators

Identity operators are used to compare the objects, not if they are equal, 
but if they are actually the same object, with the same memory location:

Operator	Description	                                                Example	
is 	        Returns True if both variables are the same object	        x is y	
is not	    Returns True if both variables are not the same object	    x is not y	
'''
x = ["Oslo","Melburn"]
y = ["Oslo","Melburn"]
z = x



# _ _ ______     _               _ 
# 0 1      10    11              21

#    x  z               y

# print(x is z)


# print(x is y)


# print(x == y)


'''
Python Membership Operators
Membership operators are used to test if a sequence is presented in an object:

Operator	Description	Example	Try it
in 	        Returns True if a sequence with the specified value is present in the object	x in y	
not in	    Returns True if a sequence with the specified value is not present in the object	x not in y	

'''
# x = ["Oslo","Melburn"]
# y = '456'
# # print("oslo" in x)
# print('4' in y)  #TypeError: argument of type 'int' is not iterable


'''

Python Bitwise Operators
Bitwise operators are used to compare (binary) numbers:

Operator Name	Description
& 	            AND	Sets each bit to 1 if both bits are 1
|	            OR	Sets each bit to 1 if one of two bits is 1
^	            XOR	Sets each bit to 1 if only one of two bits is 1

'''

    # 16 8 4*1 + 2*0 + 1* 1 

x = 4   #100 
# &
y = 5   #101
# --------------
#        001 = 1

# print(x^y)






'''
Python Assignment Operators
Assignment operators are used to assign values to variables:

Operator	Example	Same As	
=	        x = 5	x = 5	
+=      	x += 3	x = x + 3	
-=	        x -= 3	x = x - 3	
*=	        x *= 3	x = x * 3	
/=	        x /= 3	x = x / 3	
%=	        x %= 3	x = x % 3	
//=	        x //= 3	x = x // 3	
**=	        x **= 3	x = x ** 3

'''
x = 5
# x **= 3
# print(x)




######### If Else #############

x = 7
y = 5

# if x < y:
#     y *= 2
#     print(f"x is smaller than {y}")
# else:
#     x += 5
#     print(f"{x} is smaller than x") 

###### Elif ######

# if x <= y:
#     y *= 2
#     print(f"x is smaller than {y}")
# elif x == y:
#     y -= 2
#     print(f"{x} is equal to {y}")
# else:
#     x += 5
#     print(f"{x} is greateer than x") 

######## Input ##########

# x = float(input("Enter the number : "))
# print(type(x))

###### Problem 1 ##########
'''
you are creating a app for a school, where you will take marks from user and you will prin their category

80       -  Dist
50 to 79 -  First class
35 to 49 -  second class
0 to 34  -  Fail
'''

x = int(input("ener your marks "))
if x >= 80:
    print("dist")
elif x >= 50 and x <= 79:
    print("first class")    
elif x >= 35 and x <= 49:
    print("second class")   
else:
    print("you are fail")    







