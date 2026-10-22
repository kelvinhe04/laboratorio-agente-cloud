import unittest
from tasks import agregar_tarea, completar_tarea, eliminar_tarea, pendientes


class TestTasks(unittest.TestCase):
    def test_agregar_tarea(self):
        tareas = []
        tarea = agregar_tarea(tareas, "Leer documentación", "Estudio")
        self.assertEqual(tarea["titulo"], "Leer documentación")
        self.assertEqual(tarea["categoria"], "Estudio")
        self.assertFalse(tarea["completada"])

    def test_agregar_tarea_categoria_vacia(self):
        tareas = []
        with self.assertRaises(ValueError):
            agregar_tarea(tareas, "Leer documentación", "  ")

    def test_completar_tarea(self):
        tareas = []
        agregar_tarea(tareas, "Practicar", "Laboratorio")
        completar_tarea(tareas, 1)
        self.assertEqual(pendientes(tareas), [])

    def test_pendientes_filtra_por_categoria_sin_mayusculas(self):
        tareas = []
        agregar_tarea(tareas, "Practicar unittest", "Laboratorio")
        agregar_tarea(tareas, "Leer documentación", "Estudio")
        agregar_tarea(tareas, "Revisar PR", "laboratorio")
        completar_tarea(tareas, 3)

        resultado = pendientes(tareas, "lAbOrAtOrIo")

        self.assertEqual(len(resultado), 1)
        self.assertEqual(resultado[0]["titulo"], "Practicar unittest")

    def test_pendientes_categoria_inexistente_devuelve_vacia(self):
        tareas = []
        agregar_tarea(tareas, "Practicar unittest", "Laboratorio")
        agregar_tarea(tareas, "Leer documentación", "Estudio")

        resultado = pendientes(tareas, "Trabajo")

        self.assertEqual(resultado, [])

    def test_pendientes_categoria_solo_espacios_equivale_sin_filtro(self):
        tareas = []
        agregar_tarea(tareas, "Practicar unittest", "Laboratorio")
        agregar_tarea(tareas, "Leer documentación", "Estudio")
        completar_tarea(tareas, 2)

        resultado_sin_filtro = pendientes(tareas)
        resultado_con_espacios = pendientes(tareas, "   ")

        self.assertEqual(resultado_con_espacios, resultado_sin_filtro)

    def test_eliminar_tarea_existente(self):
        tareas = []
        agregar_tarea(tareas, "Practicar unittest", "Laboratorio")
        tarea_eliminada = agregar_tarea(tareas, "Leer documentación", "Estudio")

        resultado = eliminar_tarea(tareas, 2)

        self.assertEqual(resultado, tarea_eliminada)
        self.assertEqual(len(tareas), 1)
        self.assertEqual(tareas[0]["id"], 1)
        self.assertEqual(pendientes(tareas), [tareas[0]])

    def test_eliminar_tarea_id_inexistente(self):
        tareas = []
        agregar_tarea(tareas, "Practicar unittest", "Laboratorio")
        tareas_originales = tareas.copy()

        with self.assertRaisesRegex(ValueError, "Tarea no encontrada"):
            eliminar_tarea(tareas, 99)

        self.assertEqual(tareas, tareas_originales)

    def test_eliminar_tarea_conserva_ids_restantes(self):
        tareas = []
        agregar_tarea(tareas, "Tarea 1", "Laboratorio")
        agregar_tarea(tareas, "Tarea 2", "Laboratorio")
        agregar_tarea(tareas, "Tarea 3", "Laboratorio")

        eliminar_tarea(tareas, 2)

        self.assertEqual([tarea["id"] for tarea in tareas], [1, 3])


if __name__ == "__main__":
    unittest.main()
