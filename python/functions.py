# DEFINE FUNCTIONS
# IN SNAKE CASE - SNAKE_CASE
def my_function(param1="default"):
        print("My first python function")
# WILL NOT PRINT ANYTHING
# MUST CALL FUNCTIONS
# LIKE THIS - AFTER PRINT ---
## my_function()

def new_func(param1="default2"):
        print("second python function")
new_func()



# USING PARAMATER and .format
## WILL ADD IN VALUE OF KEY NAME
def new_func(param2="default2"):
        print("second python function {}".format(param2))
new_func()




## FUNCTION WITH DOCUMENTATION STRING
## DOCUMENTS FUNCTIONS

def doc_string(param3="default3"):
    """
    THIS IS THE DOCSTRING
    """
    print("second python function {}".format(param3))
doc_string()



## PRINTING SOMETHING IN A FUNCTION
def hello():
    print("hello")
hello()

# RETURNING SOMETHING IN A FUNCTIONS
# RETURNS AN OBJECT TO USE AS A VARIABLE
# WHICH U MAY CALL LATER ON
def hello():
    return "hello again"
result = hello()
print(result)


### DEFINING FUNCTION WITH INPUT TO ADD NUMBERS
## WHILE SEARCHING FOR TYPE
def addNum(num1,num2):
    return num1 + num2
result = addNum('2','3')
print(type(result))



 ## PRINT ERROR MESSAGE FUNCTION
 ## SHORT AND SWEET
 #################
def addNum(num1,num2):
    if type(num1) == type(num2) == (10):
        return num1 + num2
    else:
        print("SORRY I NEED INTEGERS NOT STRINGS")
result = addNum('2','3')



########
#LAMBDA EXPRESSION
#########
## FUNCTION THAT ACCEPTS OTHER FUNCTIONS AS INPUT PARAMATERS
## WE WILL INTRODUCE FILTER FUNCTIONS
## NORMAL FUNCTION EXAMPLE
mylist = [1,2,3,4,5,6,7,8]

def even_bool(num):
    return num%2 == 0


evens = filter(even_bool,mylist)
print(list(evens))

## LAMBDA EXPRESSION EXAMLPE
## THE FILTER FUNCTION TAKES IN 2 arguments
# a function and a sewucene - returns those items in the sequce which are true




mylist = [1,2,3,4,5,6,7,8]
evens = filter(lambda num:num%2 == 0,mylist)
print(list(evens))

### SPLITTING A SEARCH RETURN FUNCTION

####
tweet = "GO SPORTS!" "#SPORTS"
result =tweet.split("#")
print(result)
### SPLITTING A SEARCH RETURN FUNCTION
### RETURING ONLY A CERTAIN PART OF LIST

tweet = "GO SPORTS!" "#SPORTS"
result =tweet.split("#")[1]
print(result)


 #####
### IN OPERATOR
# IS X IN THE LIST
# FALSE
print('x' in [1,2,3])

# TRUE
print('x' in [1,2,3,'x'])
