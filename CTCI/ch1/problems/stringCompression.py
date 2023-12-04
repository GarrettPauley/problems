import unittest
"""
String Compression: 
given a string, return a string with compressed duplicates. 
e.g., 
aaabbbccc -> a3b3c3
aabc -> a2bc
abc -> abc

"""
def solution(s: str):

    final = ""
    streak = 1
    i = 0 # indexer
    j = 0 # position in the string

    while i < len(s):
        if j + 1 == len(s):  # we are on a streak, and have reached the end of the string. 
            final += s[i] + str(streak)
            break
        if s[j] == s[j+1]: # current character matches the next character
            streak += 1
            j += 1

        else: #
            if streak != 1: # concatenate the character at i, with the number of times it appears in the streak. 
                final += (s[i] + str(streak))
                i += streak # move the indexer to the place the streak ended. 
                j = i # sync the indexers

            else: # no streak, add current character and increment indexer
                final += s[i]
                i += 1
            # reset our streak
            streak = 1
    return final
    

# Runtime Analysis: 
# We must traverse the whole string. 
# Average case == Worst case == Best case == O(n)



class testIsUnique(unittest.TestCase): 
    def testCase1(self): 
        # delete test case
        test = "aaaa"
        self.assertEqual(solution(test),"a4")
    def testCase2(self): 
        # insert test case
        test = "aaabc"
        self.assertEqual(solution(test),"a3bc")
    def testCase3(self): 
        # replace test case
        test = "abcde"
        self.assertEqual(solution(test), "abcde")

    def testCase4(self): 
        test = "aabbcc"
        self.assertEqual(solution(test),"a2b2c")







if __name__ == '__main__': 
    unittest.main()
