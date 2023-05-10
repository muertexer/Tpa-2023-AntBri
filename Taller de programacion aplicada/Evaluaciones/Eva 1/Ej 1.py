# I. Sección Teórica (40 puntos)

# 1.TODO (4 puntos) Indique los comandos para crear subir la versión del proyecto git a un repositorio remoto.

    # git init - para inicializar el repositorio en nuestro equipo
    # git add - para agregar los archivos al "stagging area"
    # git status - para corroborar cambios
    # git commit - para guardar los cambios de forma permanente en el repositorio
    # git remote add origin "URL del respositorio" - para sincronizar el repositorio local con el repositorio remoto
    # git push -u origin main - para enviar los cambios

# 2.TODO (4 puntos) ¿Cómo se puede utilizar el código de un proyecto git en un repositorio remoto
# (GitHub) en un computador local?

    # La manera que actualmente utilizo es la de descargar el repositorio en un zip, una vez descargado
    # lo puedo usar libremente en mi computador local

# 3.TODO  (4 puntos) Si se implementa un código en Python que crea un objeto de una clase abstracta,
# ¿Qué sucede al ejecutar dicho código?

    # el objeto no podrá ser instanciado, ni utilizado y sirve de base para crear otros objetos, a modo de armazón


# 4.TODO  (4 puntos) ¿Qué significa que un método tenga el decorador @abstractmethod?

    # significa que ese método se convierte en un método abstracto
    #

# 5.TODO  (4 puntos) Indique 3 eventos que pueden ejecutarse en una interfaz gráfica de usuario.

    # oprimir un botón y que este haga algo con QPushButton
    # Escribir en un QLineEdit
    # utilizar un slider para determinar algo con QSlider

# 6.TODO  (4 puntos) ¿Qué es el ciclo de eventos?

    # se entiende por ciclo como algo repetitivo, en este caso de eventos, lo que se puede explicar como un proceso
    # en el que una serie de eventos encadenados por codigo son repetidos infinitamente o hasta que sea completada
    # una tarea a realizar


# 7.TODO  (4 puntos) Si desde la ventana principal de un programa se lanza un objeto de clase QDialog
# ¿Es posible ignorarlo y seguir utilizando la ventana principal?

    # No es posible ignorarlo ya que tiene mas prioridad que la ventana principal, por ende hasta que no se realiza
    # la tarea pedida en este, no se podra utilizar la ventana principal.
    # Es posible quitarle esta prioridad al momento de codificarlo.

# 8.TODO  (4 puntos) Mencione al menos 5 componentes gráficos de PyQt6

    # QLabel, muestra un texto o si se configura de alguna manera, puede mostrar una imagen
    # QPushButton, muestra un botón
    # QLineEdit, muestra un cuadro de texto editable
    # QListWidget, muestra una lista de texto ingresado previamente
    # QSlider, muestra un control deslizable
    # QCalendarWidget, muestra un calendario
    # QProgressBar, muestra una barra de carga o de avance

# 9.TODO  (4 puntos) Si se requiere de ingresar datos numéricos, qué alternativas existen de componentes
# en PyQt6

    # es posible usar un QSlider en el que en su recorrido se utilicen numeros
    # Un QLineEdit para ingresar str y de ahi convertirlo a numeros, de la misma manera se puede usar un QTextEdit
    # un QSpinBox y/o un QDoubleSpinBox el cual desconozco pero supongo que ingresa directamente valores numericos

# 10.TODO  (4 puntos) ¿Cómo es posible utilizar una interfaz creada con Qt Designer en un código fuente
# en Python con PyQt6?

    # utilizando el comando " pyuic6 -o archivo.py archivo.ui "
    # el archivo.py es el nombre del archivo resultante y el archivo.ui es el archivo a convertir

    # otra manera es usando directamente la interfaz de QtDesigner, en Formulario/ View Python Code...
    # aca es posible guardar directamente el archivo, copiarlo, buscar texto y seleciconar trozos de texto

