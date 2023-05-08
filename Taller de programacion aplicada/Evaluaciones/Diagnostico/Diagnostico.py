## Integrantes: Sebastian Adriazola y Antoine Briones

# Clase: Chistes
# id : int


class Chistes:
    def __init__(self):
        self.chistes = [
            "\nIntenté enamorar a una programadora, pero no se dejaba.\
            \n¿Has probado con Python?",
            "\n- Eres un fanático de la computación, ¿cierto?.\
            \n- Si... mouse o menos.",
            "\n- Mamá, ¿qué haces en frente de la computadora con los ojos cerrados?\
            \n- Nada, hijo, es que Windows me dijo que cerrara las pestañas.",
            "\nError 0094782: No se detecta ningún teclado pulse una tecla para continuar...",
            "\nUn informático, un economista y un ingeniero van en un coche por la autovía. \
            \nDe pronto el coche inexplicablemente se para. Los tres se ponen a pensar y dar soluciones.\
            \nEl Ingeniero: - Ya está, se llama a la grúa y que nos traigan otro.\
            \nEl economistas: - No, no, mejor tratamos de repararlo nosotros mismos.\
            \nEl informático: - Esto es muy fácil: ¡salgamos y volvamos a entrar!"
        ]
        self.id = 0

    def mostrar(self):
        if self.id >= len(self.chistes):
            self.id = 0
        ch = self.chistes[self.id]
        self.id += 1
        return ch

chistes = Chistes()
while input("\nEscriba 'Si' para mostrar un chiste, o cualquier otra tecla para salir: ").upper() == 'SI':
    print(chistes.mostrar())
