"""
You are given two integer arrays nums1 and nums2 sorted in non-decreasing order,
and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.



Not my solution.
This is a two pointers approach. 
both arrays are sorted. So we look for the larger of the two elements starting at the back of both arrays. 

both pointers start at the end. 

say we have pointer A and B

while there are elements to merge: 
    if we have not checked all elements in nums1 and the last element of nums1 is larger than the last elem of nums2: 
       write that value to the write_index
       decrement A
    else: 
        write the value of nums2[B]
        decrement B 
    decrement the write_index


In a nutshell, we are writing to the allocated merge spaces (the zeros) starting at the back. 
one pointer is used for the location in nums1 and the other is used for the location in nums2. 

We move one pointer at a time and update the write location, checking the values between nums1 and nums2
for the respective pointers as we go. 




"""


def merge( nums1, m, nums2, n):
    i = m - 1
    j = n - 1
    write_index = m + n - 1
    
    while j >= 0: # there are elements to be merged
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[write_index] = nums1[i]
            i -= 1
        else:
            nums1[write_index] = nums2[j]
            j -= 1
        write_index -= 1
    return nums1

print(merge([2,0], 1, [1], 1))




    
