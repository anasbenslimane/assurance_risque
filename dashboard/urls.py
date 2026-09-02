from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [

    # Connexion
    path("", views.login_view, name="login"),
    path("login/", views.login_view, name="login"),

    # Espace agent
    path("dashboard/", views.dashboard, name="dashboard"),
    path("prediction/", views.prediction, name="prediction"),
    path("analysis/", views.analysis, name="analysis"),
    path("history/", views.history, name="history"),

    # Déconnexion
    path("logout/", LogoutView.as_view(), name="logout"),
]