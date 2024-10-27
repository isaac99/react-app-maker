import os

os.environ.get('OPENAI_API_KEY', '')

color = f"ny giants"
WEB_APP_DESCRIPTION = f"A website for my home renovation and contracting business with a color theme of {color}"
PROMPT = f"recreate this css with an updated background color scheme to {color}. all colors should be updated to {color}. there are two files so the files should be updated where appropriate:  file1_index: App.css file2_app: index.css Your response should be in json format like this: {{'file1_index': 'updated content_index', 'file2_app': 'updated content_app'}} also make the logo spin the other way in the correct file. also update the font"
