#modela los atributos de una moto 
class Moto:
    def __init__(self):
        self.marca = 'Royal Endfield'
        self.color = 'Azul'
        self.modelo = 'meteor'
        self.cilindraje = 360

#objeto instancia de una clase

moto = Moto()
print(moto.marca)
print(moto.color)
print(moto.modelo)
print(moto.cilindraje)        