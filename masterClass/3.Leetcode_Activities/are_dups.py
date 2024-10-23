
# Frequency Counter Approach

# Frequency Counter / Multiple Pointers - areThereDuplicates

# Implement a function called, areThereDuplicates which accepts a variable number of arguments,
# and checks whether there are any duplicates among the arguments passed in.
# You can solve this using the frequency counter pattern OR the multiple pointers pattern.

# Examples:

# areThereDuplicates(1, 2, 3) // false
# areThereDuplicates(1, 2, 2) // true
# areThereDuplicates('a', 'b', 'c', 'a') // true
# Restrictions:

# Time - O(n)
# Space - O(n)

# ----------------------------------------------------------------
# Frequency Counter Approach:


from collections import Counter

def containsDuplicate(nums):
    dict = Counter(nums)
    for key,value in enumerate(dict):
        if dict[key] > 1:
            return True
        else:
            return False


print(containsDuplicate([1,2,3,4,5]))




def containsDuplicate (nums) -> bool:
        return len(set(nums)) < len(nums)
# Example usage
print(containsDuplicate(1, 2, 3))  # Should print False
print(containsDuplicate(1, 2, 2))  # Should print True
print(containsDuplicate('a', 'b', 'c', 'a'))  # Should print True



# ----------------------------------------------------------------
# Multiple Pointer Approach:
def containsDuplicate(nums):
    nums.sort()
    left = 0
    right = 1
    while right < len(nums):
        if nums[left] == nums[right]:
            return True
        left += 1
        right += 1
    return False

print(containsDuplicate([1,2,3,4,5]))// False
print(containsDuplicate([1,2,2,4,5]))// True
print(containsDuplicate([1,2,3,4,5,5]))// True