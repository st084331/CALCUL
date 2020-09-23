from symbol import power
import random

class Calculator:
    def __init__(self, init_value=0):
        self.value = init_value

    def add(self, *args):
        self.value += sum(args)
        return self

    def multiply(self, *args):
        for x in args:
            self.value *= x
        return self

    def divide(self, *args, integer_divide=False):
        for x in args:
            if(x==0):
                print('Incorrect argument')
                exit(0)
            else:
                if integer_divide:
                    self.value //= x
                else:
                    self.value /= x
            return self

    def subtract(self, *args):
        self.value -= sum(args)
        return self

    def power(self, *args):
        const = self.value
        for i in args:
            for x in range(i-1):
                self.value *= const
        return self

    def root(self):
        value1 = self.value
        while True:
            value2 = (self.value * self.value + value1)//(2 * self.value)
            if value2 >= self.value:
                return self
            self.value = value2


    def __repr__(self):
        return self.value

    def __str__(self):
        return str(self.value)

def fun(x):
    return x[::-1]


if __name__ == '__main__':
    calculator = Calculator(random.randint(0,100))
    print(calculator)
    print(calculator)
    print(calculator.power(2,3).add(1, 2, 3, 5.1).multiply(4, 0.123).subtract(4, 1, -100).divide(5, integer_divide=True).root())

