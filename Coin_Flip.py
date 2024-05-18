import random
ISN = (random.randrange(start= 1, stop= 65535))
print("RANDOM is ", ISN)
print("TYPE OF ISN:", type(ISN))
if ISN%2 ==0:
    print("It's a HEAD")
else:
    print("TAIL")
