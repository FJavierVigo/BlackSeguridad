
def registrar_agente(agentes):
    print("\n--- REGISTRAR AGENTE ---")
    codigo = input("Código del agente: ").strip().upper()
    nombre = " ".join(input("Nombre completo: ").strip().split())

    if not codigo or not nombre:
        print("Error: el código y el nombre son obligatorios.")
        return

    for agente in agentes:
        if agente["codigo"] == codigo:
            print("Error: ya existe un agente con ese código.")
            return

    agentes.append({"codigo": codigo, "nombre": nombre})
    print("Agente registrado correctamente.")


def registrar_puesto(puestos):
    print("\n--- REGISTRAR PUESTO ---")
    codigo = input("Código del puesto: ").strip().upper()
    nombre = " ".join(input("Nombre del puesto: ").strip().split())

    if not codigo or not nombre:
        print("Error: el código y el nombre son obligatorios.")
        return

    for puesto in puestos:
        if puesto["codigo"] == codigo:
            print("Error: ya existe un puesto con ese código.")
            return

    puestos.append({"codigo": codigo, "nombre": nombre})
    print("Puesto registrado correctamente.")
