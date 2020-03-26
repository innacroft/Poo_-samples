class Coche():
    def desplazamiento(self):
        print('Me desplazo utilizando 4 ruedas')

class Moto():
    def desplazamiento(self):
        print('Me desplazo utilizando 2 ruedas')

class Camion():
     def desplazamiento(self):
        print('Me desplazo utilizando 6 ruedas')
#si se desea acceder a cualquiera de los objetos desplazamientos pero sin crear objetos y objetos, puede crearse un metodo que lo haga por uno así:
def desplazamientoVehiculo(Vehiculo):
    Vehiculo.desplazamiento()

#se llama el metodo anterior con el nombre de la clase que se quiere, ej camion: 
miVehiculo=Camion()
desplazamientoVehiculo(miVehiculo)