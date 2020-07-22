# Dictionaries are pythons version of tables
# Allow mapping with key - value pairs
# Do not retain any order
# "name" : "value"
# can be integer or string - can nest as well
my_stuff = {"key1": "value"}
print(my_stuff)


my_stuff = {"key1": "value", "key2": "150,000",}
print(my_stuff["key2"])

# a key with another dictionary inside of it. As well as another list.
# sould not be this nested but it is possible.
my_stuff = {"key1": "value", "key2": "150,000","key3":{"123":[1,2,"grabMe"]}}
print(my_stuff["key3"]['123'][2])


# Can also call things off of ^^^^^^^-
# should not be this nested but it is possible.
my_stuff = {"key1": "value", "key2": "150,000","key3":{"123":[1,2,"grabMe"]}}
print(my_stuff["key3"]['123'][2].upper())

#####  Real World Example
menu = {"lunch": "pizza", "breakfast": "eggs",}
print(menu["lunch"])

 #Change key Value pair if needed (permanantely)
menu = {"lunch": "pizza", "breakfast": "eggs",}
menu["lunch"] = "burger"
print(menu["lunch"])

#ADD key Value pair if needed (permanantely)
menu = {"lunch": "pizza", "breakfast": "eggs",}
menu["lunch"] = "burger"
menu["dinner"] = "pasta"
print(menu)
