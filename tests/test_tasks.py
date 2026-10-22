import unittest
from tasks import agregar_tarea, completar_tarea, pendientes


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


if __name__ == "__main__":
    unittest.main()
