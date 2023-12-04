import unittest
"""
One Away: 
There are three edits that we can make. 

Insert a character
Delete a character
replace a character

given an input string and a target, return true if the input can be transformed to the target 
with zero or one edit. 

We will only consider lowercase letters.

"""
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
           'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
           'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
            'y', 'z']


def solution(s: str, target: str): 

    if s == target: 
        return True
    # If the length difference between the two strings 
    # is greater than 1, it cannot be transformed in one step
    if abs(len(s) - len(target)) > 1: 
        return False

    # Delete
    for i in range(len(s) - 1): 
        if s[:i] + s[i+1 :] == target: 
            return True
    # Replace
    for i in range(len(s) + 1):
        for letter in letters: 
            if s[:i-1] + letter + s[i:] == target: 
                return True
    # Insert
    for i in range(len(s) + 1):
        for letter in letters: 
            if s[:i] + letter + s[i:] == target: 
                return True
    return False
    

# Runtime Analysis: 

#first two checks are O(1)
# Delete step is O(n)
# Replace step is O(26 * n) == O(n)
# Insert step is same as replace step. 

# worst case is O (n + n + n) ==  O(n)





class testIsUnique(unittest.TestCase): 
    def testCase1(self): 
        # delete test case
        test = "pale"
        target = 'ale'
        self.assertEqual(solution(test, target),True)
    def testCase2(self): 
        # insert test case
        test = "nose"
        target = "nosey"
        self.assertEqual(solution(test,target), True)
    def testCase3(self): 
        # replace test case
        test = "nosep"
        target = "nosey"
        self.assertEqual(solution(test,target), True)

    def testCase4(self): 
        # too long
        test = "nose"
        target = "asdlkfjasdf"
        self.assertEqual(solution(test,target), False)







if __name__ == '__main__': 
    unittest.main()