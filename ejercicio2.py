from abc import ABC, abstractmethod

class Dispositivo(ABC):
    def __init__(self, id_modelo):
        self.id_modelo = id_modelo
        self.energia = 100.0
        
    @abstractmethod
    def reducir_energia(self, factor):
        pass
    
class LuzInteligente(Dispositivo):
    def __init__(self, id_modelo):
        super().__init__(id_modelo)
    
    def reducir_energia(self, factor):
        self.energia -= 2.5
    
    
class AireAcondicionado(Dispositivo):
    def __init__(self, id_modelo):
        super().__init__(id_modelo)
        
    def reducir_energia(self, factor):
        self.energia *= factor
        
    
class CentralHub():
    def __init__(self, id_central: str, nombre_habitacion: str, direccion_mac: str, frecuencia_ghz: float):
        self.id_central = id_central
        self.nombre_habitacion = nombre_habitacion
        self.tarjeta = Tarjeta(direccion_mac, frecuencia_ghz)
        self._dispositivos: list[Dispositivo] = []    
        
    def vincular_dispositivo(self, dispositivo : Dispositivo):
        if len(self._dispositivos) <= 3:
            self._dispositivos.append(dispositivo)
        else:
            raise ValueError("Capacidad de la central agotada")
        
    def desvincular_dispositivo(self, dispostivo : Dispositivo):
        if dispostivo in self._dispositivos:
            self._dispositivos.remove(dispostivo)
   
    @property
    def dispositivos(self):
        return tuple(self._dispositivos)
    
    def ejecutar_ciclo(self, factor : float):
        for dispositivo in self._dispositivos:
            dispositivo.reducir_energia(factor)
        
    
    
class Tarjeta:
    def __init__(self, direccion_mac: str, frecuencia_ghz: float):
        self.direccion_mac = direccion_mac
        self.frecuencia_ghz = frecuencia_ghz