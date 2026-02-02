from fastapi import FastAPI
import uvicorn
from joblib import dump, load
from datetime import date
from typing import Union
import requests
import pandas as pd
import openmeteo_requests

app = FastAPI()

def row_created(lat: float, lon: float, time: Union[date, None]):
    if time == None:
        time = date.today()
    else:
        time = time
    latitude = lat
    longitude = lon
    elevation = requests.get(f"https://api.open-meteo.com/v1/elevation?latitude={lat}&longitude={lon}").json()["elevation"][0]

    temperature_params = {
        "latitude": lat,
        "longitude": lon,
        "current": ["temperature_2m"],
    }
    openmeteo = openmeteo_requests.Client()
    temperature_responses = openmeteo.weather_api("https://api.open-meteo.com/v1/forecast", params=temperature_params)
    temperature_response = temperature_responses[0]
    current_temperature = temperature_response.Current()
    temperature = current_temperature.Variables(0).Value()


def import_model(target: str):
    try:
        return load(f"C:\\Users\\demoexam\\Desktop\\Гурбанов\\MachineLearning\\Проект №6 (последний срез)\\{target}.joblib")
    except Exception as e:
        return f"Ошибка в загрузке модели: {e}"

@app.get("/dangerous/{lat}/{long}")
def get_dangerous(lat: float, lon: float):
    

    return 0

if __name__ == '__main__':
    print(row_created(51.505713, 104.139225, None))
    uvicorn.run(app, host="127.0.0.1", port=8000)