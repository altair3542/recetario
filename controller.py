#controller.py

from recipe import Receta
from view import Vista

class Controlador:
    def __init__(self, cookbook):
        self.cookbook = cookbook
        self.view = Vista()

    def listar(self):
        recetas = self.cookbook.todas()
        self.view.mostrar(recetas)

    def crear(self):
        nombre = self.view.pedir_dato("Nombre de la receta")
        descripcion = self.view.pedir_dato("Descripcion de la receta")
        receta = Receta(nombre, descripcion)
        self.cookbook.agregar_receta(receta)
