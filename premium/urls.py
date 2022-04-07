from django.urls import path
from .import views

urlpatterns = [ 
    path('premium/',views.Premium,name="premium")
]