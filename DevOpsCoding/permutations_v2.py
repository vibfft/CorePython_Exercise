# find all permutations of a text field
# new_result = result + val[i]
# new_val = val[0:i] + val[i+1:]
# permute(new_val, new_result)

def permute(val, result=''):
    if len(val) == 0:
        print(result)
        print('*'*15)

    for i in range(len(val)):
        
        new_val = val[0:i] + val[i+1:]
        #print(f"v: {new_val} = {val[0:i]} + {val[i+1:]}\n")
        new_result = result + val[i]
        #print(f"r: {new_result} = {result} + {val[i]}")
        
        permute(new_val, new_result)


def main():
    test_str = "ABC"
    permute(test_str)


if __name__ == "__main__":
    main()
