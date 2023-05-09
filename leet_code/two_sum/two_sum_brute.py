class NumberCalc(object):
    #  0, 1, 2, 3, 4 <= indices
    # [1, 3, 7, 9, 2]
    #  pointer 1 at index 0 and goes up to index 3
    #  pointer 2 at index 1 and goes up to index 4
    def two_sum(nums: list, target: int) -> list:

        for i in range(len(nums) - 1):  # pointer 1 cannot go past len(nums) - 2
            number_to_find = target - nums[i]
            for j in range(i + 1, len(nums)): # pointer 2 is up to len(nums) - 1
                if number_to_find == nums[j]:
                    return [i, j]
                
        return None
    
    # nums = [1, 3, 7, 9, 2], target = 11
    def two_sum_v2(nums: list, target: int) -> list:
        ntf_dict = {}
        for i in range(len(nums) - 1):
            ntf = target - nums[i] # 10, 8, 4, 2, 9
            if ntf not in ntf_dict:
                ntf_dict[nums[i]] = i # keep on adding previous numbers
            else: # "number_to_find" is in ntf_dict
                return [i, ntf_dict[ntf]]  # when "number_to_find" is found in ntf_dict           
        return None
    
def main() -> None:

    nums = [1, 3, 7, 9, 2]

    n = NumberCalc
    print(n.two_sum(nums, target=11))
    print(n.two_sum_v2(nums, target=11))

if __name__ == '__main__':
    main()