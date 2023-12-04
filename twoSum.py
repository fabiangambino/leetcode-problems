# PROBLEM 

"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 
Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
"""

# EXAMPLES - uncomment individually to test with function call below

#nums = [10,20,30,40,50]
#target = 80

#nums = [2,7,11,15]
#target = 9

#nums = [3,2,4]
#target = 6

#nums = [3,3]
#target = 6

#MY CODE

"""
We have one array of integers and one target value. 
The goal is to return the index values of the two integers that when added equal the target value.
We must compare each integer with all of the other integers in the array. 
When comparing an array against itself, we can use a nested loop. 
"""

"""
CODING STEPS:
1. We define the function and the arguments it accepts. nums is an array of integers. target is an integer.
2. We create an empty array called indexes. This will later be used to add the two index values of the integers that when added equal target and to be returned.
3. We create our first for loop by index so that we can compare both indexes and values. Range establishes the index values for the first integer to the last in nums.
4. We create our nested for loop in identical fashion as the first. We can now access the indexes and values of both and compare them against each other.
5. We then set conditionals to check values as we loop through and compare integers.
6. The first part of the conditional checks that the indexes between both arrays are not the same since we don't want to compare ana integer against itself.
7. The second part of the condition checks if the integer values when added together equal the target.
8. If both conditional statements are True since we are using the AND logical operator, then the index value i is added to the indexes array.
9. Finally, the indexes array is returned with the index locations.
"""

def twoSum(nums, target):
    indexes =[]                                             #an array for the indexes to be returned later
    for i in range(0, len(nums)):                           #outer for loop (1st list to be compared to 2nd list). We do these by index so we can access/compare indexes and values. 
        for j in range(0, len(nums)):                       #inner for loop (2nd list to be compared to 1st list). We do these by index so we can access/compare indexes and values.
            if i != j and nums[i] + nums[j] == target:      #conditional disallowing comparison at the same index and checking if values equal target
                indexes.append(i)                           #adding index value to the index array once conditional is met  
    return indexes                                          #returning the index array

# FUNCTION CALL WITH TERMINAL PRINT

#print(twoSum(nums, target))

# SKIPPING EXTRA UNNECESSARY ITERATIONS

"""
At each iteration, each integer is compared only against the integers that come after it
by setting a starting range of i + 1 in the nested loop. When setting up the loops in this fashion we are saving 
ourselves from re-iterating over value comparisons we've already made through previous iterations.

We  can also remove the indexes array and the appending process to simply return an array of the index values directly.
We can do this by wrapping brackets around the return values or implementing list().
"""

def two_sum(nums, target):
    for i in range(0, len(nums)):
        #print(f"The current i value being compared is {nums[i]}.")
        for j in range(i+1, len(nums)):
            #print(f"   against j value {nums[j]}.")
            if nums[i] + nums[j] == target:
                return [i, j]
            
# FUNCTION CALL WITH TERMINAL PRINT

#print(two_Sum(nums, target))

# ITERATION BY ITERATION

"""
On the first iteration of the outer loop i is equal to 0. 
Moving onto the first iteration of the inner j loop j is equal to 1 (i +1 ... 0 + 1)
Once through the conditional, the next iteration of the j loop sets j equal to 2 while i from the outer loop remains 0.
Once through the conditional, the next iteration of the j loop sets j equal to 3 while i from the outer loop remains 0.
Once through the conditional, the next iteration of the j loop sets j equal to 4 while i from the outer loop remains 0.

On the second iteration of the outer loop i is equal to 1. 
Moving onto the first iteration of the inner j loop j is equal to 2 (i + 1 ... 1 + 1)
Once through the conditional, the next iteration of the j loop sets j equal to 3 while i from the outer loop remains 1.
Once through the conditional, the next iteration of the j loop sets j equal to 4 while i from the outer loop remains 1.

On the third iteration of the outer loop i is equal to 2. 
Moving onto the first iteration of the inner j loop j is equal to 3 (i + 1 ... 2 + 1)
Once through the conditional, the next iteration of the j loop sets j equal to 4 while i from the outer loop remains 1.

On the fourth iteration of the outer loop i is equal to 3. 
Moving onto the first iteration of the inner j loop j is equal to 4 (i + 1 ... 3 + 1)

On the fifth iteration of the outer loop i is equal to 4.
Moving onto the first iteration of the inner j loop j is equal to 5 (i + 1 ... 4 + 1)
range(5,5) returns an empty array with nothing to iterate over. The last integer has already been compared to all others.
"""

# SOLVING THE PROBLEM USING WHILE LOOP INSTEAD OF FOR LOOP

"""
On the first iteration, the i counter is set to 0 and the outer loop is entered. 

Once in the outer loop, the j counter is set to i + 1 forcing comparison to start one index over.

Once in the inner loop, we check if the two values equal the target. If so, we return a list of both index numbers.

We increment j by 1 at the end of the inner loop and increment i by 1 at end of the outer loop.

The process continues until all comparisons have been made and the condition is met.

"""

def two_sum_v2(nums, target):
    i = 0
    while i < len(nums):
        j = i + 1
        while j < len(nums):
            if nums[i] + nums[j] == target:
                return [i, j]
            j += 1
        i += 1

# FUNCTION CALL WITH TERMINAL PRINT

#print(twoSum(nums, target))


# HIGHER LEVEL SOLUTION TO BE REVIEWED

"""
#!/usr/bin/env python3


def two_sums(nums, target):

    # Returns a map where the key is the number and the value of its index
    # for for example if nums is [2,5,1] the result map would be
    # {2: 0, 5: 1, 1: 2}
    def make_map(nums):
        map = {}
        for i in range(0, len(nums)):
            map[nums[i]] = i
        return map

    # Convert the input into the special map so we can quicky lookup in constant time
    # the numbers we desire to find
    lookup = make_map(nums)

    # Iterate through all nums...
    for i in range(0, len(nums)):
        value = nums[i]
        # Subtract the target from the number, this is the number we know we
        # must look for to assert success. For example if value is 6 and target
        # is 9, we must look for a 3 in nums (or its map representation for faster
        # lookups) to assert success
        lookfor = abs(value - target)
        found = lookup.get(lookfor)
        # One last caveat, if the value we need is == the input we need to check its
        # index to make sure we aren't picking the number we are iterting over. Thats
        # why we also store the index in the map too
        if found is not None and found != i:
            return [i, found]
    return []


assert two_sums([10, 20, 30, 40, 50], 80) == [2, 4]
assert two_sums([3, 3], 6) == [0, 1]
assert two_sums([2, 7, 11, 15], 9) == [0, 1]
assert two_sums([3, 2, 4], 6) == [1, 2]

so a few things:
1. theres no nested for loops, a map is used, map lookups are instantaneous big O of 1 (constant time) 
2. you don't need to keep a result list because the directions say you can just assume theres one answer or no answer, so if i find the two indicies , i immediately return

3. abs() is a mathematical function, absolute value
4. i could probably make this less lines of code but i wanted to make it as obvious as possible for and high readability

5. the solution in english is this

if i have a number and i wanna know if two numbers make a target then i can use simple subtraction to infer what i'm looking for, for example 

[3,2,4] with a target of 6 , if i'm iterating over 3 and i know that the target is 6 then 6 - 3 = 3  i know i need to look for another 3 to have the solution, my conditional isn't hit i move on

i see 2 so 6 - 2 is 4 i need to look for a 4, i see a 4 then i have the solution
"""

# Note: Something odd occurs when there are duplicates, since maps can
# only contain unique keys the map will be updated with the latest index
# The algorithm below however is agnostic to this issue
