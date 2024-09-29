import requests
import openai
import os
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

openai.api_key = os.getenv('OPENAI_API_KEY')

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
                {"role": "system", "content": "You are an AI Assistant called AggieBot, created by Agnes to  only answer programming questions. Any  information regarding Agnes they can directly ask her Via +254 707 606 316."},
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
