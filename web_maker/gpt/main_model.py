from openai import OpenAI
import constants
import json


class GptService():
    def __init__(self, model="gpt-3.5-turbo"):
        self.client = OpenAI(
            # This is the default and can be omitted
            # api_key
        )
        self.model = model
        last_message = None
        last_response = None

    def get_client(self):
        return self.client
    
    def set_model(self, model):
        self.model = model
    
    def query_gpt(self, prompt, role="user", max_tokens=250):
        chat_completion = self.client.chat.completions.create(
            messages=[
                {
                    "role": f"{role}",
                    "content": f"{prompt}",
                }
            ],
            model=self.model,
        )
        return chat_completion.choices[0].message.content