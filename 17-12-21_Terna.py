############### Slicing ############

# a = 'himalaya'
a = [4,5,6,7,8,9]

# a[2:5]

# print(a[2:])

########## Data Types ############

############ 1. List  ################
'''1. Lists are used to store multiple items in a single variable.
   2. List items are  changeable(Mutable), and allow duplicate values.
   3. List items are indexed, the first item has index [0], the second item has index [1] and so on...
   4. Lists are written with square brackets.
   5. list can have any datatype in it.'''

   ############# List Methods ###############
'''
     Method	    Description

    append()	Adds an element at the end of the list
    clear()	    Removes all the elements from the list
    copy()	    Returns a copy of the list
    count()	    Returns the number of elements with the specified value
    extend()	Add the elements of a list (or any iterable), to the end of the current list
    index()	    Returns the index of the first element with the specified value
    insert()	Adds an element at the specified position
    pop()	    Removes the element at the specified position
    remove()	Removes the item with the specified value
    reverse()	Reverses the order of the list
    sort()	    Sorts the list
'''
### Definiation #####

a = [4,5,6,7,5.6,'string',[4,5],[6.7,[6,'fg',['python']]]]
b = [3,90]
###### Adding elements to list ######

# a.append(8.7)
# a.insert(1,'hello')
# a.extend(b)

#### Removing an element ############
# print(a)
# a.pop()
# a.remove(5.6)
# del a
# a.clear()
# print(a)

### Accessing elements of list ######
# print(a[7][1][2][0][1])

# print(a[6][1])

##### Changing the elements of list #####
a = [7,5,'string',5,[4,5],[6.7,[6,'fg',['python']]]]

# a[7][1][0]="hello"

# a[4][1][1][1] = 't'  #TypeError: 'str' object does not support item assignment
# a[4] = 6.5
# 'hello'
# print(a)



######### Special Methods ####################

# print(a.count(5))
# print(a.index(5))
# a = 'Pasad'   # String does not have any built in methods to reverese.
# a.reverse()
# print(a[::-1])
# c  = complex()
# a = [3j,4j,5j]
# a.sort(reverse=True)
# print(a)

x= a.copy()
print(x)

