from django.urls import path
from . import views
from django.views import static
from django.conf import settings



urlpatterns = [
    path("",  views.home, name="home")
]