
from django.contrib import admin
from django.urls import path
from customer.views import dashboard

urlpatterns = [
    path('admin-portal/', dashboard, name='dashboard'),
    path('admin/', admin.site.urls),
]

