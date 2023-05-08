from Sesion import Sesion

class main:
    idSes = int(input("Ingrese el ID de la sesión: "))
    NomAs = input("Ingrese el nombre de la asignatura: ")
    NomProf = input("Ingrese el nombre del profesor: ")
    sala = input("Ingrese el nombre de la sala: ")
    FeClase = input("Ingrese la fecha de la clase (formato DD-MM-YYYY): ")
    HIni = input("Ingrese la hora de inicio de la clase (formato HH:MM): ")
    HFin = input("Ingrese la hora de fin de la clase (formato HH:MM): ")
    sesion = Sesion(idSes, NomAs, NomProf, sala, FeClase, HIni, HFin)
        
            
        