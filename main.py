
from registro import registrar_agente, registrar_puesto
from turnos import crear_turno, asignar_agente, consultar_cobertura
from datos import buscar_agente, guardar_datos, cargar_datos


datos = cargar_datos()

while True:
    print("\n===== SISTEMA BLACK SEGURIDAD =====")
    print("1. Registrar agente")
    print("2. Registrar puesto")
    print("3. Crear turno")
    print("4. Asignar agente")
    print("5. Consultar cobertura")
    print("6. Buscar agente")
    print("7. Guardar y salir")

    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
        registrar_agente(datos["agentes"])
    elif opcion == "2":
        registrar_puesto(datos["puestos"])
    elif opcion == "3":
        crear_turno(datos["turnos"], datos["puestos"])
    elif opcion == "4":
        asignar_agente(datos["agentes"], datos["turnos"])
    elif opcion == "5":
        consultar_cobertura(datos["turnos"])
    elif opcion == "6":
        buscar_agente(datos["agentes"])
    elif opcion == "7":
        if guardar_datos(datos):
            print("Hasta pronto.")
            break
    else:
        print("Opción no válida. Intenta nuevamente.")
