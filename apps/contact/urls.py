from django.urls import path

from contact import views

# name_spcace --> contact:index
app_name = 'contact'

urlpatterns = [
    path('', views.index, name='index'),
]
