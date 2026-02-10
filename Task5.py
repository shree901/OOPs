class Calculator:
    def __call__(self, a, b):
        return a + b


calc = Calculator()
print(calc(10, 20))
