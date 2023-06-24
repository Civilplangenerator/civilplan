from django.urls import path
from . import views

urlpatterns = [
    path("build",views.build,name="build"),
    
]