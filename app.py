#app.py

from cookbook import LibroDeRecetas
from controller import Controlador
from router import Enrutador

archivo_csv = 'recetas.csv'
libro_de_recetas = LibroDeRecetas(archivo_csv)
controlador = Controlador(libro_de_recetas)

enrutador = Enrutador(controlador)

enrutador.ejecutar()
