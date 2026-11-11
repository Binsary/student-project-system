from django.contrib.auth import views as auth_views
from django.urls import path

from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("projects/", views.project_list, name="project_list"),
    path("projects/add/", views.add_project, name="add_project"),
    path("projects/<int:pk>/edit/", views.edit_project, name="edit_project"),
    path("projects/<int:pk>/delete/", views.delete_project, name="delete_project"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="projects/login.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(next_page="home"),
        name="logout",
    ),
]

