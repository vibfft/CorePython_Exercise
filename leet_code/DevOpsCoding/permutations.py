# find all permutations of a text field

def permute(input_str, start_index, end_index):
    if start_index == end_index:
        print(''.join(input_str))
    else:
        for i in range(start_index, end_index):
            input_str[start_index], input_str[i] = input_str[i], input_str[start_index]
            permute(input_str, start_index + 1, end_index)
            input_str[start_index], input_str[i] = input_str[i], input_str[start_index]


def main():
    test_str = "ABC"
    permute(list(test_str), 0, len(test_str))


if __name__ == "__main__":
    main()
