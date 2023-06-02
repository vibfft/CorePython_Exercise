def move_zeroes(nums: list) -> None:
    
    if len(nums) == 1:
        print(nums)
        return
    
    size = len(nums)
    p1 = 0
    for i in range(size):
        if nums[p1] == 0:
            print(f"val: {nums[p1]}")
            nums.append(nums.pop(p1))
            print(f"arry: {nums}")
        else:
            p1 += i
    print(nums)
            
def main() -> None:
    arry_a = [0,1,0,3,12]
    arry_b = [0]
    arry_c = [0,0,1]
    arry_d = [4,2,4,0,0,3,0,5,1,0]
    
    for arry in [arry_a, arry_b, arry_c, arry_d]:
        move_zeroes(arry)
    
if __name__ == '__main__':
    main()
    
            
    
    