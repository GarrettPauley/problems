
def solution(num): 
    # while there are digits
    digits = str(num)
    permutations = [ [w,x,y,z] for w in digits for x in digits for y in digits for z in digits ]

    smallest = num
    for p in permutations: 
        first_sum = int(p[0]) + int(''.join(p[1:]))
        second_sum = int(''.join(p[:2])) + int(''.join(p[2:]))
        third_sum = int(''.join(p[0:3])) + int(p[3])
        print(f"new perm: {first_sum}\t{second_sum}\t{third_sum} ")
        smallest_sum = min(first_sum, second_sum, third_sum)
        if smallest_sum < smallest: 
            smallest = smallest_sum
    return smallest




print(solution(2932))

