class TV:
    _numTV = 0
    def __init__(self, marca, estado) :
        self._marca = marca
        self._canal = 1
        self._precio = 500
        self._estado = estado
        self._volumen = 1
        self._control = None
        TV._numTV +=1
# Get para para los atributos marca, canal, precio, volumen, estado y control.

    def getMarca(self):
        return self._marca
    def getCanal(self):
        return self._canal
    def getPrecio(self):
        return self._precio
    def getVolumen(self):
        return self._volumen
    def getEstado(self):
        return self._estado
    def getControl(self):
        return self._control
    
# Set para para los atributos marca, canal, precio, volumen y control.
    
    def setMarca(self, marca):
        self._marca = marca

    def setCanal(self, canal):
        if self._estado == True:
            if canal <= 120 and canal >= 1:
                self._canal = canal
        
    def setPrecio(self, precio):
        self._precio = precio

    def setVolumen(self, volumen):
        if self._estado == True:
            if volumen <= 7 and volumen >= 0:
                self._volumen = volumen

    def setControl(self, control):
        self._control = control  

# Metodos TurnOn, TurnOff, VolumenUp, VolumenDown, CanalUp y CanalDown

    def turnOn(self):
        if self._estado == False:
            self._estado = True

    def turnOff(self):
        if self._estado == True:
            self._estado = False

    def canalUp(self):
        if self._estado == True and (self._canal < 120):
            self._canal += 1

    def canalDown(self):
        if self._estado == True and (self._canal > 1):
            self._canal -= 1

    def volumenUp(self):
        if self._estado == True and (self._volumen < 7):
            self._volumen += 1

    def volumenDown(self):
        if self._estado == True and (self._volumen > 0):
            self._volumen -= 1

#Metodos de clase Get y Set para numTV
    @classmethod
    def getNumTV (cls):
        return cls._numTV
    
    @classmethod
    def setNumTV (cls, numTV):
        cls._numTV = numTV
    
            




      

    

        