from django.contrib import admin
from .models import Receta
from .models import Ingrediente


class RecetasAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'preparacion', 'foto')
    search_fields = ('nombre', 'preparacion')
    
class IngredientesAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cantidad', 'unidades', 'receta')
    search_fields = ('nombre', 'cantidad', 'unidades', 'receta')

admin.site.register(Receta, RecetasAdmin)
admin.site.site_header = 'Practica de Django 3_2 con recetas'
admin.site.index_title = 'Panel de control de las recetas'
admin.site.site_title = 'PabloMorenillaPinos'

admin.site.register(Ingrediente, IngredientesAdmin)
admin.site.site_header = 'Practica de Django 3_2 con ingredientes'
admin.site.index_title = 'Panel de control de las ingredientes'
admin.site.site_title = 'PabloMorenillaPinos'
