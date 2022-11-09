from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator()

    def test_multiply_success(self):
        assert self.calc.multiply(2,6) == 12

    def test_division_success(self):
        assert self.calc.division(12,3) == 4

    def test_substraction_success(self):
        assert self.calc.subtraction(4,2) == 2

    def test_adding_success(self):
        assert self.calc.adding(2,3) == 5

    def teardown(self):
        print("Выполнение метода Teardown\n"
              "Завершение тестов.")