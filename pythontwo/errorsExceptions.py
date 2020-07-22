# USED FOR LARGER BLOCKS OF CODING WHERE USER INPUT IS - INPUT 

try:
    f = open("simple.txt","r")
    f.write("Test Write to simple Text!")

except:
    print("ERROR: COULD NOT FIND FILE OR READ DATA!")
finally:
    print("I ALWAYS WORK NO MATTER WHAT!")
