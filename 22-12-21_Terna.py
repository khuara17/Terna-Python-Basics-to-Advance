############## Loops ###################
# for , while

############# 1. for Loop #######

# Syntax

'''
for variable in range(initial value,end value,increament value)
'''
'''
Assign the value to the variable
Check the condition 
Execute whatever present in the body of for loop
Increment the value by whatever defined in for loop

The conition in for loop is  "<" ,,, not "<="
'''

# mylist = [1,2,3,4,5,6,7,8,8,9]

# for i in mylist:
#     print(i)

# for val in range(0,3,1):
#     print("computer")

# val = 0 , 0 < 3
# print val :- 0

# val = val + 1  = 0 + 1 = 1 ,  1 < 3
# print val :- 1

# val = val + 1  = 1 + 1 = 2 ,  2 < 3
# print val :- 2

# val = val + 1 = 2 + 1 = 3,  3 < 3

######### Variation ##############
#1.
#for val in range(11):   # Defaults : 1. Initial val = 0 , 2. Increment val = 1

#2. 
# for val in range(4,10):    # Defaults : 2. Increment val = 1
#     print(val)   

# print(range(1,5))


############  for loop with only membership operator #########
s = ("dshfga",3,4,5.6)
dicto = {
    4:5,
    'hi' : 667,
    34 : 12
}
# for i in dicto:
#    print(i) 


####### For else #######

# for x in range(6):
#     for i in range(3):
#         print(x)
# else:
#     print("Finished !")




############ While Loop ########

#### Syantax #####
'''
while condition:
    Body of while
'''
# t = 2
# while t < 10:
#     if t % 2 == 0:
#         print(t)
#     t += 1 # t = t + 1
# else:
#     print("finished")

# while True:


############# Break ############

mylst = ["Apple","Orange","Banana","mango"]
# for i in mylst:
#     if i == "Banana":
#         break
#     print(i)


########## Continue #####

# while i < 4:
#     i += 1
#     if i == 2:
#         continue
#     print(i)
    
    
    


########## Pass #############

for i in mylst:
    pass

##########   While with string ########

# s = 'abcde'
# i  = 0
# while i < len(s):
#     print(s[i])
#     i += 1
#     print(s[i])
#     i += 1


# Write a program that will take two numbers from user say a and b, 
# you have to return the multiplication of those numbers , You cannot use the * operator.

num1=int(input("Enter a number for num1: "))
num2=int(input("Enter a number for num2: "))
product= 0
for i in range (1,num1+1):  
    product=product+num2       
print(product)

num1 = 2
num2 = 4


# 4 * 3 = 12 => 4 + 4 + 4 or 3 + 3 + 3+3 = 12