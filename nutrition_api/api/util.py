import requests
from django.conf import settings

def search_food(query):
    """
    Searches for food items using the Nutritionix API.
    After finding the food, it fetches detailed nutrient data.
    """
    base_url = "https://trackapi.nutritionix.com/v2"
    
    headers = {
        "Content-Type": "application/json",
        "x-app-id": settings.APP_ID,
        "x-app-key": settings.API_KEY
    }

    search_response = requests.get(f"{base_url}/search/instant", headers=headers, params={"query": query})
    if search_response.status_code != 200:
        return {"error": "Failed to fetch food data"}
    
    search_data = search_response.json()
    common_foods = search_data.get("common", [])

    detailed_foods = []
    for food in common_foods:
        food_name = food["food_name"]  
        nutrient_payload = {"query": food_name}
        
        nutrient_response = requests.post(f"{base_url}/natural/nutrients", headers=headers, json=nutrient_payload)
        if nutrient_response.status_code == 200:
            nutrient_data = nutrient_response.json().get("foods", [])[0]  
            food["nf_calories"] = nutrient_data.get("nf_calories", None)
            food["nf_total_fat"] = nutrient_data.get("nf_total_fat", None)
            food["nf_protein"] = nutrient_data.get("nf_protein", None)
            food["nf_total_carbohydrate"] = nutrient_data.get("nf_total_carbohydrate", None)
        
        detailed_foods.append(food)

    return {"common": detailed_foods}

