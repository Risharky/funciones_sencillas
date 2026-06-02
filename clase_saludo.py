"""
creacion de clases
"""
class Saludo:
    #definicion del metodo constructor
    def __init__(self, nombre):
        self.__nombre =nombre

    #definicion de retono de cadena 
    def retornar_saludo(self):
        return self.__nombre
    
    
    
""" 
creacion de objetos
"""    

unSaludo = Saludo('Ricardo')
print('hola',unSaludo.retornar_saludo(),' esto es un simple saludo')