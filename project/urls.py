"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
# import main_app.views_1 as views_1
import main_app.views as views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),

    # Рассчитать зарплату
    path('api/calculate', views.CalculateView.as_view()),
    # path('api/calculate_dev', views.CalculateView.as_view()),
]

# urlpatterns += [url(r'^', views_1.ReactAppView.as_view())]
