########### Presendance & Associativity ###########
'''
Category	        Operator	        Associativity

Parentheses	         () []           	Left to right                Highest
Exponentiation        **                Right to left
Multiplicative  	* / % //	        Left to right
Additive	        + -	                Left to right
Shift	            << >>	            Left to right
Relational	        < <= > >=	        Left to right
Equality	        == !=	            Left to right
Bitwise AND	            &	            Left to right
Bitwise XOR	            ^	            Left to right
Bitwise OR	            |	            Left to right
Assignment	= += -= *= /= %=>>= <<= &= ^= |=	Right to left
Comma	                ,	            Left to right                 Lowest
'''

# x = 3 * ( ( ( (6+4) *2 ) - 10 ) //2 ) // 4 * 2
# print(x)

'''
x = 6

(6+4) = 10
10 * 2 = 20
20 -10 = 10
10 //2= 5
3 * 5 = 15
15 // 4 = 3
3 * 2 = 6
x = 6
'''


# x= 15 // 5 + 2 = 7


########### in-built functions ###########
'''
Function	Description

sum()	    Sums the items of an iterator
bin()	    Returns the binary version of a number
enumerate()	Takes a collection (e.g. a tuple) and returns it as an enumerate object
eval()	    Evaluates and executes an expression
filter()	Use a filter function to exclude items in an iterable object
len()	    Returns the length of an object
map()	    Returns the specified iterator with the specified function applied to each item
max()	    Returns the largest item in an iterable
min()	    Returns the smallest item in an iterable
round()	    Rounds a numbers
sorted()	Returns a sorted list
sum()	    Sums the items of an iterator
zip()	    Returns an iterator, from two or more iterators
'''

# 1. Map 
x = ("yash","Shweta","Amogh")
x = ("3","5","7")
# Syantax
# map(function,iterables)

# x = map(int,x)
# print(type(list(x)[0]))






########### Problem Solving #############

# 1. 
'''
Take the comma seperated numbers from user and find the largest number from it.
'''
# 2,3,4,5
# myNo = list(map(int,input("Enter the numbers speperated by commas:- ").split(",")))
# print(myno)

# Method 1
# lar=myNo[0]
# for x in myNo[1:]:
#     if x > lar:
#         lar=x

# print(lar)

# Method 2

# myList = list(map(int,input('Enter the number with comma for split : ').split(",")))

# myList.sort(reverse=True)

# print(myList[0])


#2.
'''
In input list, every number repeats at least once, except for two.
Write a program that will print the two unique numbers.

Examples

return_unique([1, 9, 8, 8, 7, 6, 1, 6]) ➞ [9, 7]

return_unique([5, 5, 2, 4, 4, 4, 9, 9, 9, 1]) ➞ [2, 1]

return_unique([9, 5, 6, 8, 7, 7, 1, 1, 1, 1, 1, 9, 8]) ➞ [5, 6]
'''


# mylist = list(map(int,input("Enter the numbers speperated by commas:- ").split(",")))

# op = []
# for i in mylist:
#     if mylist.count(i) == 1:
#         op.append(i)

# print(op)
# 1, 9, 8, 8, 7, 6, 1, 6

list = list(map(int, input("Enter Numbers saperated by comma: ").split(",")))
dict = {
    1 : 1,
    9 : 1,
    8 : 2,

}
for x in list:
    if x in dict.keys():
        dict[x] = dict[x]+1
    else:
        dict[x] = 1
out = []
for x in dict:
    if dict[x] == 1:
        out.append(x)
print(out)


# 3.
'''
A number is said to be Harshad if it's exactly divisible by the sum of its digits. 
Take a number from user and check whether a number is a Harshad or not.

Examples
is_harshad(75) ➞ False
# 7 + 5 = 12
# 75 is not exactly divisible by 12
 
is_harshad(171) ➞ True
# 1 + 7 + 1 = 9
# 9 exactly divides 171
 
is_harshad(481) ➞ True

is_harshad(89) ➞ False

is_harshad(516) ➞ True

is_harshad(200) ➞ True
'''
