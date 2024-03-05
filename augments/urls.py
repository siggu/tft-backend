from django.urls import path
from . import views

urlpatterns = [
    path("", views.Augments.as_view()),
    path("silver/", views.SilverAugments.as_view()),
    path("gold/", views.GoldAugments.as_view()),
    path("prismatic/", views.PrismaticAugments.as_view()),
]
