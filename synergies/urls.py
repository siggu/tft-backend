from django.urls import path
from . import views

urlpatterns = [
    path("origin", views.Origins.as_view()),
    path("job", views.Jobs.as_view()),
]
