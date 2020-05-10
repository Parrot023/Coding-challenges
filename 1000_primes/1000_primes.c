// This is my first ever C program
// It is a line to line translation of my 1000_primes.py python script to find primes
// By trying out both the Python and the C script you can really see how much faster C is
// Date: 13/04/2020 GMT + 2 

#include <stdio.h>
#include <time.h>



int main() {

    time_t time_before = time(NULL);

    int primes_to_find;
    printf("How many primes do you want ");
    scanf("%d", &primes_to_find);

    int primes_found[primes_to_find];

    int current_number = 1;
    int number = current_number - 1;

    int index = 1;
    int found = 0;

    primes_found[0] = 2;

    while (1)
    {
        //printf("index %d\n", index);
        number = current_number - 1;
        if (current_number % 2 != 0) {
            while (number != 0)
            {
                if(current_number%number == 0) {
                    //printf("not prime %d\n", current_number);
                    break;
                }
                number -= 1;
            }
            if (number == 1) {
                //printf("prime %d\n", current_number);
                found ++;
                primes_found[index] = current_number;
                index += 1;

                printf("Primes found %d\n", index);

            }
            
        }
        if (found > primes_to_find) {
            break;
        }
        current_number += 1;
    }
    
    time_t time_after = time(NULL);
    
    for (int i = 0; i < primes_to_find; i ++) {
        printf("prime: %d\n ", primes_found[i]);
    }

    printf("Found %d primes in %d seconds", primes_to_find, time_after - time_before);

    return 0;

}