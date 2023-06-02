def contains_duplicates(nums: list) -> bool:
    
    dups_hash = {}
    for i in range(len(nums)):
        if nums[i] not in dups_hash:
            dups_hash[nums[i]] = 1
        else:
            return True
    return False
                
def main() -> None:
    
    list_a = [1,2,3,1]
    list_b = [1,2,3,4]
    list_c = [1,1,1,3,3,4,3,2,4,2]
    
    for lst in [list_a, list_b, list_c]:
        print(contains_duplicates(lst))
    
if __name__ == '__main__':
    main()