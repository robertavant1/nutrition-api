"""
URL configuration for nutrition_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from api.views import FoodViewSet, SearchFoodAPIView, MyFoodEndpoint
from rest_framework import routers
from django.urls import include, path
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'food', FoodViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),  
    path('search-food/', SearchFoodAPIView.as_view(), name="search_food"),  
    path("my-food/", MyFoodEndpoint.as_view(), name='user_food'),
]
