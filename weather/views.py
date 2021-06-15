from django.shortcuts import render
import json
import requests

#Create your views here.
def Myapp(request):
    if request.method=='POST':
        city=request.POST['city']
        source='http://api.openweathermap.org/data/2.5/weather?q='+ city + '&units=metric&appid=4cb0327c665c78d7fc28d031b0e9c9c1'
        list_of=requests.get(source)
        list_of_data=list_of.json()
        data={
             "country_code":str(list_of_data['sys']['country']),
             "temp":str(list_of_data['main']['temp'])+ ' °C',
             "pressure":str(list_of_data['main']['pressure']),
             "humidity":str(list_of_data['main']['humidity']),
             "max_temp":str(list_of_data['main']['temp_max'])+ ' °C',
             "min_temp":str(list_of_data['main']['temp_min'])+ ' °C',
             "feel":str(list_of_data['main']['feels_like'])+ ' °C',
             "des":str(list_of_data['weather'][0]['description']),
             "icon":list_of_data['weather'][0]['icon'],
             "city":city
        }
        print(data)
    else:
        data={}
    return render(request,'weather/index.html',data)