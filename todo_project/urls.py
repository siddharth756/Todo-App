
from django.contrib import admin
from django.urls import path,include

app_name = 'todo_app'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("todo_app.urls")),
]
