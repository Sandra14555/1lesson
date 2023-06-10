class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def addition(self):
        return self.num1 + self.num2

    def subtraction(self):
        return self.num1 - self.num2

    def multiplication(self):
        return self.num1 * self.num2

    def division(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "Error: Division by zero is not allowed."



num1 = int(input("Input first number: "))
num2 = int(input("Input second number: "))


calculator = Calculator(num1, num2)


result_addition = calculator.addition()
result_subtraction = calculator.subtraction()
result_multiplication = calculator.multiplication()
result_division = calculator.division()


print("Addition:", result_addition)
print("Subtraction:", result_subtraction)
print("Multiplication:", result_multiplication)
print("Division:", result_division)

