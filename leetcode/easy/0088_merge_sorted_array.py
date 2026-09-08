def merge(nums1,m,nums2,n):
    write = m+n-1
    left = m-1
    right = n-1
    while right >= 0:
        if left >= 0 and nums1[left] > nums2[right]:
            nums1[write] = nums1[left]
            left -= 1
        else:
            nums1[write] = nums2[right]
            right -= 1
        write -= 1
    return nums1

nums1 = [0]
m = 0
nums2 = [1]
n = 1

print(merge(nums1,m,nums2,n))