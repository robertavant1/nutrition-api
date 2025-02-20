from rest_framework import serializers
from .models import FoodLog

class FoodSerializer(serializers.Serializer):
    food_name = serializers.CharField()
    serving_qty = serializers.FloatField()
    serving_unit = serializers.CharField()
    tag_name = serializers.CharField()
    photo = serializers.JSONField()
    nf_calories = serializers.FloatField(required=False)  
    nf_total_fat = serializers.FloatField(required=False)  
    nf_protein = serializers.FloatField(required=False) 
    nf_total_carbohydrate = serializers.FloatField(required=False) 

class FoodLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodLog
        fields = "__all__"

class MacroSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodLog
        fields = ["nf_calories", "nf_total_fat", 'nf_protein', "nf_total_carbohydrate"]