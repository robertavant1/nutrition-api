
from rest_framework import permissions, viewsets
from django.http import JsonResponse
from .util import search_food 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .util import search_food
from .serializers import FoodSerializer, FoodLogSerializer, MacroSerializer
from .models import FoodLog

class FoodViewSet(viewsets.ModelViewSet):
    queryset = FoodLog.objects.all()
    serializer_class = FoodLogSerializer

class SearchFoodAPIView(APIView):
    """
    API endpoint for searching foods using Nutritionix API, now including nutrients.
    Example: /search-food/?query=hamburger
    """
    def get(self, request):
        query = request.GET.get("query", None)
        if not query:
            return Response({"error": "Query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
        data = search_food(query)
        if "error" in data:
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

        serializer = FoodSerializer(data=data["common"], many=True)
        serializer.is_valid()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def add_to_log(request):
        user = request.user
        food_name = request.data.get("food_name")  
        serving_qty = request.data.get("serving_qty")  
        serving_unit = request.data.get("serving_unit")  
        nf_calories = request.data.get("nf_calories", None)
        nf_total_fat = request.data.get("nf_total_fat", None)
        nf_protein = request.data.get("nf_protein", None)
        nf_total_carbohydrate = request.data.get("nf_total_carbohydrate", None)
        food_log = FoodLog.objects.create(
            user=user,
            food_name=food_name,
            calories=nf_calories,
            total_fat = nf_total_fat,
            protein = nf_protein,
            carbs = nf_total_carbohydrate
        )
        return Response(
            {"message": "Food added successfully", "food_name": food_log.food_name},
            status=status.HTTP_201_CREATED
        )

class MyFoodEndpoint(APIView):
    def get(self,request):
        user = request.user
        food_log = FoodLog.objects.filter(user=user)
        serializer = FoodLogSerializer(food_log, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class MacroTotalView(APIView):
    def get(self, request):
        user = request.user
        food_log = FoodLog.objects.filter(user=user)
        serializer = MacroSerializer(food_log, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)