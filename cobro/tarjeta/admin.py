from django.contrib import admin
from .models import Cliente, Pagaduria, Banco, Rtarjeta, Empresa


# Register your models here.
class TarjetaAdmin(admin.ModelAdmin):
    list_display= ('cliente','empresa','pagaduria','banco', 'cuota','clave')
    search_fields =('cliente__nombres','cliente__apellidos','empresa__nombre','pagaduria__nombre','banco__nombre')
    def Cliente(self, obj):        
        return obj.cliente.apellidos, obj.cliente.nombres
    def pagaduria(self, obj):        
        return obj.empresa.nombre
    def pagaduria(self, obj):        
        return obj.pagaduria.nombre
    def banco(self, obj):       
        return obj.banco.nombre
   
class ClienteAdmin(admin.ModelAdmin):
     list_display=('identificacion','apellidos', 'nombres') 
     search_fields =('identificacion','apellidos', 'nombres') 





admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Banco)
admin.site.register(Rtarjeta, TarjetaAdmin)
admin.site.register(Empresa)
admin.site.register(Pagaduria)

