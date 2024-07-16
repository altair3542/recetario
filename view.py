#view.py

class Vista:
    def mostrar(self, recetas):
        for indice, receta in enumerate(recetas):
            print(f"{indice + 1}. {receta.nombre}: {receta.descripcion}")

    def pedir_dato(self, dato):
        print(f"{dato}?")
        return input(">").strip()
