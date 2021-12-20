############# Type Conversion ########

a = (2,3,[45])
b = str(a)
# print(type(b))

# set
# dict

# print(len(a))
########### Tuple ##################
''' 1. Tuples are used to store multiple items in a single variable.
    2. Tuple items are unchangeable(Immutable), and allow duplicate values.
    3. Tuples are written with round brackets. '''

'''
Method	        Description
count()	    Returns the number of times a specified value occurs in a tuple
index()	    Searches the tuple for a specified value and returns the position of where it was found
'''

a = (5, 8.9, 5, True, [6,8,(80,'kl')])
b = [4,5,6,()]

# a[2] = 6  #TypeError: 'tuple' object does not support item assignment

# print(a[2:4])
# print(a)

### Updating the elements of tuple ####

# x = list(a)
# x[2][4][5] = 6
# x.append(90)
# a = tuple(x)
# print(a)



######## Unpacking ############

# c,d,e = [4,5,[6,7]]

# print(c,d,e)


##### Joining Tuple ####

# a = (5, 8.9, 5, True, [6,8,(80,'kl')])
# b = (4,5,6,())
# c = a + b


c = [5, 6]
# c = c * 12
c = c + [7]
# print(c)







########### Set ##################
''' 1. Set items are unchangeable(Immutable), and do not allow duplicate values and unordered.
    2. Sets are written with curly brackets.. '''


'''
Method	        Description
add()	    Adds an element to the set
clear()	    Removes all the elements from the set
copy()	    Returns a copy of the set
discard()	Remove the specified item
pop()	    Removes an element from the set
remove()	Removes the specified element
update()	Update the set with the union of this set and others
'''

myset = {4,5,6,7}  #{7,6,5,4} Similar
myset2 = {7,10}
# print(myset[2]) #TypeError: 'set' object does not support indexing

########### Add items to the set  ##########

# myset.add('value')

myset.update(myset2)
# print(myset) 


###### Remove Item from the set ######

# myset.discard('values')
# myset.remove(8)
# myset.clear()
# del myset
# myset.pop()
# print(myset) 


###### Exercise ######
# Remove all the duplicates

mylist = [5,6,7,5,5,6,7]
# print(list(set(mylist)))



########### Dictonary ############

''' 1. Dictionaries are used to store data values in key:value pairs.
    2. A dictionary is a collection which is changeable(mutable) and does not allow duplicate Keys.
    3. Dictionaries are written with curly brackets, and have keys and values.
    4. For keys we can have only non-iterable data types
    5. For values we can have any data type. '''


'''
Method	            Description
clear()	        Removes all the elements from the dictionary
copy()	        Returns a copy of the dictionary
fromkeys()	    Returns a dictionary with the specified keys and value
get()	        Returns the value of the specified key
items()	        Returns a list containing a tuple for each key value pair
keys()	        Returns a list containing the dictionary's keys
pop()	        Removes the element with the specified key
popitem()	    Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	    Updates the dictionary with the specified key-value pairs
values()	    Returns a list of all the values in the dictionary
'''


########## Accessing an element of dict ############

# print(mydict['key'][6][0])

###### Adding an item to dict #####

# mydict[7] = 85

######## Updating valuess ##########
# mydict[4] = 5657
# mydict.update({5.6:7})

############# Removing an item from dict #######

# mydict.pop('key')
# mydict.popitem()
# # del mydict
# mydict.clear()
# print(len(mydict))


######### Special Methods ########
mydict = {
    4 : 'first',
    5.6 : [5,6],
    True: 4,
    'key' : {6: (6,90)},
    7 : 85
    }
# print(mydict.keys())
# print(mydict.values())
# print(mydict.items())



############### Applying Loops on data stuctures #############

# for i,j in mydict.items():
#     print(i,j)

# for i in mylist:
