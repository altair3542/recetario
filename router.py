class Enrutador:
    def __init__ (self, controlador):
        self.controlador = controlador

    def ejecutar(self):
        print("Bienvenido al recetario")
        print("          --          ")

        while True:
            self.mostrar_tareas()
            accion = int(input().strip())
            self.enrutar_accion(accion)

    def mostrar_tareas(self):
        print("")
        print("Que quieres hacer a continuación?")
        print("1 - listar todas las recetas")
        print("2 - Añadir una nueva receta")
        print("3 - Salir")

    def enrutar_accion(self, accion):
        if accion == 1:
            self.controlador.listar()
        elif accion == 2:
            self.controlador.crear()
        elif accion == 3:
            self.detener()
        else:
            print("Por favor, selecciona una opcion valida")

    def detener(self):
        print("adios")
        exit()

        
