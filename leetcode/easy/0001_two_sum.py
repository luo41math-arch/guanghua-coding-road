def two_sum_brute(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return [i,j]

def two_sum_hash(nums,target):
    #哈希表：数字 -> 下标，复杂度o(1)
    hashmap={}
    for i,num in enumerate(nums):

        #找当前数字的共轭
        need=target-num

        #如果需要的数字已经出现
        if need in hashmap:
            return [hashmap[need],i]

        #哈希精髓，边查边存
        hashmap[num]=i

nums=[2,7,11,15]
target=9

print(two_sum_hash(nums,target))