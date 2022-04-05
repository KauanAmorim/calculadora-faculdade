class Calculadora:

    def __init__(self, number1, number2) -> None:
        self.__number1 = number1
        self.__number2 = number2

    @property
    def number1(self):
        return self.__number1
    
    @property
    def number2(self):
        return self.__number2
    
    def calcular(self, operation):
        if operation == "somar":
            return self.somar()
        if operation == "subtrair":
            return self.subtrair()
        if operation == "multiplicar":
            return self.multiplicar()
        if operation == "dividir":
            return self.dividir()
        if operation == "resto":
            return self.resto()

    def somar(self):
        result = self.__number1 + self.__number2
        return result
    
    def subtrair(self):
        result = self.__number1 - self.__number2
        return result

    def multiplicar(self):
        result = self.__number1 * self.__number2
        return result

    def dividir(self):
        result = self.__number1 / self.__number2
        return result

    def resto(self):
        result = self.__number1 % self.__number2
        return result
