from django.db import models

# Create your models here.

class RegistrationExternalities(models.Model):
    
    classificationChoise = (
        ('red', 'Red'),
        ('seguridad', 'Seguridad'),        
    )

    name = models.CharField('nombre', max_length=250, blank=False, null=False)
    description = models.TextField('descripción', blank=True, null=True)
    classification = models.CharField('clasificación', max_length = 250, blank=False, null=False, choices = classificationChoise, default = "Red")
    revised = models.BooleanField('revisada', default=False)
    userIncidents = models.CharField('Usuario', max_length=250, blank=False, null=False, default='Usuario de la incidencia')
    date = models.DateTimeField('Fecha', auto_now_add = True)


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'incidencia'
        verbose_name_plural = 'incidencias'
        ordering = ['-date']