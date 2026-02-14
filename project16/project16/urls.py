"""
URL configuration for project16 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('insert_dept/',insert_dept),
    path('insert_emp/',insert_emp), 
    path('display_Emp/',display_Emp),
    path('display_Dept/',display_Dept),
    path('display_EDJ/',display_EDJ),
    path('display_MEDJ/',display_MEDJ),
    path('display_Lookups/',display_Lookups),
    path('display_EMO/',display_EMO),
    path('display_EDMO/',display_EDMO),
    path('display_DERF/',display_DERF),
]
