import requests
from django.shortcuts import render
from decouple import config


# Create your views here.

def home(request):

    weather_data = None

    if request.method == 'POST':
        city = request.POST.get('city')

        api_key = config('OPENWEATHER_API_KEY')
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

        # Fetching API data
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()

            # Extracting usefull data
            weather_data = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'icon': f"http://openweathermap.org/img/wn/{data['weather'][0]['icon']}@2x.png",
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed'],
            }
        else:
            weather_data = {
                'error': "Sorry, we couldn't find the city you entered. Please try again with another city."}

    return render(request, 'home.html', {'weather_data': weather_data})
