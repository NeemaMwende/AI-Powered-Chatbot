import requests
import openai
import os
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')
# openai.api_key = api_key

# Check if the API key is loaded
# api_key = os.getenv('OPENAI_API_KEY')
# if api_key:
#     print(f"API key loaded successfully: {api_key[:5]}...")  # Print first 5 characters for security
# else:
#     print("Failed to load API key")

def index(request):
    return render(request, 'index.html', {})

@csrf_exempt
def chat(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        if message:
            try:
                # Generate response directly from OpenAI
                openai_response = generate_openai_response(message)
                print("OpenAI Response:", openai_response)
                return JsonResponse(openai_response)
            except Exception as e:
                error_message = f"Failed to generate response from OpenAI: {e}"
                print(error_message)
                return JsonResponse({'error': error_message}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=400)

def generate_openai_response(message):
    try:
        openai_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an AI Assistant called NeemaBot, created by Neema to act as a mental health assistant and help users talk through any issues they are going through especially issues concerning social injustices and discrimination. Any  information regarding Neema they can directly ask her Via +254 792 366 778."},
                {"role": "user", "content": message}
            ],
            max_tokens=150,
            temperature=0.5
        )

        direct_response = openai_response.choices[0].message['content'].strip()
        print("Direct OpenAI Response:", direct_response)

        return {'text': direct_response}
    except Exception as e:
        error_message = f"Failed to generate response from OpenAI: {e}"
        print(error_message)
        return {'error': error_message}
