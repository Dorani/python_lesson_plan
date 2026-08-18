#3. Two Sum

#Classic HackerRank/LeetCode pattern.

def two_sum(nums, target):
    lookup = {}
    
    for i, num in enumerate(nums):
        compliment = target - num
        
        if compliment in lookup:
            return [lookup[num, i]]
        else:
            lookup[num] = i
            
    return []