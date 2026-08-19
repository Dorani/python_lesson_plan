#3. Two Sum

#Classic HackerRank/LeetCode pattern.

def two_sum(nums, target):
    lookup = {}
    i = 0
    
    for num in nums:
        complement = target - num
        if complement in lookup:
            return [lookup[complement], i]
        
        lookup[num] = i
        i += 1
        
    return []


nums = [2, 7]
target = 9

print(two_sum([2, 7, 11, 15], 9))
# [0, 1]

print(two_sum([3, 2, 4], 6))
# [1, 2]

print(two_sum([3, 3], 6))
# [0, 1]

print(two_sum([1, 5, 3, 7], 10))
# [1, 3]