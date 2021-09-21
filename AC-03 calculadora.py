# -*- coding: utf-8 -*-
#Importação de modulos
import abc
from logging import raiseExceptions
from unittest import TestCase,main


#Criação de classes
class Calculadora(object):
    def calcular(self,argumento1,argumento2,operador):
        operacao = OperacaoFabrica().criar(operador)
        if(operacao == None):
            return 0
        else:
            resultado = operacao.executar(argumento1,argumento2)
            return resultado

class OperacaoFabrica(object):
    def criar(self, operador):
        if (operador == 'soma'):
            return Soma()
        elif (operador == 'subtracao'):
            return Subtracao()
        elif (operador == 'divisao'):
            return Divisao()
        elif (operador == 'multiplicacao'):
            return Multiplicacao()
        elif (operador == 'potenciacao'):
            return Potenciacao()
        elif (operador == 'resto'):
            return Resto()

class Operacao(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def executar(self,argumento1,argumento2):
        pass

#Classes de Operação
class Soma(Operacao):
    def executar(self, argumento1, argumento2):
        resultado = argumento1 + argumento2
        return resultado
class Subtracao(Operacao):
    def executar(self, argumento1, argumento2):
        resultado = argumento1 - argumento2
        return resultado
class Divisao(Operacao):
    def executar(self, argumento1, argumento2):
        resultado = argumento1 / argumento2
        return resultado
class Multiplicacao(Operacao):
    def executar(self, argumento1, argumento2):
        resultado = argumento1 * argumento2
        return resultado    
class Resto(Operacao):
    def executar(self,argumento1,argumento2):
        resultado = argumento1%argumento2
        return resultado
class Potenciacao(Operacao):
    def executar(self, argumento1, argumento2):
        resultado = argumento1 ** argumento2
        return resultado


#Testes
class Testes(TestCase):
    def test_soma(self):
        calculo_soma = Calculadora()
        result = calculo_soma.calcular(2,3,'soma')
        self.assertEqual(result,5)
        
    def test_multiplicacao(self):
        calculo_multiplicacao = Calculadora()
        result = calculo_multiplicacao.calcular(2,5,'multiplicacao')
        self.assertEqual(result,10)

    def test_divisao(self):
        calculo_divisao = Calculadora()
        result = calculo_divisao.calcular(2,4,'divisao')
        self.assertEqual(result,0.5)

    def test_subtracao(self):
        calculo_subtracao = Calculadora()
        result = calculo_subtracao.calcular(10,50,'subtracao')
        self.assertEqual(result, -40)

    def test_potenciacao(self):
        calculo_potencia = Calculadora()
        result = calculo_potencia.calcular(4,4,'potenciacao')
        self.assertEqual(result,256)
    def test_resto(self):
        calculo_resto= Calculadora()
        result= calculo_resto.calcular(99,2,'resto')
        self.assertEqual(result,1)


banner = """"CALCULADORA
Operações:\n
    Soma            +
    Subtracao       -
    Multiplicacao   x
    Divisao         /
    Potenciacao     n²
    Resto           %\n"""


def codigo():
    operacoes=['soma','subtracao','multiplicacao','divisao','potenciacao','resto']
    operacao=input("Digite o nome da operação, sem acento:\n").lower()
    if operacao not in operacoes:
        print("Operação não reconhecida")
        codigo()
    argumento1=float(input("Digite o valor 1:\n"))
    argumento2=float(input("Digite o valor 2:\n"))
    resultado = Calculadora().calcular(argumento1,argumento2,operacao)
    print ("Resultado = {0:g}".format(float(resultado)))


print(banner)
codigo()
main()