
def solution(nums):
    pass


print(solution([5,4,3,2,1]))
print(solution([5,1,1,2,0,0]))

import random

def quicksort(nums):
    if(len(nums) < 2): 
        return nums
    # pick the pivot
    pivot = nums[random.randint(0, len(nums)-1)]
    # split the lists into less than and greater than lists. 
    less = [x for x in nums if x < pivot]
    equal = [x for x in nums if x == pivot]
    more = [x for x in nums if x > pivot] 

    return quicksort(less) + equal + quicksort(more)

print(quicksort([3,4,1,2, 0, 0]))





# Quicksort

# pick a random pivot point in the array. 
# quicksort (elems less than the pivot) + pivot + quicksort(elems greater than the pivot )

def quicksort(nums): 
    if len(nums) < 2: 
        return nums
    pivot = nums[random.randint(0, len(nums)-1)]
    less = [x for x in nums if x < pivot]
    equal =[x for x in nums if x == pivot]
    more = [x for x in nums if x > pivot]
    return quicksort(less) + equal + quicksort(more)