from django.contrib import admin
from .models import Todo

# Register your models here.

class todoAdmin(admin.ModelAdmin):
    list_display = ['id','user','title','description','completed','created_at']

    # def save_model(self, request, obj, form, change):
    #     obj.user = request.user
    #     super().save_model(request, obj, form, change)

admin.site.register(Todo,todoAdmin)