import pytest
from app.calculator import Calculator

class testCalc:
    def setup(self):
        self.Calc = Calculator

    def test_mutiply_Calculate_correcly(self):
        assert self.Calc.multiply(self, 10, 10) == 100

    def test_division_correctly(self):
        assert self.calc.division(self, 60, 3) == 20

    def test_subtraction_correctly(self):
        assert self.calc.subtraction(self, 200, 100) == 100

    def test_adding_correctly(self):
        assert self.calc.adding(self, 1, 1) == 2