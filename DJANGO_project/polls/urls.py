from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_html, name="polls_name")
]
