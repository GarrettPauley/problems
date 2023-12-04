import unittest
"Implement an alogorithm that determines if a string has all unique characters"

def isUnique(s: str): 
    chars = {}
    for i in s: 
        chars[i] = 1
    if len(chars.keys()) == len(s): 
        return True
    else: 
        return False
 
class testIsUnique(unittest.TestCase): 
    def testUnique1(self): 
        test = "thisisnotunique"
        self.assertEqual(isUnique(test), False)
    def testUnique2(self): 
        test = "nose"
        self.assertEqual(isUnique(test), True)


if __name__ == '__main__': 
    unittest.main()