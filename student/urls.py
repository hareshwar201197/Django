
from django.urls import path
from .views import *
urlpatterns = [
    path("",home),
    path("home/",home),
    path("add-student/", add_student),
    path("delete-student/<int:roll>", delete_student),
    path("update-student/<int:roll>", update_student),
    path("do-update-student/<int:roll>", do_update_student),
]