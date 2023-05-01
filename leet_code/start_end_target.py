nums = [1,3,3,5,5,5,8,9]
target = 9
def binary_search(nums, left, right, target):
    while left <= right:
        mid = (left + right) // 2
        
        found_val = nums[mid]
        
        if found_val == target:
            return mid
        elif found_val < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1

def search_range(nums, target):
    if len(nums) < 1:      # empty array
        return [-1, -1]
    
    first_pos = binary_search(nums, 0, len(nums) - 1, target)  # first find the starting index of the target
    
    if first_pos == -1:    # target is not found
        return [-1, -1]
    
    print(f"first pos: {first_pos}")
    end_pos = first_pos
    start_pos = first_pos
    temp1 = -1
    temp2 = -1
    
    while start_pos != -1:     # is the target found in the left half
        temp1 = start_pos
        start_pos = binary_search(nums, 0, start_pos - 1, target)
        print(f"start_pos: {temp1}")
    start_pos = temp1
    
    while end_pos != -1:       # is the target found in the right half
        temp2 = end_pos
        end_pos = binary_search(nums, end_pos + 1, len(nums) - 1, target)
        print(f"end_pos: {temp2}")
    end_pos = temp2
    
    return [start_pos, end_pos]

print(search_range(nums, target))