# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# 1*, 2*, 3, 4*, 5, 6, 7*, 8*, 9
# 3 + 5 + 6 + 9 = 23

# Find the sum of all the multiples of 3 or 5 below 1000.
# Find the sum of all the multiples of 8 or 13 between 500 and 700.
# multiple1 = 8
# multiple2 = 13
# lower_limit = 500
# higher_limit = 700


def sum_of_multiples(multiple1, multiple2, lower_limit, higher_limit):
    sum = 0
    # Iterate from 1 to 1000
    for i in range(lower_limit, higher_limit): # 1, 2, 3, 4, 5, ..., 999
        # if multiple of 3 or 5
        if (i % multiple1 == 0 or i % multiple2 == 0): # False, False, True, False, True
            # add that to the variable 'sum'
            sum += i # 0 + 3 = 3, 3 + 5 = 8

    # return sum
    return sum

# final_sum = sum_of_multiples(8, 13, 500, 700)
# print(final_sum)

print(sum_of_multiples(8, 13, 500, 700))