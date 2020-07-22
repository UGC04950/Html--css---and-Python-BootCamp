## defining function and prininting it

#def hello():
#    return "hello"
#result = hello()

#print(result)


def addNum(num1,num2):
    if type(num1) == type(num2) == type(10):
            return num1+num2
    else:
            return "sorry, i need integers!"
result = addNum(1,9)
print(result)
