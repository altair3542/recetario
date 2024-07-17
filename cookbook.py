#cookbook.py

import csv
import os
from recipe import Receta


class LibroDeRecetas:
    def __init__(self, archivo_csv):
        self.archivo_csv = archivo_csv
        self.recetas = []
        self.asegurar_csv_existe()
        self.cargar_csv()

    def asegurar_csv_existe(self):
        if not os.path.exists(self.archivo_csv):
            with open(self.archivo_csv, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['nombre', 'descripcion'])

    def todas(self):
        return self.recetas

    def agregar_receta(self, receta):
        self.recetas.append(receta)
        self.guardar_csv()

    def eliminar_receta(self, indice_receta):
        self.recetas.pop(indice_receta)
        self.guardar_csv()

    def cargar_csv(self):
        with open(self.archivo_csv, 'r') as archivo:
            lector = csv.reader(archivo)
            for fila in lector:
                self.recetas.append(Receta(fila[0], fila[1]))

    def guardar_csv(self):
        with open(self.archivo_csv, 'w') as archivo:
            escritor = csv.writer(archivo)
            for receta in self.recetas:
                escritor.writerow([receta.nombre, receta.descripcion])
