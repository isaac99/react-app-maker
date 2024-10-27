# Set env var OPENAI_API_KEY or load from a .env file:
from openai import OpenAI
import constants
import json
import web_maker.utils.file_utils as file_utils
from web_maker.gpt.main_model import GptService
from web_maker.tree_of_thoughts.tree_of_thoughts import TreeOfThought
import prompts

# from langchain.chains import APIChain
# from langchain.chains.api import open_meteo_docs
# from langchain_openai import OpenAI
# from langchain.chains.openai_functions.openapi import get_openapi_chain

def main():
    prompt = prompts.STEPS_QUERY_PROMPT
    tot = TreeOfThought(root_prompt=prompt, ongoing_prompt_template=prompts.PROMPT_TEMPLATE, max_iterations=15)
    tot.run()
    print("=" * 100)
    print("Final Tree of Thoughts:")
    tot.print_tree(tot.root)

    """

    print("Hello World!")

    

    with open("./website-skeleton/src/index.css", "r") as f:
        content_index = f.read()

    with open("./website-skeleton/src/App.css", "r") as f:
        content_app = f.read()

    print(content_index)
    print(content_app)

    prompt = f"recreate this css with an updated background color scheme to {color}. all colors should be updated to {color}. there are two files so the files should be updated where appropriate:  file1_index: {content_index} file2_app: {content_app} Your response should be in json format like this: {{'file1_index': 'updated content_index', 'file2_app': 'updated content_app'}} also make the logo spin the other way in the correct file. also update the font"

    
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"{prompt}",
            }
        ],
        model="gpt-3.5-turbo",
    )

    file1 = json.loads(chat_completion.choices[0].message.content)["file1_index"]
    file2 = json.loads(chat_completion.choices[0].message.content)["file2_app"]


    with open("./website-skeleton/src/index.css", "w") as f:
        f.write(file1)

    with open("./website-skeleton/src/App.css", "w") as f:
        f.write(file2)


    """



    # new_path = file_utils.copy_directory("./website-skeleton", "./completed-website")
    



    # print("Hello World!")

if __name__ == "__main__":
    main() 