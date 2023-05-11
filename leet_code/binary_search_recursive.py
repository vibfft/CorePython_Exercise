def binary_search(num_array: list, left: int, right: int, target: int) -> int:

    if not len(num_array):
        return num_array

    elif len(num_array) == 1:
        return 0

    else:
        mid = (left + right) // 2
        if num_array[mid] < target:
            binary_search(num_array, mid + 1, right, target)
        elif num_array[mid] > target:
            binary_search(num_array, left, mid - 1, target)
        else:
            return mid

def main() -> None:
    num_array = [1,3,7,10,11,19,25]
    for i in [7, 10, 19]:
        print(f"{i}")
        print(f"target: {i}, index: {binary_search(num_array, 0, len(num_array) - 1, i)}")
if __name__ == '__main__':
    main()