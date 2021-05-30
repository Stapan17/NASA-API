from django.shortcuts import render
import requests
import json

API_KEY = 'h60qxZnn4eIT1c2Hl42ZB3e5sN88RY6k8j8JAcUL'


def home(request):
    URL1 = 'https://api.nasa.gov/planetary/apod?api_key=' + API_KEY

    response = requests.get(URL1)
    jsonData = response.json()
    explanation = jsonData['explanation']
    explanation = explanation[:-80]
    url = jsonData['url']
    title = jsonData['title']

    context = {'explanation': explanation, 'url': url, 'title': title}

    return render(request, 'home.html', context)
