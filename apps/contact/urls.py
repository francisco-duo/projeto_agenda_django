from contact import views
from django.urls import path

# name_spcace --> contact:index
app_name = 'contact'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:contact_id>/', views.contact, name='contact'),
]
