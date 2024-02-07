from django.contrib import admin
from django.urls import path
import jobs.views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("amit", jobs.views.amit, name='amit'),
]
