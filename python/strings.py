# Strings
# Basics
 # Single or Double Quote
'hello'
"hello"

# Indexing
my_string = 'abcdefg'
print(my_string[0])

# Slicing
print(my_string[2:])

 # up to but not including that index
print(my_string[:3])


# define start and ending point - up to but not including 5
print(my_string[2:5])


# define step size
print(my_string[::2])


# Uppercase
x = my_string.upper()
print(x)

# Lowercase -
x = my_string.lower()
print(x)


# Splitting Strings - default it will split on white space created
example_two = 'Hello World'
x = example_two.split()
print(x)

x = example_two.split('e')
print(x)


# print formatting (interperlation)
x = "Insert another string here: {}".format("INSERT ME!")
print(x)

x = "Item One: {} Item Two: {}".format("dog" , "cat")
print(x)

x = "Item One: {x} Item Two: {x}".format(x = "dog" , y = "cat")
print(x)
