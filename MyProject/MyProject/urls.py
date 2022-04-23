from django.contrib import admin
from django.urls import path
from MyApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="Home"),
    path('addData', views.addData,name="addData"),
    path('updateData/<int:id>', views.updateData),
    path('deleteData/<int:id>', views.deleteData),
]
