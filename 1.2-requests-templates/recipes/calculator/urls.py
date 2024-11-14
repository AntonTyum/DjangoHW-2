from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:recipe_name>/', views.recipe_view, name='recipe_view'),
]