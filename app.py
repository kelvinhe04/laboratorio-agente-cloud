from tasks import agregar_tarea, completar_tarea, pendientes

tareas = []
agregar_tarea(tareas, "Estudiar agentes cloud", "estudio")
agregar_tarea(tareas, "Preparar laboratorio", "preparacion")
completar_tarea(tareas, 1)

for tarea in pendientes(tareas):
    print(f'- {tarea["id"]}: {tarea["titulo"]}')
