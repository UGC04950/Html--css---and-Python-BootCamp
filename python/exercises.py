#############
##Problem 1 ##
##############

# Given the string :
s = 'django'

#use indexing to print out the following:
 #d
print(s[0])
 # o
print(s[-1])
 # djan
print(s[:4])
 # jan
print(s[1:4])
 # go
print(s[4:6])
#bonus: use indexing to reerse the string
mylist = ['j','a','n','g','o']
mylist.reverse()
s = mylist
print(s)



#############
##Problem 2 ##
##############
 # Given this nested list :
l = [3,7,[1,4,'hello']]
# Reassign "hello" to be "goodbye"
l[2][2] = 'goodbye'

#############
##Problem 3 ##
##############
# using keys and indexing grab hello from the following dictionaries:

d1 = {'simple_key': 'hello'}

 # print(d1['simple_key'])

d2 = {'k1': {'k2':'welcome'}}
# print(d2['k1']['k2'])

d3 = {'k1':[{'nestkey': ['this is deep', ['hello']]}]}
# grab k1 key. now 1st element in that last
# grab nest_key dictionary - Grab 2nd item in list at index 1 -
# then grab 0 - 1st item in that list

# print(d3['k1'][0]['nest_key'][1][0])

#############
##Problem 4 ##
##############
# Use a set to find the unique values of the list below:
mylist = [1,1,1,1,1,2,2,2,3,3,3,3]

set(mylist)
print(set(mylist))

#############
##Problem 5 ##
##############
#you are given two variables:
age = 4/***/

#use print formatting to print the following string:
"Hello my dog's name is Sammy and he is 4 years old"

print("Hello my dog's name is {a} and he is {b} years old".format(a = age, b = name))
