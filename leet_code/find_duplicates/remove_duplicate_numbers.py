
def remove_dups(nums: list) -> int:
    
    p1 = 0
    p2 = 1
    for i in range(len(nums)-1):
       if nums[p1] == nums[p2]:
           nums.pop(p2)
       else:
           p1 += 1
           p2 += 1
    return nums


def main() -> None:
    orig = [-1,0,0,0,1,1,1,2,2,2]
    print(orig)
    print(remove_dups(orig))
    
if __name__ == '__main__':
    main()