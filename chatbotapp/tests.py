import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')

try:
    openai_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            prompt = "Hello World",
            max_tokens=150,
            temperature=0.5
        )
    
    print("Key is valid")
    
except openai.error.APIError as e:
    print(f"invalid key: {e}")