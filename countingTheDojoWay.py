# Counting, the Dojo Way. Print int's 1-100. If divisible by 5, print "Coding" instead. 
# If divisible by 10, print "Coding Dojo".
for i in range(0, 101):
    if i % 10 == 0: # using modulus here. This means if i % by 10 has no remainder
        print("Coding Dojo")
    elif i % 5 == 0: # using elif here instead of another if statement so that it drops through loop
        print("Coding")
    else: 
        print(i)
