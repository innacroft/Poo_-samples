class Vehiculos():
    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False
    
    def arrancar(self):
        self.enmarcha=True
    def aceletar(self):
        self.acelera=True
    def frenar(self):
        self.frena=True
    def estado(self):
        print("Marca : {},\nModelo: {},\nEnmarcha: {},\nAcelera: {},\nFrena: {}" .format(self.marca,self.modelo,self.enmarcha,self.acelera,self.frena))

class Furgoneta(Vehiculos):
    def carga(self,cargar):
        self.cargado=cargar
        if(self.cargado):
            return "la furgoneta está cargada"
        else:
            return "la furgoneta no está cargada"

    def estado(self): #este reemplaza al metodo del padre
        print("Marca : {},\nModelo: {},\nEnmarcha: {},\nAcelera: {},\nFrena: {},\nCargada: {}" .format(self.marca,self.modelo,self.enmarcha,self.acelera,self.frena, self.cargado))



class Moto(Vehiculos):
    hcaballito=""
    
    def caballito(self):
        self.hcaballito="voy haciendo caballito"

    def estado(self): #este reemplaza al metodo del padre
        print("Marca : {},\nModelo: {},\nEnmarcha: {},\nAcelera: {},\nFrena: {},\nHace caballito: {}" .format(self.marca,self.modelo,self.enmarcha,self.acelera,self.frena, self.hcaballito))


class VElectricos():
    def __init__(self):
        self.autonomia=100
    
    def cargarEnergia(self):
        self.cargando=True

class BElectrica(VElectricos,Vehiculos): #Esta hereda los metodos de las dos clases !! esto se llama herencia multuiple, y tiene preferencia el de mas de la izquierda
    pass

print("starting ....")
miMoto=Moto("honda","C")
miMoto.caballito()
miMoto.estado()

furgoneta1= Furgoneta("Renault", "Kangoo")
furgoneta1.carga(True)
furgoneta1.estado()

miBici=BElectrica("") 