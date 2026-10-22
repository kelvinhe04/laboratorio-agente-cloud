def agregar_tarea(tareas, titulo):
    titulo = titulo.strip()
    if not titulo:
        raise ValueError("El título es obligatorio")
    tarea = {"id": len(tareas) + 1, "titulo": titulo, "completada": False}
    tareas.append(tarea)
    return tarea


def completar_tarea(tareas, tarea_id):
    for tarea in tareas:
        if tarea["id"] == tarea_id:
            tarea["completada"] = True
            return tarea
    raise ValueError("Tarea no encontrada")


def pendientes(tareas):
    return [t for t in tareas if not t["completada"]]
