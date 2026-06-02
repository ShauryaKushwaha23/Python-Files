# llm.py

from helpers import print_llm_response  # <-- Import the function

favorite_game = "Chess"
favorite_movie = "Inception"
favorite_food = "Pizza"

prompt = f"""
Based on my favorite game, movie, and food, can you recommend a new song for me to listen to?
Game: {favorite_game}
Movie: {favorite_movie}
Food: {favorite_food}
"""

print_llm_response(prompt)  # Call the helper
