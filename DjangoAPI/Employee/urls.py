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
    path('department/', views.departmentApi, name=''),
    path('department/<id>/', views.departmentApi, name=''),
]