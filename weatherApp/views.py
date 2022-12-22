from django.shortcuts import render
import requests
import json


# Create your views here.
def index(request):
    data = {}
    if request.method == 'POST':
        city = request.POST['city']
        source = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&appid=bdc3cee5ec5fe024aea027166ec6dbd1')
        if source.status_code == 200:
            list_of_data = source.json()
            data = {
                "country_code": str(list_of_data['sys']['country']),
                "coordinate": str(list_of_data['coord']['lon']) + ', '
                              + str(list_of_data['coord']['lat']),

                "temp": str(list_of_data['main']['temp']) + ' °C',
                "pressure": str(list_of_data['main']['pressure']),
                "humidity": str(list_of_data['main']['humidity']),
                'main': str(list_of_data['weather'][0]['main']),
                'description': str(list_of_data['weather'][0]['description']),
                'icon': list_of_data['weather'][0]['icon'],
            }

        else:
            data = {'error': 'Invalid entry. Please enter another location.'}
    return render(request, "main/index.html", data)

