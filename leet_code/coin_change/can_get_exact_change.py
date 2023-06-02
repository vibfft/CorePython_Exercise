#!/usr/bin/env python


def canGetExactChange(targetMoney, denominations):

    if targetMoney in denominations:
        return True
    else:
        coin_list = sorted(denominations, reverse=True)
        for c in coin_list:
            if targetMoney == c:
                return True
            else:
                if c < targetMoney:
                    print(f"coin: {c}, target_money: {targetMoney}")
                    coin_list.remove(c)
                    return canGetExactChange(targetMoney - c, denominations)
        else:
            return False


print(canGetExactChange(94, [5, 10, 25, 100, 200]))
print(canGetExactChange(75, [4, 17, 29]))
print(canGetExactChange(100, [5, 10, 25]))
