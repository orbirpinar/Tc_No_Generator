#! /usr/bin/python
import random

def generate_random_number(element_count):
    random_numbers = []
    for i in range(element_count):
        random_number = random.randint(1,9)
        print(random_number)
        random_numbers.append(random_number)
    print(random_numbers)
    return random_numbers

def generate_tc_no():
    random_numbers = generate_random_number(9)
    even = random_numbers[0::2]
    print(f"EVEN {even}")
    odd = random_numbers[1::2]
    print(f"ODD {odd}")
    total_odd = sum(odd) 
    total_even = sum(even)
    tenth = (7 * total_even - total_odd) % 10
    random_numbers.append(tenth)
    total = sum(random_numbers)
    eleventh = total % 10
    random_numbers.append(eleventh)
    print(f"RANDOM NUMBER LIST {random_numbers}")
    return "".join(map(str,random_numbers))

tc = generate_tc_no()
print(tc)


        
