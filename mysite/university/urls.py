from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("teacher/", views.add_teacher, name="add-teacher"),
    path("teachers/", views.show_teachers, name="teachers"),
]
