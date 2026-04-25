tareas = []

def mostrar_tareas():
    if len(tareas) == 0:
        print("\n📋 No tienes tareas pendientes.")
    else:
        print("\n📋 Tus tareas:")
        for i, tarea in enumerate(tareas, 1):
            print(f"  {i}. {tarea}")

def agregar_tarea():
    tarea = input("\n¿Qué tarea quieres añadir? ")
    tareas.append(tarea)
    print(f"✅ Tarea '{tarea}' añadida.")

def eliminar_tarea():
    mostrar_tareas()
    if len(tareas) > 0:
        num = int(input("\n¿Qué número de tarea quieres eliminar? "))
        eliminada = tareas.pop(num - 1)
        print(f"🗑️ Tarea '{eliminada}' eliminada.")

while True:
    print("\n--- GESTOR DE TAREAS ---")
    print("1. Ver tareas")
    print("2. Añadir tarea")
    print("3. Eliminar tarea")
    print("4. Salir")
    
    opcion = input("\nElige una opción: ")
    
    if opcion == "1":
        mostrar_tareas()
    elif opcion == "2":
        agregar_tarea()
    elif opcion == "3":
        eliminar_tarea()
    elif opcion == "4":
        print("¡Hasta luego Pablo! 👋")
        break
    else:
        print("❌ Opción no válida.")