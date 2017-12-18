from django.urls import path
from functionality import views

urlpatterns = [
    path('', views.index, name='index'),
    path('calc/', views.calculations, name='calculations'),
]
