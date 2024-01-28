import openai 
from config import settings

class ChatGPT:
    openai.api_key = settings.API_KEY

    @classmethod
    def get_answer(cls, question):
        chat_completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", 
            messages=[{"role": "user", "content": question.capitalize()}]
        )
        return chat_completion["choices"][0]["message"]["content"]


