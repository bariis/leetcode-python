"""
17. Letter Combinations of a Phone Number
@Level: Medium

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
"""

class Solution:
    def letterCombinations(self, digits):
        digit_to_letters = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z']
        }

        def backtrack(combination, next_digits):
            if len(next_digits) == 0:
                output.append(combination)
            else:
                for letter in digit_to_letters[int(next_digits[0])]:
                    backtrack(combination + letter, next_digits[1:])
        output = []
        if digits:
            backtrack("", digits)
        return output
