# Nutrition dataset
foods = [
    {"food": "Apple", "calories": 95, "carbs": 25.0, "protein": 0.5, "fat": 0.3, "vitamin_c": 8.4, "iron": 0.2, "vegan": "Yes", "keto": "No", "gluten_free": "Yes"},
    {"food": "Chicken Breast", "calories": 165, "carbs": 0.0, "protein": 31.0, "fat": 3.6, "vitamin_c": 0.0, "iron": 0.9, "vegan": "No", "keto": "Yes", "gluten_free": "Yes"},
    {"food": "Brown Rice", "calories": 216, "carbs": 45.0, "protein": 5.0, "fat": 1.8, "vitamin_c": 0.0, "iron": 0.8, "vegan": "Yes", "keto": "No", "gluten_free": "Yes"},
    {"food": "Broccoli", "calories": 55, "carbs": 11.0, "protein": 3.7, "fat": 0.6, "vitamin_c": 81.2, "iron": 0.7, "vegan": "Yes", "keto": "Yes", "gluten_free": "Yes"},
    {"food": "Almonds", "calories": 164, "carbs": 6.1, "protein": 6.0, "fat": 14.0, "vitamin_c": 0.0, "iron": 1.1, "vegan": "Yes", "keto": "Yes", "gluten_free": "Yes"}
]

# Function to recommend foods by diet type
def recommend_foods(diet_type):
    diet_type = diet_type.lower()
    key_map = {
        "vegan": "vegan",
        "keto": "keto",
        "gluten-free": "gluten_free"
    }
    key = key_map.get(diet_type)
    if not key:
        return None
    return [food for food in foods if food[key] == "Yes"]

# Nutrition Advisor Chatbot
def nutrition_chatbot():
    print("🍎 Hello! I'm your Nutrition Advisor Bot.")
    
    while True:
        print("\nWhat kind of dietary preference do you follow? (vegan, keto, gluten-free)")
        print("Type 'exit' to quit.")
        user_input = input("> ").strip().lower()
        
        if user_input == "exit":
            print("👋 Goodbye! Stay healthy!")
            break
        
        suggestions = recommend_foods(user_input)
        
        if suggestions:
            print(f"\nHere are some foods suitable for a {user_input} diet:")
            for food in suggestions:
                print(f"- {food['food']} | Calories: {food['calories']}, Protein: {food['protein']}g, Fat: {food['fat']}g")
        else:
            print(f"❌ Sorry, I couldn't find any foods matching the '{user_input}' diet. Try another!")

# Run the bot
if __name__ == "__main__":
    nutrition_chatbot()
s