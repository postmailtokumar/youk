from django.urls import path

from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('employee_list', views.employee_list),
    path('employee_add', views.employee_add)
]