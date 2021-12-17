# Values Greater than Second - Write a function that accepts a list and creates a new list containing only 
# the values from the original list that are greater than its 2nd value. 
# Print how many values this is and then return the new list. If the list has less than 2 elements, 
# have the function return False
# Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
# Example: values_greater_than_second([3]) should return False

def values_greater_than_second(list):
    if len(list) < 2:
        return False


def values_greater_than_second(list):
    if len(list) < 2:
        return False
    output = [] # outputs a new list
    for i in range(0,len(list)): # we need a count here
        if list[i] > list[1]: # accessing the hard value here the second element in the array
            output.append(list[i]) # use append 
    print(len(output))
    return output


print(values_greater_than_second([5,2,3,2,1,4])) # spaces above the print line are important here
print(values_greater_than_second([3]))
