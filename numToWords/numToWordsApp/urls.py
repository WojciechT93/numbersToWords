from django.urls import path
from . import views

urlpatterns = [
    path('chooseNumber/', views.chooseNumber),
    path('result/',views.result),
]