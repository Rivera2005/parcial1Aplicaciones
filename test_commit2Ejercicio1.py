from ejercicio1 import Tren, VagonCargaSeca, VagonCisterna

print("=== CASO 1: Tren válido ===")

try:
    tren = Tren("T001", "L001", "GE", 1000)

    tren.enganchar_vagon(
        VagonCargaSeca("VS1", 20, 80)
    )  # peso = 100

    tren.enganchar_vagon(
        VagonCisterna("VC1", 10, 20000, 0.001)
    )  # peso = 30

    print("Peso total del tren:", tren.obtener_peso_tren())
    print("Tren creado correctamente")

except ValueError as e:
    print("ERROR:", e)


print("\n=== CASO 2: Más de 3 cisternas ===")

try:
    tren = Tren("T002", "L002", "GE", 1000)

    # Mucho peso seco para que no falle por el 60%
    tren.enganchar_vagon(
        VagonCargaSeca("VS1", 50, 250)
    )  # peso = 300

    tren.enganchar_vagon(
        VagonCisterna("VC1", 10, 10000, 0.001)
    )  # peso = 20

    tren.enganchar_vagon(
        VagonCisterna("VC2", 10, 10000, 0.001)
    )  # peso = 20

    tren.enganchar_vagon(
        VagonCisterna("VC3", 10, 10000, 0.001)
    )  # peso = 20

    print("Se agregaron 3 cisternas correctamente")

    # Debe fallar
    tren.enganchar_vagon(
        VagonCisterna("VC4", 10, 10000, 0.001)
    )

except ValueError as e:
    print("ERROR:", e)


print("\n=== CASO 3: Supera el 60% del peso total ===")

try:
    tren = Tren("T003", "L003", "GE", 1000)

    tren.enganchar_vagon(
        VagonCargaSeca("VS1", 20, 80)
    )  # peso = 100

    tren.enganchar_vagon(
        VagonCisterna("VC1", 10, 20000, 0.001)
    )  # peso = 30

    tren.enganchar_vagon(
        VagonCisterna("VC2", 10, 40000, 0.001)
    )  # peso = 50

    # Aquí debería dispararse la restricción del 60%
    tren.enganchar_vagon(
        VagonCisterna("VC3", 10, 80000, 0.001)
    )

except ValueError as e:
    print("ERROR:", e)