# at first the goal was to get the sum of the first 1000 primes
# but when i had gotten the first 1000
# i was like wy not get the first 10000
# an then i was like
# why not let the user specify how many primes the wont
# and then i kinda got away from the sum thing
# but hey at the end it tells you how long it took so......
# i think its pretty good
from datetime import datetime
primes_found = [2]
current_number = 1
number = current_number-1
primes_needed_to_find = int(input("How many primes do you want "))
start = datetime.now()
while True:
    number = current_number - 1
    print(number)
    if current_number%2 != 0:
        while number != 0:
            if current_number%number == 0:
                break
            number -= 1
        if number == 1:
            primes_found.append(current_number)
    if len(primes_found) == primes_needed_to_find:
        break
    current_number += 1
print(primes_found)
end = datetime.now()
print("Found " + str(len(primes_found)) + " Primes in " + str(datetime.timestamp(end) - datetime.timestamp(start)) + " secends")