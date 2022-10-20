from django.db import models
from django.core.mail import send_mail
from django.utils.html import format_html
from datetime import datetime
from django.core.mail import send_mail

# Create your models here.

class Consulta(models.Model):

    CONTESTADA = 'Contestada'
    NOCONTESTADA = 'No Contestada'
    ENPROCESO = 'En_Proceso'
    DEVOLICIOND = (
        (CONTESTADA, 'Contestada'),
        (NOCONTESTADA, 'No Contestada'),
        (ENPROCESO, 'En Proceso'),
    )

    nombre                = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.TextField(blank=False, null=False)
    mail                  = models.EmailField(max_length=50, blank=True, null=True)
    estado_respuesta      = models.CharField(max_length=15, blank=True, choices=DEVOLICIOND, default=NOCONTESTADA)
    telefono              = models.CharField(max_length=90, blank=True, null=True)
    fecha = models.DateField(default=datetime.now, blank=True, editable=True)


    def __str__(self):

        return self.nombre
    

    def estado_de_respuesta(self):
        if self.estado_respuesta == 'Contestada':
            return format_html('<span style="background-color:#0a0; color: #fff; padding:5px;">{}</span>', self.estado_respuesta, )
        elif self.estado_respuesta == 'No Contestada':
            return format_html('<span style="background-color:#a00; color: #fff; padding:5px;"">{}</span>', self.estado_respuesta, )
        elif self.estado_respuesta == 'En_Proceso':
            return format_html('<span style="background-color:#F0B203; color: #000; padding:5px;"">{}</span>', self.estado_respuesta, )

class Respuesta(models.Model):

    consulta        = models.ForeignKey(Consulta, blank=False, null=True, on_delete=models.CASCADE)
    respuesta       = models.TextField()
    fecha           = models.DateField(default=datetime.now, blank=True, editable=False)
    #history = HistoricalRecords()


    def create_mensaje(self):

        consula_cambio_estado = Consulta.objects.get(id=self.consulta.id)
        consula_cambio_estado.estado_respuesta = "Contestada"
        consula_cambio_estado.save()

    def save(self, *args, **kwargs):
        self.create_mensaje()
        force_update = False
        if self.id:
            force_update = True
        super(Respuesta, self).save(force_update=force_update)