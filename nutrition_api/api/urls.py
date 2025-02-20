from django.urls import include, path
from .views import home, SearchFoodAPIView, MyFoodEndpoint

urlpatterns = [
    path("", home, name="home"),
    path("search-food/", SearchFoodAPIView.as_view(), name='search_food'),
    path("my-food/", MyFoodEndpoint.as_view(), name='user_food'),
]