class Moto:
    def __init__(self,marca, color, modelo, cilindraje):
        self.marca = marca
        self.color = color
        self.modelo = modelo
        self.cilindraje = cilindraje

marca = input("Digite la marca de la moto: ")
color = input("Digite el color de la moto: ")
modelo = input("Digite el modelo de la moto: ")
cilindraje = int(input("Digite el cilindraje de la moto: "))

moto = Moto(marca,color, modelo, cilindraje)
print(f'la moto es de la marca {moto.marca}, color {moto.color}, modelo {moto.modelo} y con el cilindraje {moto.cilindraje}')