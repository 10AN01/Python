import os
from dotenv import load_dotenv
import requests
from fastapi import FastAPI
from app.database import save_weather,check_city_exist

from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.responses import FileResponse
router = FastAPI()

load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")

# Point to app/static
router.mount("/static", StaticFiles(directory="app/static"), name="static")

@router.get("/")
def serve_index():
    return FileResponse("app/static/index.html")

@router.get("/weather/{city}")
def get_weather(city:str):
    city = city.lower()
    #Call api
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    cached_weather = check_city_exist(city)
    # If already exists in database
    if cached_weather:
        return {
            "city": cached_weather[0],
            "temperature": cached_weather[1],
            "description": cached_weather[2]
        }
    
    #Converts to Json
    data = response.json()
    
    # Assigns specific data
    temperature = data["main"]["temp"]
    description = data["weather"][0]["description"]
    #Saves data into the database
    save_weather(city,temperature,description)
    return {
        "city": city,
        "temperature": temperature,
        "description": description
    }

    