import sys

class Calculator():

    valid_ops = ["+", "-", "*", "/"]

    def __init__(self, first, op: str, second) -> None:
        self.first = {"value": first}
        self.op = op
        self.second = {"value": second}
        self.result = None

    def validate_values(self):

        try:
            int(self.first["value"])
            int(self.second["value"])
            # print(f'int: {self.first["value"]}')
            # print(f'int: {self.second["value"]}')
            self.first['value'] = int(self.first['value'])
            self.second['value'] = int(self.second['value'])
            return True
        except ValueError:
            try:
                float(self.first["value"])
                float(self.second["value"])
                # print(f'int: {self.first["value"]}')
                # print(f'int: {self.second["value"]}')
                self.first['value'] = float(self.first['value'])
                self.second['value'] = float(self.second['value'])
                return True
            except ValueError:
                return False

    def validate_operator(self):

        if self.op not in Calculator.valid_ops:
            return False
        return True

    def check_divide_by_zero(self):
        if not self.second['value']:
            return True
        return False

    def calculate(self):

        if self.op == "+":
            self.result = float(self.first['value'] + self.second['value'])
        elif self.op == "-":
            self.result = float(self.first['value'] - self.second['value'])
        elif self.op == "*":
            self.result = float(self.first['value'] * self.second['value'])
        elif self.op == "/":
            self.result = float(self.first['value'] / self.second['value'])

        return self.result


def main() -> None:

    c = Calculator(1,'+',2)
    while True:
        data = input("Enter an equation")
        first, op, second = data.split()
        c = Calculator(first, op, second)
        # print(c.first, ",", c.op, ",", c.second)
        if not c.validate_values():
            print("Do you even know what numbers are? Stay focused!")
            continue
        elif not c.validate_operator():
            print(
                "Yes ... an interesting math operation. You've slept through all classes, haven't you?")
            continue
        else:
            if c.op == "/" and c.check_divide_by_zero():
                print("Yeah... division by zero. Smart move...")
                continue
            result = c.calculate()
            print(result)


if __name__ == '__main__':
    main()
