def longestConsecutive(nums):
    if not nums:
        return 0

    nums = sorted(set(nums))
    
    max_len = 1
    curr_len = 1

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1] + 1:
            curr_len += 1
        else:
            max_len = max(max_len, curr_len)
            curr_len = 1

    return max(max_len, curr_len)


l = [1,1,2,3,4,5,2,4,53,6,6,3,24,3,4,7,8,1]
n = longestConsecutive(l)
print(n)