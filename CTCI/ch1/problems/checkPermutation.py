import unittest
"Implement an alogorithm that determines if a string has all unique characters"

def check_perm(a: str, b: str): 
    a_permutations = perm(a)
    b_permutations = perm(b)

    if b in a_permutations or a in b_permutations: 
        return True
    return False

def check_palindrome_permutation(s: str): 
    """ Given a string, check if it is a permutation of a palindrome. Ignore case and non-letter chars"""
    s = s.lower().replace(' ', '')
    permutations = perm(s)
    for word in permutations: 
        if isPalindrome(word): 
            return True
    return False

def isPalindrome(s: str): 
    if s == s[::-1]: 
        return True
    return False

     

def insert(s: str, c: str,  index: int): 
    return s[:index] + c + s[index:]

def perm(s: str):  
    if len(s) == 1: 
        return s
    else: 
        lastChar = s[-1]
        previousPerm = perm(s[:-1])
        perms = []
        for word in previousPerm:
            for i in range(len(s)):
                perms.append(insert(word,lastChar, i))
        return perms


class TestPermutation(unittest.TestCase): 
    def test_perm1(self): 
        a = "tac"
        b = "cat"
        self.assertEqual(check_perm(a, b),True)
    def test_perm2(self): 
        a = "dad"
        b =  "add"
        self.assertEqual(check_perm(a,b), True)
    def test_perm3(self): 
        a = "mom"
        b =  "nom"
        self.assertEqual(check_perm(a,b),False)

    def test_perm_palindrome(self): 
        a = "Tact Coa"
        self.assertEqual(check_palindrome_permutation(a),True)



if __name__ == '__main__': 
    unittest.main()
