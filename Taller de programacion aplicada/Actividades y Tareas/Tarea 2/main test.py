from abc import ABC, abstractmethod

class Camara(ABC):
    def __init__(self, idcam, nombre, resolucion):
        self.idcam = idcam
        self.nombre = nombre
        self.resolucion = resolucion

    @abstractmethod
    def tr(self):
        pass

class Sesion:
    def __init__(self, id, nombre_asignatura, nombre_profesor, sala, fecha_clase, hora_inicio, hora_fin):
        self.id = id
        self.nombre_asignatura = nombre_asignatura
        self.nombre_profesor = nombre_profesor
        self.sala = sala
        self.fecha_clase = fecha_clase
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.camara_en_uso = None
        self.lista_camaras = []

    def agregar_camara(self, camara):
        self.lista_camaras.append(camara)

    def cambiar_camara(self, indice):
        if indice < len(self.lista_camaras):
            self.camara_en_uso = self.lista_camaras[indice]
            print(f"Cambiando a la cámara {self.camara_en_uso.nombre}")
        else:
            print("Índice de cámara inválido")

    def crear_camara(self):
        idcam = input("Ingrese el ID de la cámara: ")
        nombre = input("Ingrese el nombre de la cámara: ")
        resolucion = input("Ingrese la resolución de la cámara: ")
        camara = Camara(idcam, nombre, resolucion)
        self.agregar_camara(camara)

class Main:
    def __init__(self):
        self.sesion = None

    def crear_sesion(self):
        self.sesion = Sesion(input("Ingrese el ID de la sesión: "),
                             input("Ingrese el nombre de la asignatura: "),
                             input("Ingrese el nombre del profesor: "),
                             input("Ingrese el nombre de la sala: "),
                             input("Ingrese la fecha de la clase (en formato AAAA-MM-DD): "),
                             input("Ingrese la hora de inicio de la clase (en formato HH:MM): "),
                             input("Ingrese la hora de fin de la clase (en formato HH:MM): "))
        print(f"Sesión creada con ID {self.sesion.id}")

    def crear_camara(self):
        self.sesion.crear_camara()

    def cambiar_camara(self):
        indice = int(input("Ingrese el índice de la cámara a la que desea cambiar: "))
        self.sesion.cambiar_camara(indice)

    def ejecutar(self):
        opcion = input("¿Desea crear una sesión? (s/n): ")
        if opcion == "s":
            self.crear_sesion()
        while True:
            opcion = input("Ingrese 'c' para crear una cámara, 's' para cambiar de cámara o 'salir' para terminar: ")
            if opcion == "c":
                self.crear_camara()
            elif opcion == "s":
                self.cambiar_camara()
            elif opcion == "salir":
                break

# Ejemplo de uso
main = Main()
main.ejecutar()
