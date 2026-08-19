# // Example 1:

# // Input: nums = [1,2,3,1], k = 3
# // Output: true
# // Example 2:

# // Input: nums = [1,0,1,1], k = 1
# // Output: true
# // Example 3:

# // Input: nums = [1,2,3,1,2,3], k = 2
# // Output: false

# //i and j in the array
# //such that nums[i] == nums[j] and abs(i - j) <= k.

def find_dups(nums, k):
    count = {}
    i = 0
    
    for num in nums:
        if num in count:

            if abs(i - count[num]) <= k:
                return True
            
            count[num] = 1
            i += 1
    
    return False