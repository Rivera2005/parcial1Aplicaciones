from ejercicio2 import CentralHub, LuzInteligente, AireAcondicionado

central = CentralHub(
    id_central="HUB-77",
    nombre_habitacion="Sala",
    direccion_mac="00:1B:44:11:3A:B7",
    frecuencia_ghz=5.5
)


luz1 = LuzInteligente("LUZ-01")
luz2 = LuzInteligente("LUZ-02")

ac1 = AireAcondicionado("AC-01")
ac2 = AireAcondicionado("AC-02")

ac1.temperatura = 45.0   # activa condición peligrosa
ac2.temperatura = 30.0

central.vincular_dispositivo(luz1)
central.vincular_dispositivo(luz2)
central.vincular_dispositivo(ac1)
central.vincular_dispositivo(ac2)

print("Dispositivos vinculados:", central.dispositivos)

try:
    central.ejecutar_ciclo()
    print("Ciclo ejecutado correctamente")
    print("Estado central:", central.estado)
except Exception as e:
    print("Error:", e)

print("\nEnergías después del ciclo:")

for d in central.dispositivos:
    print(d.id_modelo, "->", d.energia)

print("\nEstado final:", central.estado)

try:
    central.ejecutar_ciclo()
except RuntimeError as e:
    print("\nBloqueo activado correctamente:")
    print(e)