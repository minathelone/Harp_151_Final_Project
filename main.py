'''
Sample Spoonacular API call. I recommend everyone makes their own separate spoonacular account and their own key
since Spoonacular sets a daily call limit-Will
'''
import requests
import json

key = 'e145281d4e034704b95167d50dbb4081'
url = f'https://api.spoonacular.com/recipes/findByIngredients?apiKey={key}&ingredients=apples,+flour,+sugar&number=2'

recipe = requests.get(url)
json_file = recipe.json()
print(json.dumps(json_file, indent=4))
