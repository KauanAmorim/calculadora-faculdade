from jsonschema import ValidationError
import math

class Calculadora:

    def setNumber1(self, number) -> None:
        self.__number1 = number
    
    def setNumber2(self, number) -> None:
        self.__number2 = number

    def setOperation(self, operation) -> None:
        self.__operation = operation

    @property
    def number1(self):
        return self.__number1
    
    @property
    def number2(self):
        return self.__number2
    
    @property
    def operation(self):
        return self.__operation

    def calcular(self):
        self.__validParameters(self.__operation)

        if self.__operation == "sqrt":
            return self.squareRoot()
        if self.__operation == "pow":
            return self.exponential()
        if self.__operation == "log":
            return self.logarithm()
        
        raise Exception("This operation does not exist")

    def squareRoot(self):
        self.__validParameters(self.__number1)
        result = math.sqrt(self.__number1)
        return result
    
    def exponential(self):
        self.__validParameters(self.__number1, self.__number2)
        result = math.pow(self.__number1, self.__number2)
        return result

    def logarithm(self):
        self.__validParameters(self.__number1)
        result = math.log(self.__number1)
        return result
    
    def __validParameters(self, parameter1, parameter2 = False) -> None:
        if parameter1 and parameter2:
            if not (parameter1 and parameter2):
                raise ValidationError("Missing parameter to continue the operation")
        else:
            if not parameter1:
                raise ValidationError("Missing parameter to continue the operation")