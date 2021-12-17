# countdown function: Create a function that accepts a number as an input. 
# Return a new list that counts down by one, from the number (as the 0th element) 
# down to 0 (as the last element).
# Example: countdown(5) should return [5,4,3,2,1,0]



def countdown(num):
    output = [] # array is the new list
    for i in range(num,-1,-1): # decrement by 1, and then go to -1 because it is not included! only go to 0
        output.append(i) # using append method
    return output # no print statement with just this - we need the line below:

print(countdown(5))
