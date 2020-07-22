## TUPLES --------------
  # tuples are immutable sequences like Strings
  # Lists are mutable - can be changed once previously defined
t = (1,2,3)
print(t)
print(t[1])

# can also hold mixed data types.
z = ('a',True,123)
print(z)



## SETS ----------------
  # sets are unordered collections of unique elements


X = set()
X.add(1)
X.add(2)
X.add(4)
X.add(0.2)
print(X)

  # Sets will not allow something to be added multiple times
  # like a list with repeated elements -
converted = set([1,1,1,1,2,2,2,2,3,3,3,3])
print(converted)

## Booleans -----------------------
  # booleans are just True and False
 #True - #False
 #0 - 1
