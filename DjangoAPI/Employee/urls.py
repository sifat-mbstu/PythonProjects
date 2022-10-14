"""from django.conf.urls import url"""
from django.urls import re_path,path
from Employee import views

"""
urlpatterns = [
    url(r'^department$',views.departmentApi),
    url(r'^department/([0-9]+)$', views.departmentApi)
]
from django.urls import include, path
"""
urlpatterns = [
    path('', views.departmentApi, name=''),
    path('department/', views.departmentApi, name=''),
    path('department/<id>/', views.departmentApi, name=''),
    
    path('employee/', views.employeeApi, name=''),
    path('employee/<id>/', views.employeeApi, name=''),
    
    path('employee/savefile/', views.SaveFile),
]
