from django.contrib import admin
from .models import Page

# Register your models here.
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')

    class Media:
        css = {
            'all': ('pages/css/custom_ckeditor.css',)
        }
    #Esto nos servira para que el cuadro de contenido sea responsivo importando

admin.site.register(Page, PageAdmin)
