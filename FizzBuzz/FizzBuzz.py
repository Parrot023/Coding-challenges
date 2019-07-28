#Multiples
multiple1 = 3
multiple2 = 5

#My first version

""" for i in range(1, 101):
    
    if i%multiple1 == 0 and i%multiple2 != 0:
        print("Fizz")
    
    elif i%multiple2 == 0 and i%multiple1 != 0:
        print("Buzz")

    elif i%multiple1 == 0 and i%multiple2 == 0:
        print("FizzBuzz")
    else:
        print(i)

 """
#Better version (inspired by: Tom scott video)

""" for i in range(1,101):
    
    if i%multiple1 == 0 and i%multiple2 == 0:
        print("FizzBuzz")

    elif i%multiple1 == 0:
        print("Fizz")
    
    elif i%multiple2 == 0:
        print("Buzz")

    else:
        print(i) """


# Even better version made completely by myself build on top of the 
# tom scott version in 5 minutes
# Shorter and more dynamic
# if Fizz and Buzz and 3 and 5 isnt enough for you 
# fell free to add as many more as you want

multiples =  [3, 5]
terms = ["Fizz", "Buzz"]

for i in range(1,101):

    output = ""

    for j in range(len(multiples)):
        if i%multiples[j] == 0:
            output += terms[j]

    if output == "":
        output = i

    print(output)