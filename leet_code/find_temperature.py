#
# import java.math.*;
#
# class Solution {
#     static double closestToZero(double[] ts) {
#         if (ts.length == 0) return 0;
#
#         double closest = ts[0];
#         for (double i: ts) {
#             double abs = Math.abs(i);
#             double absClosest = Math.abs(closest);
#             if (abs < absClosest) {
#                 closest = i; } else if (abs == absClosest & & closest < 0) {
#                 closest = i; }
#         }
#         return closest; }
# }


def closest_zero(ts: list) -> float:

    if not len(ts):
        return 0

    closest = ts[0]
    for val in ts:
        abs_val = float(abs(val))
        abs_near_zero = float(abs(closest))

        if abs_val < abs_near_zero:
            closest = val
        elif abs_val == abs_near_zero and closest < 0:
            closest = val

    return closest

def main() -> None:

    array_one = [7, -10, 13, 8, 4, -7.2, -12,
                 1.7, -3.7, 3.5, -9.6, 6.5, -1.7, -6.2, 0.2, 7]
    array_empty = []
    array_big = [5526]
    array_small = [-273]
    array_big_small = [5526, -273]
    for input_array in [array_one, array_empty, array_big, array_small, array_big_small]:
        print(f"Final: {closest_zero(input_array)}")


if __name__ == '__main__':
    main()
