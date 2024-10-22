def minimumAverage(nums):
    avg_arr = []
    if len(nums) == 2:
        return (nums[0] + nums[1]) / 2

    sorted_arr = sorted(nums)
    left = 0
    right = len(sorted_arr) - 1
    while left < right:
        smallest = sorted_arr[left]
        biggest = sorted_arr[right]
        avg = (smallest + biggest) / 2
        avg_arr.append(avg)

        left += 1
        right -= 1

    print(avg_arr)
    return min(avg_arr)

nums = [1,9,8,3,10,5]
print(minimumAverage(nums))

def minimumAverageRecursive(nums):
    if len(nums) == 2:
        return (nums[0] + nums[1]) / 2

    sorted_arr = sorted(nums)
    avg = (sorted_arr[0] + sorted_arr[-1]) / 2

    print(sorted_arr)
    print(avg)
    removed_first_last = sorted_arr[1: -1]
    print(removed_first_last)
    if removed_first_last:
        return min(avg, minimumAverageRecursive(removed_first_last))

    return avg

nums = [1,9,8,3,10,5]
print(minimumAverageRecursive(nums))
