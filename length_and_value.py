# This Length, That Value: 
# Write a function that accepts two integers as parameters: size and value. 
# The function should create and return a list whose length is equal to the given size, 
# and whose values are all the given value.
# Example: length_and_value(4,7) should return [7,7,7,7]
# Example: length_and_value(6,2) should return [2,2,2,2,2,2]

def length_and_value(size,value): # 1. accepts two ints as params, size and value
    output = [] # 2. the function should create and return a list (creation is here)
    for i in range(0, size): # 3. create the for loop
        output.append(value)
    return output # 2. return the list

print(length_and_value(4,7)) #size is 4 and the value is 7
print(length_and_value(6,2))
