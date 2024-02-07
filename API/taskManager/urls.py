from django.urls import path
from django.contrib import admin
from taskManager.views import Tasks



urlpatterns = [path('Tasks', Tasks)]