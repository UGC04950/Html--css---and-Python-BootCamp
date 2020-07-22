# Lists (ARRAYS)

my_list = [1,2,3,4,5,6,7,8,9,10]
print(my_list)

# Multiple Integer Types
my_list = [1,2,3,25.5,True,]
print(my_list)
# Nested List
my_list = ['nestedlist1', 1,2,3,25.5,True, 'nestedlist2', [4,5,6,]]
print(my_list)

# Lenth of List
my_list = [1,2,3]
print(len(my_list))

my_list = ['a','b','c','d']
print(my_list)

# Indexing and slicing on Lists
print(my_list[0])
print(my_list[:3])
print(my_list[::2])


# Adding items to a list -
# reassignment with index calls on a list defining it as a mutable item
mylist = ['a','b','c','d']
print('Before Reassignment')
print(my_list)

my_list[0] = 'NEW ITEM'
print('After Reassignment')
print(my_list)


# adding (appending) new item to List - does not affect items in list already just adds new item
my_list = ['a','b','c']
print(my_list)

my_list.append(['d','e','f'])
print(my_list)

# extending the list instead of printing nested list
new_list = ['h','i','j']
new_list_two = ['k','l','m']
new_list.extend(new_list_two)
print(new_list)


# removing something from a list
new_list_3 = ['a','b','c','d','e','f','g']
new_list_3.pop()
print(new_list_3)

# removing from index - (a) in this case
new_list_3 = ['a','b','c','d','e','f','g']
new_list_3.pop(0)
print(new_list_3)


# removing object from list and saving it to a new item (g) in this case
new_list_3 = ['a','b','c','d','e','f','g']
item = new_list_3.pop()
print(new_list_3)
print(item)

# Revserse
new_list_3 = ['a','b','c','d','e','f','g']
new_list_3.reverse()
print(new_list_3)

# sort -
new_list_3 = ['b','a','d','e','c','g','f']
new_list_3.sort()
print(new_list_3)


# Nested List Index
my_list_4 = [1,2,['x','y','z']]
print(my_list_4[2])
print(my_list_4[2][1])


# List Comprehension - for loop flattened out into a list - (columized)
matrix = [[1,2,3],[4,5,6],[7,8,9]]

first_col = [row[0] for row in matrix]
print(first_col)
