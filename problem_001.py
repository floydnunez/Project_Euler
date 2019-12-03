import math

grand_limit = 1000

multiples_of_3 = []
multiples_of_5 = []

def get_all_multiples_up_to(multiples_of, limit):
    result = []
    for index in range(1, math.ceil(limit / multiples_of) + 1):
        number = index * multiples_of
        if number < limit:
            result.append(number)
    return result

multiples_of_3 = get_all_multiples_up_to(3, grand_limit)
multiples_of_5 = get_all_multiples_up_to(5, grand_limit)


#deduplicate
for a_multiple_of_5 in multiples_of_5:
    if a_multiple_of_5 in multiples_of_3:
        multiples_of_3.remove(a_multiple_of_5)

total = 0
for elem in multiples_of_3:
    total += elem
for elem in multiples_of_5:
    total += elem

print(total)
