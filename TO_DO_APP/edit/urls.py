from django.conf.urls import url
from django.contrib import admin
from edit import views
from django.urls import path, include

urlpatterns = [
  path('', views.edit_link),
  path('edit_todo/<int:todo_id>', views.edit_todo)
]
