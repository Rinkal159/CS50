calories = [
    {"fruit":"apple", "calory": 130},
    {"fruit":"avocado", "calory": 50},
    {"fruit":"banana", "calory": 110},
    {"fruit":"cantaloupe", "calory": 50},
    {"fruit":"grapefruit", "calory": 60},
    {"fruit":"grapes", "calory": 90},
    {"fruit":"honeydew melon", "calory": 50},
    {"fruit":"kiwifruit", "calory": 90},
    {"fruit":"lemon", "calory": 15},
    {"fruit":"lime", "calory": 20},
    {"fruit":"nectarine", "calory": 60},
    {"fruit":"orange", "calory": 80},
    {"fruit":"peach", "calory": 60},
    {"fruit":"pear", "calory": 100},
    {"fruit":"pineapple", "calory": 50},
    {"fruit":"plums", "calory": 70},
    {"fruit":"strawberries", "calory": 50},
    {"fruit":"sweet cherries", "calory": 100},
    {"fruit":"tangerine", "calory": 50},
    {"fruit":"watermelon", "calory": 80},
]

text = input("Item: ")

for calory in calories:
    if text.lower() == calory["fruit"]:
        print(f"Calories: {calory["calory"]}")
        break
