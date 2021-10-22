"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]

"""

def combination(digits):
    
    if len(digits) == 0:
            return

    lst=['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']

    temp = []
    rv = []

    def doit(digits):
        if digits is None:
            rv.append(''.join(temp))
            return
        for i in lst[int(digits[0])-2]:
            temp.append(i)
            if len(digits) > 1:
                doit(digits[1:])
            else:
                doit(None)
            temp.pop()

    doit(digits)
    return rv

if __name__ == '__main__':
    output = combination('23')
    print(output)