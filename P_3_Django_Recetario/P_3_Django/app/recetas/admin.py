from django.contrib import admin
from .models import Receta


class RecetasAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'preparacion', 'foto')
    search_fields = ('nombre', 'preparacion')
    

admin.site.register(Receta, RecetasAdmin)
admin.site.site_header = 'Practica de Django con recetas'
admin.site.index_title = 'Panel de control de las recetas'
admin.site.site_title = 'PabloMorenillaPinos'