# if 1 is less than 2 print first block of code
if 1 < 2:
    print('first block')
# Will not print because 1 is not greater than 2
if 1 > 2:
    print('second block')


# if else statements

if 1 < 2:
    print("hello")
else:
    print("last")


# else if statements
#elif

# if 1 is less than 2 print first block of code
if 1 < 2:
    print('whats up')
elif 3 == 3:
    print('elif ran')
# Will not print because 1 is not greater than 2
else:
    print('printing again')


# LOOPS
# FOR LOOPS
# Iterate through a list
list = [1,2,3,4,5,6]
# for item in variable created
for item in list:
        # code here
    print('hello')


# FOR LOOP IN dictionary
# NOT PRINTED IN ORDER DICTIONARIES DO NOT RETAIN ANY order
d = {"sam": 1, "frank": 2, "dan": 3}

for item in d:
    print(item)

# TO GET KEYS OUT
for k in d:
    print(k)
    print(d[k])






#
# Iterate through tuple
# list with  3 tuples
mypairs = [(1,2),(3,4),(5,6)]
for dog in mypairs:
# Tuple Unpacking into for LOOP

    for (tup1,tup2) in mypairs:
        print(tup1)
        print(tup2)


### WHILE LOOPS
# USING PRINT FORMATTING
    #i = 1

#hile 1<5:
    # print("i is: {}".format(i))
#    i = i +  1


## LIST COMPREHENSION
# REMOVING x ** 2 =
x = [1,2,3,4]

out = []
for num in x]
    out.append(num**2)
    print(out)
####  LIST COMPREHENSION CORRECTLY
