"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

This is a dynamic programming problem. 
Intuitively, if we are at the top step, we know that we got there by travelling
one step or two steps. 

If we add (number of ways to get to the n-1 step) + (number of ways to get to the n-2 step)
then we have our answer. 

Base Case: There is zero or one step - there is 1 way to climb 0 steps and there is 1 way to climb 1 step
Recursive Case: 

"""

climbed = {} 
def climbStairs(n): 
    if n < 2: 
        return 1
    if n in climbed.keys():  # memoization
        return climbed[n]
    else: 
        climbed[n] = climbStairs(n-1) + climbStairs(n-2)
    
    return climbed[n]


print(climbStairs(2)) # 2
print(climbStairs(3)) # 3
print(climbStairs(1)) # 1


