nums = [11,15,2,7] 
target = 9

# this is a brute force solution
def two_sum(nums: list, target: int) -> list:
    for i in range(0, len(nums) - 1):     # max index value for p1 is len(nums) - 2, hence range is len(nums) - 1
        for j in range(i + 1, len(nums)): # max index value for p2 is len(nums) - 1, hence range is len(nums)
            if (nums[i] + nums[j] == target):
                return [i, j]
    return [-1, -1]

print(two_sum(nums, target))
    
    
    