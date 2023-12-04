""" 
You are given two strings s1 and s2 of equal length.
 A string swap is an operation where you choose two indices in a string 
 (not necessarily different) and swap the characters at these indices.

Return true if it is possible to make both strings equal by performing at most one string swap 
on exactly one of the strings. Otherwise, return false.

Example 1:

Input: s1 = "bank", s2 = "kanb"
Output: true
Explanation: For example, swap the first character with the last character of s2 to make "bank".
Example 2:

Input: s1 = "attack", s2 = "defend"
Output: false
Explanation: It is impossible to make them equal with one string swap.
Example 3:

Input: s1 = "kelb", s2 = "kelb"
Output: true
Explanation: The two strings are already equal, so no string swap operation is required.

"""


import unittest
def solution(a: str, b: str):
    count = 0 
    if a == b: 
        return True
    if sorted(a) != sorted(b): 
        return False
    for i in range(len(a)): 
        if a[i] != b[i]: 
            count += 1
    if count != 2: 
        return False
    return True

        



   

# Runtime Analysis: 


class TestCases(unittest.TestCase): 
    def testCase1(self): 
        a = "bank"
        b = "kanb"
        self.assertEqual(solution(a,b),True)
    def testCase2(self): 
        a = "pale"
        b = "ealp"
        self.assertEqual(solution(a,b),True)

    def testCase3(self): 
        a = "sleep"
        b = "lseep"
        self.assertEqual(solution(a,b),True)

    def testCase4(self): 
        a = "attack"
        b = "defend"
        self.assertEqual(solution(a,b),False)
    def testCase5(self): 
        # more than one way to make the swap. return false
        a = "att"
        b = "tat"
        self.assertEqual(solution(a,b),False)








if __name__ == '__main__': 
    unittest.main()
