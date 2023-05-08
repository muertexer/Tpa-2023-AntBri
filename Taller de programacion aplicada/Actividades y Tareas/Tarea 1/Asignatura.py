# Por Sebastian Adriazola, Antoine Briones, Benjamin Burgos y Cristopher González  


# Se debe realizar un registro de las Asignaturas y sus Estudiantes.
# Una Asignatura tiene un nombre, fecha inicio clases y un estudiante.
# Un Estudiante tiene un nombre, fecha de nacimiento, carrera y año ingreso.
# Cree una asignatura y un estudiante con sus datos ingresados por teclado.

# Estructura de Asignatura
# Estructura de Estudiante
# Ingresar datos de Asignatura
# Ingresar datos de Estudiante
# Mostrar datos de Asignatura y Estudiante


class Asignaturas:
    def __init__(self, nombre_asig, inicio):
        self.nombre_asig = str(nombre_asig)
        self.inicio = str(inicio)

    def getNombre_asig(self):
        return "Nombre de Asignatura:" +" "+ self.nombre_asig

    def getIncio(self):
        return "Fecha de inicio de clases:" +" "+self.inicio


    def __str__(self):
        return "Nombre de Asignatura: " + str(self.nombre_asig) + \
        "\t\tFecha de inicio de clases: " + str(self.inicio)



class Estudiantes(Asignaturas):
    def __init__(self, nombre_asig, incio, nombre_est, nac_est, carrera, ingreso):
        super().__init__(nombre_asig, incio)
        self.nombre_est = str(nombre_est)
        self.nac_est = str(nac_est)
        self.carrera = str(carrera)
        self.ingreso = str(ingreso)

    def getNombre_est(self):
        return "Nombre de Estudiante:" + " " + self.nombre_est

    def getNac_est(self):
        return "Fecha de nacimiento:" + " " + self.nac_est

    def getCarrera(self):
        return "Carera:" + " " + self.carrera

    def getIngreso(self):
        return "Año de ingreso:" + " " + self.ingreso


    def __str__(self):
        return "Nombre de Asignatura: " + str(self.nombre_asig) + "\t\tFecha de inicio de clases: " + \
            str(self.inicio) + "\nEstudiante: " + str(self.nombre_est) + "\t\tFecha de nacimiento: " + \
            str(self.nac_est) + "\t\tCarera: " + str(self.carrera) + "\t\tAño de ingreso: " + str(self.ingreso)


# TESTEO

asignatura1 = Asignaturas("lenguaje", "20/05/351")
print(asignatura1)
print(asignatura1.getIncio())
print(asignatura1.getNombre_asig())
print("\n\n")
estudiate1 = Estudiantes("lenguaje", "20/05/351", "mauricio algo", "15/07/2003", "icinf", "2022")
print(estudiate1)
print("\n\n")
print(estudiate1.getNombre_asig())
print(estudiate1.getIncio())
print(estudiate1.getNombre_est())
print(estudiate1.getNac_est())
print(estudiate1.getCarrera())
print(estudiate1.getIngreso())

