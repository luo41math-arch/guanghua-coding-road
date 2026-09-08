def sortedSquares(nums):
    left = 0
    right = len(nums)-1
    nums_new = [0]*len(nums)
    write = len(nums)-1
    while write >= 0:
        if abs(nums[left]) > abs(nums[right]):
            nums_new[write] = nums[left]**2
            left += 1
        else:
            nums_new[write] = nums[right]**2
            right -= 1
        write -= 1
    return nums_new

nums = [-4, -1, 0, 3, 10]
print(sortedSquares(nums))