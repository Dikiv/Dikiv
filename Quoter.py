# file: update_readme.py
import json
import random

# Define the paths to the .md and JSON files
md_file_path = "./README.md"
json_file_path = "assets/quotes.json"

# Read the content of the .md file
with open(md_file_path, 'r') as md_file:
    md_content = md_file.read()

# Load quotes from the JSON file
with open(json_file_path, 'r') as json_file:
    quotes = json.load(json_file)

# Select a random quote
selected_quote = random.choice(quotes)
author = selected_quote['author']
quote = selected_quote['quote']

# Replace placeholders with dynamic values
md_content = md_content.replace("{{author}}", author).replace("{{quote}}", quote)

# Write the updated content back to the .md file
with open(md_file_path, 'w') as md_file:
    md_file.write(md_content)

