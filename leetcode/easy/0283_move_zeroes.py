def movezeros(nums):
    read = 0
    write = 0
    while read < len(nums):
        while read < len(nums) and nums [read] == 0:
            read += 1
        if read == len(nums):
            break
        nums[write] = nums[read]
        write += 1
        read += 1
    while write < len(nums):
        nums[write] = 0
        write += 1
    return nums

nums = [0, 1, 0, 3, 12]
print(movezeros(nums))