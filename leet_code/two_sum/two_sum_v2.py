class TwoSum:
    def two_sum(self, nums: list, target: int) -> list:
        
       p1 = 0
       p2 = 1
       pair = []
       while True:
           
           num_to_find = target - nums[p1]
           print(f"ptr1: {p1}, ptr2: {p2}, nums: {nums}")
           if num_to_find == nums[p2]:
               pair.append(p1)
               pair.append(p2)
               break
               
           elif p2 < len(nums) - 1:
               p2 += 1
               
           elif p1 < len(nums) - 2:
               p1 += 1
               nums = nums[p1:]
               p2 = p1 + 1
               
           else:
               break
       return pair    
        
                
def main():
    s = TwoSum()
    print(s.two_sum([7,11,2,15],9))
    print(s.two_sum([3,2,4],6))
    
if __name__ == '__main__':
    main()
                
        