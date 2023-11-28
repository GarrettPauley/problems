
""" 
You are given a positive integer num consisting of exactly four digits. Split num into two new integers new1 and new2 by using the digits found in num. Leading zeros are allowed in new1 and new2, and all the digits found in num must be used.

For example, given num = 2932, you have the following digits: two 2's, one 9 and one 3. Some of the possible pairs [new1, new2] are [22, 93], [23, 92], [223, 9] and [2, 329].
Return the minimum possible sum of new1 and new2.

we could split the number in one of 3 places

e.g., num = 1234

1|234
12|34
123|4

The minumum solution will always be split down the middle, otherwise we are guaranteed to have a three digit number. 
Even with leading zeros. 
0001
0| 001
or 
000|1 
This is the same as 00|01

if we sort the digits of the number, we can construct minimum pairs. 
minimize the tens digit with the two smallest numbers. minimize the ones digit with the third and fourth smallest numbers. 

e.g., 9876 = [6,7,8,9]
smallest pairs = (68) and (79)


"""
def solution(num):
    d = sorted (str(num))
    smallest_tens_digit = d[0]
    second_smallest_tens_digit = d[1]
    smallest_ones_digit = d[2]
    second_smallest_ones_digit = d[3]
    return (smallest_tens_digit + smallest_ones_digit) + (second_smallest_tens_digit + second_smallest_ones_digit)







# You are given a positive integer num consisting of exactly four digits. Split num into two new integers new1 and new2 by using the digits found in num. Leading zeros are allowed in new1 and new2, and all the digits found in num must be used.

# For example, given num = 2932, you have the following digits: two 2's, one 9 and one 3. Some of the possible pairs [new1, new2] are [22, 93], [23, 92], [223, 9] and [2, 329].
# Return the minimum possible sum of new1 and new2.

# we could split the number in one of 3 places

# e.g., num = 1234

# 1|234
# 12|34
# 123|4



