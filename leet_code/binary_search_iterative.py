# time complexity is O(logN)
# space complexity is O(1)

def binary_search(number_array: list, target: int) -> int:
    b_index = 0
    e_index = len(number_array) - 1

    while b_index <= e_index:

        m_index = (e_index + b_index) // 2 # beginning and ending index need to be added since 
                                           # mid point needs to be greater when target is higher than mid point
                                           # and lower when the mid point is less than target
        print(f"index: {m_index}, b: {b_index}, e: {e_index}, array: {number_array}")
        if target == number_array[m_index]:
            return m_index
        elif target < number_array[m_index]:
            e_index = m_index - 1
        elif target > number_array[m_index]:
            b_index = m_index + 1

def main() -> None:

    number_array = [2,5,9,11,19,25]

    for i in [5,11,19,25]:
        print(f"number to find: {i}, position of the number: {binary_search(number_array, i)}")

if __name__ == '__main__':
    main()