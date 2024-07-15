from django.urls import path
from . import views

urlpatterns = [
    path("set11", views.Set11Traits.as_view()),
    path("set12", views.Set12Traits.as_view())
]
