
from datetime import datetime


def crear_turno(turnos, puestos):
    print("\n--- CREAR TURNO ---")
    codigo = input("Código del turno: ").strip().upper()
    codigo_puesto = input("Código del puesto: ").strip().upper()
    fecha = input("Fecha (DD-MM-AAAA): ").strip()

    if not codigo or not codigo_puesto:
        print("Error: los códigos son obligatorios.")
        return

    for turno in turnos:
        if turno["codigo"] == codigo:
            print("Error: ese código de turno ya existe.")
            return

    if not any(puesto["codigo"] == codigo_puesto for puesto in puestos):
        print("Error: el puesto no está registrado.")
        return

    try:
        datetime.strptime(fecha, "%d-%m-%Y")
        inicio = int(input("Hora de inicio (0 a 23): "))
        fin = int(input("Hora de fin (1 a 24): "))
    except ValueError:
        print("Error: fecha u horas incorrectas.")
        return

    if not (0 <= inicio < fin <= 24):
        print("Error: el turno debe empezar y terminar el mismo día.")
        return

    for turno in turnos:
        mismo_puesto = turno["codigo_puesto"] == codigo_puesto
        misma_fecha = turno["fecha"] == fecha
        se_superponen = inicio < turno["fin"] and turno["inicio"] < fin
        if mismo_puesto and misma_fecha and se_superponen:
            print("Error: el puesto ya tiene un turno en ese horario.")
            return

    turnos.append({
        "codigo": codigo,
        "codigo_puesto": codigo_puesto,
        "fecha": fecha,
        "inicio": inicio,
        "fin": fin,
        "codigo_agente": ""
    })
    print("Turno creado correctamente.")


def validar_asignacion(agentes, turnos, codigo_agente, codigo_turno):
    existe_agente = False
    for agente in agentes:
        if agente["codigo"] == codigo_agente:
            existe_agente = True
            break

    if not existe_agente:
        return False, "El agente no está registrado."

    turno_elegido = None
    for turno in turnos:
        if turno["codigo"] == codigo_turno:
            turno_elegido = turno
            break

    if turno_elegido is None:
        return False, "El turno no existe."

    if turno_elegido["codigo_agente"] != "":
        return False, "El turno ya tiene un agente asignado."

    for turno in turnos:
        mismo_agente = turno["codigo_agente"] == codigo_agente
        misma_fecha = turno["fecha"] == turno_elegido["fecha"]
        se_superponen = (
            turno_elegido["inicio"] < turno["fin"]
            and turno["inicio"] < turno_elegido["fin"]
        )
        if mismo_agente and misma_fecha and se_superponen:
            return False, "El agente tiene otro turno en ese horario."

    return True, "Asignación válida."


def asignar_agente(agentes, turnos):
    print("\n--- ASIGNAR AGENTE ---")
    codigo_agente = input("Código del agente: ").strip().upper()
    codigo_turno = input("Código del turno: ").strip().upper()

    valido, mensaje = validar_asignacion(
        agentes, turnos, codigo_agente, codigo_turno
    )
    if not valido:
        print("Asignación rechazada:", mensaje)
        return

    for turno in turnos:
        if turno["codigo"] == codigo_turno:
            turno["codigo_agente"] = codigo_agente
            break

    print("Agente asignado correctamente.")


def consultar_cobertura(turnos):
    print("\n--- TURNOS SIN COBERTURA ---")
    encontrados = 0
    for turno in turnos:
        if turno["codigo_agente"] == "":
            print(
                f"Turno: {turno['codigo']} | Puesto: {turno['codigo_puesto']} | "
                f"Fecha: {turno['fecha']} | {turno['inicio']}:00 - {turno['fin']}:00"
            )
            encontrados += 1

    if encontrados == 0:
        print("No hay turnos pendientes de cobertura.")
