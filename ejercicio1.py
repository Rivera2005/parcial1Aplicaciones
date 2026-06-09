"""
Una locomotora tiene una capacidad máxima de arrastre en toneladas. 
Jamás se puede enganchar un vagón si este hace que el peso total del tren supere la capacidad de la locomotora
"""

from abc import ABC, abstractmethod

class Locomotora:
    def __init__(self, id_locomotora: str, modelo: str, capacidad_arrastre: float):
        self.id_locomotora = id_locomotora
        self.modelo = modelo
        self.capacidad_arrastre = capacidad_arrastre #Peso máximo en toneladas que puede remolcar.

class Vagon(ABC):
    def __init__(self, id_vagon: str, peso_vacio: float):
        self.id_vagon = id_vagon
        self.peso_vacio = peso_vacio
        
    @abstractmethod
    def calcular_peso_total(self) -> float:
        pass
        
class VagonCargaSeca(Vagon):
    def __init__(self, id_vagon, peso_vacio, peso_carga_actual: float):
        super().__init__(id_vagon, peso_vacio)
        self.peso_carga_actual = peso_carga_actual
    
    def calcular_peso_total(self):
        return self.peso_vacio + self.peso_carga_actual

class VagonCisterna(Vagon):
    def __init__(self, id_vagon, peso_vacio, capacidad_litros: float, densidad_liquido: float):
        super().__init__(id_vagon, peso_vacio)
        self.capacidad_litros = capacidad_litros
        self.densidad_liquido = densidad_liquido
        
    def calcular_peso_total(self):
        return self.peso_vacio + (self.capacidad_litros * self.densidad_liquido)

class Tren:
    def __init__(self, id_tren: str, id_locomotora: str, modelo: str, capacidad_arrastre: float):
        self.id_tren = id_tren
        self.locomotora = Locomotora(id_locomotora, modelo, capacidad_arrastre)
        self._vagones = []
    
    def enganchar_vagon(self, vagon: Vagon):
        peso_tren = self.obtener_peso_tren()
        cantidad_vagonesCisterna = 0
        peso_vagonesCisterna = 0.00
        for vagoni in self._vagones:
            if isinstance(vagoni, VagonCisterna):
                cantidad_vagonesCisterna += 1
                peso_vagonesCisterna += vagoni.calcular_peso_total()
            
        if isinstance(vagon, VagonCisterna):
            cantidad_vagonesCisterna += 1
            peso_vagonesCisterna += vagon.calcular_peso_total()
                
        if peso_tren + vagon.calcular_peso_total() > self.locomotora.capacidad_arrastre:
            raise ValueError("Capacidad de arrastre excedida")
        elif cantidad_vagonesCisterna  > 3 :
            raise ValueError("Restricción de seguridad de Vagones Cisterna violada")
        elif peso_vagonesCisterna > (peso_tren + vagon.calcular_peso_total()) * 0.6:
            raise ValueError("Restricción de seguridad de Vagones Cisterna violada")
        else:
            self._vagones.append(vagon)
    
    def obtener_peso_tren(self) -> float:
        peso_tren = 0.00
        
        for vagon in self._vagones:
            peso_tren += vagon.calcular_peso_total()
        
        return peso_tren
        
                