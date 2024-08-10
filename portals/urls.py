from django.urls import path
from . import views

urlpatterns = [
    path("set11", views.Set11Portals.as_view()),
    path("set12", views.Set12Portals.as_view()),
    path("make-error",views.make_error)
]
