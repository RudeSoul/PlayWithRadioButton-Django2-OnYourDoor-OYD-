from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('view/', views.homepage, name="home"),
    path('sentvalue/', views.sentvalue, name="sentvalue")
]
