from django.conf.urls import url
from django.contrib import admin
from . import views
from django.urls import path, include

urlpatterns = [
  url(r'^$', views.home, name='home'),
  path('addtodo/', views.addtodo),
  path('delete_todo/<int:todo_id>/', views.delete_todo),
  path('edit/<int:todo_id>/', include('edit.urls')),
]
