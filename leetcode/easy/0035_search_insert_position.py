def searchInsert(nums: List[int], target: int) -> int: 
    left = 0
    right = len(nums)-1
    mid = (left + right)//2
    while nums[mid] != target and left <= right:
        if nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
        mid = (left + right)//2
    if left > right:
        return left
    return mid