# Dictionaries

# A Dictionary is another mutable set type that can store any number of Python objects, 
# including other set types. Dictionaries consist of pairs (called items) of keys 
# and their corresponding values. While this data structure is known as a dictionary in Python
# you'll see the same structure referred to as an associative array or hash table in other languages. 
# In general, hash table is the most generic term. 

# A dictionary is an unordered collection of objects.
# Values are accessed using a key.
# can shrink or grow as needed.
# contents of dictionaries can be modified
# dictionaries can be nested


# 2 dictionaries created two different ways

# below "Sun" is the key and "Sunday" is the value for example
# weekend = {"Sun": "Sunday", "Sat": "Saturday"} #literal notation
# capitals = {} #create an empty dictionary then add values
# capitals["svk"] = "Bratislava" # here the key is inside the [] square brackets and value is after = 
# capitals["deu"] = "Berlin"
# capitals["dnk"] = "Copenhagen"
# print(weekend["Sun"])

# Removing values

# 2 ways to remove a key-value pair

# value_removed = capitals.pop('svk') # will remove the key 'svk' and return it's value
# del capitals['dnk'] # will delete the key, and not return anything
# print(capitals["svk"])


# Nested Dictionaries
# nesting is also allowed with dictionaries. They can contain lists and tuples

# context = {
#     'questions': [
#     {'id' : 1, 'content': 'Why is the light in the fridge but not the freezer?'},
#     {'id' : 2, 'content': 'Why don\'t sheep shrink when wet?'},
#     {'id' : 3, 'content': 'Why cars drive on the parkway and park in the driveway?'},
#     {'id' : 4, 'content': 'Why are they apartments all stuck together?'}
#     ]
# }
# print(context.values()) # this built-in method prints all of the dictionary's values


# Conditionals

# if - elif - else

# ninja = {
#     "first_name":"Michael",
#     "last_name":"Benton",
#     "age" : 37,
#     "favorite_languages" : ["Python", "Java", "JavaScript"]
# }

# if ninja["age"] > 100:
#     print("30 is the new 40!")
# elif ninja["age"] < 30:
#     print("Hey there kiddo!")
# else:
#     print("Whatcha gonna do babay!") # Prints "Whatcha gonna do babay!"


# Another conditional example
# note: indendation needs to be corrected for the print statements to work

    # x = 12
    # if x > 50:
    #     print("bigger than 50")
    # else:
    #     print("smaller than 50")
    # # because x is not greater than 50, the second print statement is the only one that will execute
    
    # x = 55
    # if x > 10:
    #     print("bigger than 10")
    # elif x > 50:
    #     print("bigger than 50")
    # else:
    #     print("smaller than 10")
    # # even though x is greater than 10 and 50, the first true statement is the only one that will execute, so we will only see 'bigger than 10'
    
    # if x < 10:
    #     print("smaller than 10")
    # nothing happens, because the statement is false   

