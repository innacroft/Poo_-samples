class Coche():#se inicia con class y el nombre en mayuscula
    #Establecer las propiedades

    #crear constructor --> inicia la clase y da un estado incial de los objetos de la clase
    def __init__(self):
        self.__ruedas=4 #-->ENCAPSULACION esto es una variable privada, quiere decir que no es accesible fuera de esta clase
        self.largoChasis=250
        self.anchoChasis=120
        
        self.__enMarcha=False

    #establecer comportamientos --> metodos: funcion especial que  pertenece a clase
    def  arrancar(self): #self--> hace referencia al objeto que pertenece a la clase(instancia)
        self.__enMarcha=True #-->ENCAPSULACION esto es una variable privada, solo se puede modificar desde aca

    def estado(self):
        if(self.enMarcha):
            return ("En marcha" )
        else:
            return ("Detenido" )
            
    def chequeo

miCoche=Coche() #instancia de clase
print("el largo del coche es: {}" .format(miCoche.largoChasis))
#llamar metodo dentro de clase
miCoche.arrancar()

print("Estado del coche: {}" .format(miCoche.estado()))

