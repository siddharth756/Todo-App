from django.urls import path 
from todo_app.views import todolistview,tododetailview,todocreateview,todoupdateview,tododeleteview,signupview,loginview,logoutview

urlpatterns = [
    path('',todolistview.as_view(),name="home"),
    path('create/',todocreateview.as_view(),name="create"),
    path('todo/<int:pk>/',tododetailview.as_view(),name="detail"),
    path('todo/<int:pk>/update',todoupdateview.as_view(),name="update"),
    path('todo/<int:pk>/delete',tododeleteview.as_view(),name="delete"),
    path('signup/',signupview.as_view(),name="signup"),
    path('login/',loginview.as_view(),name="login"),
    path('logout/',logoutview,name="logout"),
]
