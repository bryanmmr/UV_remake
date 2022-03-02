from django.shortcuts import render
# from secret import *
import os
# Create your views here.
import urllib.request
import json

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + ',PE&units=metric&appid=' + os.getenv('API_KEY') + '&lang=es').read()

        list_of_data = json.loads(source)
        data = {
            "country_code" : str(list_of_data['sys']['country']),
            "lat" : str(list_of_data['coord']['lat']),
            "lng" : str(list_of_data['coord']['lon']),
            "coordinate" : str(list_of_data['coord']['lat']) + str(list_of_data['coord']['lon']),
            "temp"  : str(list_of_data['main']['temp']) + 'C',
            "pressure" : str(list_of_data['main']['pressure']),
            "humidity" : str(list_of_data['main']['humidity']),
            "main"  : str(list_of_data['weather'][0]['main']),
            "description" : str(list_of_data['weather'][0]['description']),
            "icon" : str(list_of_data['weather'][0]['icon']),
            "API_KEY" : str(os.getenv('API_KEY_MAPS')),
        }
        print(data)
    else:
        data = {}

    return render(request, 'main/index.html', data)
