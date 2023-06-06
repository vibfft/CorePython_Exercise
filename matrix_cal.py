#!/usr/bin/env python3

def abs_difference_matrix(matrix):

    first_sum = 0
    second_sum = 0
    if not len(matrix):
        return 0
    elif len(matrix) == 1:
        return 0
    else:
        for i in range(len(matrix)):
            first_sum += matrix[i][i]
            second_sum += matrix[i][len(matrix) - 1 - i]

    return abs(first_sum - second_sum)

def main() -> None:
    # 1 + 5 + 9 = 15
    # 3 + 5 + 7 = 15
    # 1 - 5 - 9 = 13
    # 3 - 5 + 7 = 5
    print(abs_difference_matrix([[1,2,3],
                                 [4,-5,6],
                                 [7,8,-9]]))

if __name__ == '__main__':
    main()
