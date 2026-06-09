from abc import ABC, abstractmethod

class Dispositivo(ABC):
    def __init__(self, id_modelo):
        self.id_modelo = id_modelo
        self.energia = 100.0

    @abstractmethod
    def reducir_energia(self):
        pass


class LuzInteligente(Dispositivo):
    def reducir_energia(self):
        self.energia -= 2.5
        if self.energia < 0:
            self.energia = 0


class AireAcondicionado(Dispositivo):
    def __init__(self, id_modelo):
        super().__init__(id_modelo)
        self.temperatura = 20.0  # valor inicial realista

    def reducir_energia(self):
        if self.temperatura <= 20:
            factor = 0.98
        elif self.temperatura <= 30:
            factor = 0.95
        elif self.temperatura <= 40:
            factor = 0.90
        else:
            factor = 0.85

        self.energia *= factor


class Tarjeta:
    def __init__(self, direccion_mac: str, frecuencia_ghz: float):
        self.direccion_mac = direccion_mac
        self.frecuencia_ghz = frecuencia_ghz


class CentralHub:
    def __init__(self, id_central: str, nombre_habitacion: str, direccion_mac: str, frecuencia_ghz: float):
        self.id_central = id_central
        self.nombre_habitacion = nombre_habitacion
        self.tarjeta = Tarjeta(direccion_mac, frecuencia_ghz)
        self._dispositivos: list[Dispositivo] = []
        self.estado = "NORMAL"

    def vincular_dispositivo(self, dispositivo: Dispositivo):
        if len(self._dispositivos) >= 4:
            raise ValueError("Capacidad de la central agotada")
        self._dispositivos.append(dispositivo)

    def desvincular_dispositivo(self, dispositivo: Dispositivo):
        if dispositivo in self._dispositivos:
            self._dispositivos.remove(dispositivo)

    @property
    def dispositivos(self):
        return tuple(self._dispositivos)

    def ejecutar_ciclo(self):

        if self.estado == "MODO_AHORRO_CRITICO":
            raise RuntimeError("Central bloqueada por seguridad energética")

        # 1. actualizar energía
        for d in self._dispositivos:
            d.reducir_energia()

        # 2. evaluar condiciones
        if self._evaluar_condiciones_criticas():
            self.estado = "MODO_AHORRO_CRITICO"

    def _evaluar_condiciones_criticas(self):

        if len(self._dispositivos) == 0:
            return False

        total_energia = 0.0
        aire_mayor_40 = False

        for d in self._dispositivos:
            total_energia += d.energia

            if isinstance(d, AireAcondicionado):
                if d.temperatura > 40:
                    aire_mayor_40 = True

        promedio = total_energia / len(self._dispositivos)

        condicion_energia_baja = promedio < 15.0
        condicion_riesgo_calor = (
            self.tarjeta.frecuencia_ghz > 5.0 and aire_mayor_40
        )

        return condicion_energia_baja or condicion_riesgo_calor