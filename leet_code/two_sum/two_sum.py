# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.
#
# Example 1:
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:
#
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:
#
# Input: nums = [3,3], target = 6
# Output: [0,1]

# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         nums_dict = {}
#         for i in range(len(nums)):

#             complement = target - nums[i]
#             if complement in nums_dict:
#                 return nums_dict[complement], i
#             nums_dict[nums[i]] = i

#         return "No two sum solution"

class TwoSum:
    # nums = [1, 3, 7, 9, 2], target = 9
    #  0, 1, 2, 3, 4 <= indices
    # [1, 3, 7, 9, 2]
    #  pointer 1 at index 0 and goes up to index 3
    #  pointer 2 at index 1 and goes up to index 4
    def two_sum(self, nums: list, target: int) -> list:
        
        comp_dict = dict()
        for i, item in enumerate(nums):
            
            tmp_comp = target - item
            if item not in comp_dict:   # 1, 3, 7, 9, 2, note item 2 is in comp_dict
                comp_dict[tmp_comp] = i # DICT: {8: 0, 6: 1, 2: 2, 0: 3}
            else:
                print(f"DICT: {comp_dict}")
                return [comp_dict[item], i] 
        return [-1,-1]
def main():
    s = TwoSum()
    print(s.two_sum([],1))
    print(s.two_sum([5],5))
    print(s.two_sum([1,3,7,9,2],25))
    print(s.two_sum([1,3,7,9,2],9))
    print(s.two_sum([3,2,4],6))
    
if __name__ == '__main__':
    main()
                
        