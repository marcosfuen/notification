from django.contrib import admin
from .models import RegistrationExternalities

import csv
import datetime
import time
import pytz
from datetime import datetime, timedelta
from django.http import HttpResponse
from django.conf import settings
# Register your models here.


class RegistrationExternalitiesAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'classification', 'revised', 'userIncidents', 'date']
    search_fields = ['name']
    exclude = ['userIncidents']
    actions = ['downloadCsv']
    changelist_actions = ('downloadCsv')
    # cambia el link del campo por e que quiero editar el objeto
    # list_display_links = ['date']
    
    def save_model(self, request, obj, form, change):
        obj.userIncidents = request.user.first_name + ' ' + request.user.last_name
        # obj.userIncidents = request.user.username
        super().save_model(request, obj, form, change)

    def downloadCsv(self, request, queryset):
        f = open('incidencias.csv',
                 'w', newline='', encoding="utf-8")
        writer = csv.writer(f, dialect='excel', delimiter=',')
        writer.writerow(["No".upper(), "Nombre".upper(), "Descripción".upper(), "Clasificación".upper(), "Revisadas".upper(), "Usuarios que reporto la incidencia".upper(), "Fecha".upper(), "Hora".upper()])
        count = 0
        for s in queryset:
            count += 1
            writer.writerow([count, str(s.name), str(s.description), str(s.classification), str(s.revised), str(s.userIncidents), str(s.date.astimezone(pytz.timezone(settings.TIME_ZONE)).__format__('%Y-%m-%d')) , str(s.date.astimezone(pytz.timezone(settings.TIME_ZONE)).__format__('%H:%M:%S'))])
        f.close()
        f = open('incidencias.csv', 'rb')
        response = HttpResponse(f, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=incidencias.csv'

        return response
    downloadCsv.label = 'Exportar a CSV'
    downloadCsv.short_description = "Generar incidencias en formato CSV"

admin.site.register(RegistrationExternalities, RegistrationExternalitiesAdmin)

admin.site.site_header = 'Notificación Incidencias - Log In'
admin.site.site_title = 'Sistema de reportes de incidencias - Administración'