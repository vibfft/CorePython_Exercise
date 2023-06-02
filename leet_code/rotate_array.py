def rotate(nums: list, k: int) -> None:
    
    for j in range(k):
        tmp_list = []
        tmp_list.append(nums[-1])
        for i in range(len(nums) - 1):
            tmp_list.append(nums[i])
        # print(tmp_list)
        nums = tmp_list
    print(nums)

def main() -> None:
    array_one = [1,2,3,4,5,6,7] # k=3
    rotate(array_one, 3)
    
    array_two = [-1,-100,3,99]  # k=2
    rotate(array_two, 2)
    
if __name__ == "__main__":
    main()