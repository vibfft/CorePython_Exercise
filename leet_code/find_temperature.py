def closest_zero(ts: list) -> float:

    if not len(ts):
        return 0

    if len(ts) == 1:
        return ts[0]
    
    pos_smallest = []
    neg_smallest = []

    for val in ts:
        if float(val) < 0.0:
            print(f"Sneg: {neg_smallest}, V: {val}")
            neg_smallest.append(val)
        elif float(val) > 0.0:
            print(f"Spos: {pos_smallest}, V: {val}")
            pos_smallest.append(val)
    
    neg_max = max(neg_smallest)
    pos_min = min(pos_smallest)
    
    print(f"neg: {neg_smallest}, {neg_max}, pos: {pos_smallest}, {pos_min}")
    if float(abs(neg_max)) >= float(abs(pos_min)):
        return pos_min
    return neg_max

def main() -> None:

    array_one = [7,-10,13,8,4,-7.2,-12,1.7,-3.7,3.5,-9.6,6.5,-1.7,-6.2,7]
    array_empty = []
    array_big = [5526]
    array_small = [-273]
    array_big_small = [5526, -273]
    for input_array in [array_one, array_empty, array_big, array_small, array_big_small]:
        print(f"Final: {closest_zero(input_array)}")

if __name__ == '__main__':
    main()