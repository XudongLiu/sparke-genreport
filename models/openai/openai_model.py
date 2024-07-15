import os

from models.base_model import BaseLLMModel
from openai import OpenAI

from dotenv import load_dotenv
load_dotenv()

class OpenAIModel(BaseLLMModel):
    # implement the abstract methods
    def __init__(self):
        key = os.getenv("OPENAI_API_KEY")
        self.client = OpenAI(api_key=key)
    def process_text(self, text, model="gpt-3.5-turbo",prompt=""):
        response = self.client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": text},
                {"role": "user", "content": prompt},
            ]
        )

        print(response.choices[0].message.content)
        return response.choices[0].message.content
