# PROBLEM

"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

 

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].
"""

# EXAMPLES

# MY CODE

I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000


XIV = 14
XXIV = 24 
XIX = 19 
XXIX = 29

XL = 40
XLIV = 44 
LVIII = 58
XC = 90
XCVI = 96

CD = 400
CDLV = 455 
CMLXXXVI = 986

# NOTES 

"""
The maxmimum number of times a roman numeral can consecutively follow itself is 3. For example III is 3 but the proper written form
of the number 4 is IV. These rules must be followed to write a roman numeral in proper form.

The normal process of counting and writing roman numerals is from largest to smallest. We convert the numerals to numbers by adding
from left to right. 

There are 6 instances where subtraction is used.

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.

We made need multiple functions to enforce roman numeral counting rules. Some letters cannot be repeated 4 times in a row while 
others cannot appear in certain orientations. Having several functions to enforce rules and validate whether a number is entered
in  valid roman numeral form will help.
"""

# CODING STEPS

"""
1. We can create a map/dictionary of the values of each roman numeral and it's corresponding arabic number.
2. We can create a running total equal to zero to which we will add as we loop through the roman numberal string.
3. Next we can loop through the string and start building our arabic number.
4. Once there aren't any numberals left, we can stop iterating and return our arabic number.
"""

"""Dictionary"""

roman = {
    "I" : 1,
    "V" : 5,
    "X" : 10,
    "L" : 50,
    "C" : 100,
    "D" : 500,
    "M" : 1000
}

test_value1 = "XVI"
test_value2 = "XXXX"
test_value3 = "IV"
test_value4 = "IIII"

# SAMPLE MASTER FUNCTION TO BE WORKED ON

def roman_to_integer(rom_num):
    arabic = 0
    for numeral in rom_num:
        arabic += roman[numeral]
    return arabic

print(roman_to_integer(test_value3))

"""
I should probably write other functions to test the positioning and roman numeral rules to ensure accurate counting
as += does not represent a full picture of roman numeral counting structure.
"""


