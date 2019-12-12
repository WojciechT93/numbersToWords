from django.urls import path
from . import views

urlpatterns = [
    path('chooseNumber/', views.choose_number),
    path('result/',views.result),
]