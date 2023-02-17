from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.create),
    path('read/', views.read),
    path('update/<int:id>', views.update),
]
