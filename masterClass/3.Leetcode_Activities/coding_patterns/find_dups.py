#2. Find Duplicates
# Examples:

# areThereDuplicates(1, 2, 3) // false
# areThereDuplicates(1, 2, 2) // true

def find_dups(nums):
    lookup = {}
    
    for num in nums:
        if num in lookup:
            return True
        else:
            lookup[num] = 1
        
    return False


#2 pointer approach:

def find_dups_sorted(nums):
    nums.sort()
    left = 0
    right = 1
    
    for num in nums:
        if nums[left] == nums[right]:
            return True
        else:
            left += 1
            right += 1
        
    return False
        
        
#3 using a set
def find_dups_s(nums):
    seen = set()
    duplicates = set()
    
    for num in nums:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
            
    return list(duplicates)

#3.5 sets clean
def find_dups1(nums):
    removed = set(nums)
    if len(removed) < len(nums):
        return True
    else:
        return False