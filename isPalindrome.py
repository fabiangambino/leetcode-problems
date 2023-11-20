# PROBLEM

"""
Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
 

Follow up: Could you solve it without converting the integer to a string?
"""

# EXAMPLES
#num = 121
#num = -121
#num = 10

# MY CODE

"""
A palindrome is a word, phrase, or sequence that reads the same backwards as it does forwards. An example would be "RACECAR".
In this case we are checking if integers are palindromes, 121 for example backwards also reads 121 which is a palindrome.
234 in this case reads 432 backwards and therefore is not a palindrome.
"""

"""
CODING STEPS:
We can break the integer into individual pieces or if converted to a string, by individual characters (numbers).
Once broken into smaller pieces, we can reconstruct it in reverse and then compare the two arrangements.
If they are equal, we can return true, otherwise, we can return false.
"""
    
def isPalindrome(num):
    reverse = ""                    # an empty string to be constructed in reverse for use in comparison later
    for n in reversed(str(num)):    # looping through the a reversed list of the integer string conversion
        reverse += n                # adding each individual character to the reverse string at each iteration
    if str(num) == reverse:         # conditional checking equivalence between both arrangements
        return True                 # returning True if equivalence is found
    return False                    # returning false otherwise
                 
# FUNCTION CALL WITH TERMINAL PRINT 

print(isPalindrome(num))




