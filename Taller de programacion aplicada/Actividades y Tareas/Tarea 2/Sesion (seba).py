import datetime

class sesion:
    def __init__ (self, id,nombre_asig,profe,sala,fecha,hora , cam_vivo , lista_cam):
        self.id = id
        self.nombre_asig = nombre_asig
        self.profe = profe
        self.sala = sala
        self.fecha = fecha
        self.hora = hora
        self.cam_vivo = cam_vivo
        self.lista_cam = lista_cam
        
    def iniciar_transmision():
        iniciar = input("Inicie transmision con ENTER: ")
        return iniciar
    def terminar_transmision():
        terminar = input("Terminar transmision con ENTER: ")
        return terminar
    def cambiar_camara():
        click = input("Presione flechas <- en casod e querer volver a la camara anterior y -> para la camara siguiente:")
        return click
    
    
    def get_id(self):
        return self.id
    
    def get_nombre_asig(self):
        return self.nombre_asig
    
    def get_profe(self):
        return self.profe
    
    def get_sala (self):
        return self.sala
    
    def get_fecha():
        fecha = datetime.datetime.now().date()
        return fecha
    
    def get_hora():
        hora_inicial = datetime.datetime.now()
        hora = hora_inicial.strftime('%H:%M')
        return hora
    
    def camara_en_uso(self):
        return self.cam_vivo
    
    def lista_camaras(self):
        return self.lista_cam
    
    
       

