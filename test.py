import unittest
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
    def test_square_root(self):
        calculadora = Calculadora()
        calculadora.setOperation('sqrt')
        calculadora.setNumber1(4)
        result = calculadora.calcular()
        expected = 2.0
        self.assertEqual(result, expected)
    
    def test_exponential(self):
        calculadora = Calculadora()
        calculadora.setOperation('pow')
        calculadora.setNumber1(4)
        calculadora.setNumber2(2)
        result = calculadora.calcular()
        expected = 16.0
        self.assertEqual(result, expected)
    
    def test_logarithm(self):
        calculadora = Calculadora()
        calculadora.setOperation('log')
        calculadora.setNumber1(4)
        result = calculadora.calcular()
        expected = 1.3862943611198906
        self.assertEqual(result, expected)