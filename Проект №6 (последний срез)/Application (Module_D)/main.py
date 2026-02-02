from fastapi import FastAPI
import uvicorn
from joblib import dump, load
from datetime import date
from typing import Union
import requests
import pandas as pd
import openmeteo_requests
from geopy.geocoders import Nominatim

app = FastAPI()


def check_features(lat: float, lon: float, radius=500) -> dict[str, int]:
    """
    Возвращает количество объектов в 500 метров вокруг точки.

    Args:
        lat (float): Широта точки
        lon (float): Долгота точки
        radius (int): Радиус вокруг точки, в котором будут браться объекты
    """

    features = {"water": 0, "forest": 0, "buildings": 0}

    max_retries = 3
    retry_count = 0

    query = f"""
    [out:json][timeout:10];
    (
      node(around:{radius},{lat},{lon})["natural"="water"];
      way(around:{radius},{lat},{lon})["natural"="water"];
      node(around:{radius},{lat},{lon})["waterway"];
      way(around:{radius},{lat},{lon})["waterway"];
      node(around:{radius},{lat},{lon})["natural"="wood"];
      way(around:{radius},{lat},{lon})["natural"="wood"];
      node(around:{radius},{lat},{lon})["natural"="forest"];
      way(around:{radius},{lat},{lon})["natural"="forest"];
      node(around:{radius},{lat},{lon})["building"];
      way(around:{radius},{lat},{lon})["building"];
    );
    out center;
    """
    response = requests.get(
        "https://overpass-api.de/api/interpreter",
        params={'data': query},
        timeout=20
    )

    if response.status_code == 200:
        data = response.json()

        # Парсим результаты и считаем по типам
        for element in data.get('elements', []):
            tags = element.get('tags', {})

            # Проверяем тип объекта по тегам
            if tags.get('natural') == 'water' or tags.get('waterway'):
                features['water'] += 1

            elif tags.get('natural') in ('wood', 'forest'):
                features['forest'] += 1

            elif tags.get('building'):
                features['buildings'] += 1
    return features


def row_created(lat: float, lon: float, time: Union[date, None]) -> pd.DataFrame():
    if not time:
        time = date.today()
    else:
        time = time
    try:
        elevation = requests.get(f"https://api.open-meteo.com/v1/elevation?latitude={lat}&longitude={lon}").json()["elevation"][0]
    except Exception as e:
        elevation = 0

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
    features = check_features(lat=lat, lon=lon)

    row = pd.DataFrame({"time": [time], "latitude": [lat], "longitude": [lon], "elevation": [elevation],
                         "temperature": [temperature], "water_feature": [features["water"]],
                         "forest_feature": [features["forest"]], "buildings_feature": [features["buildings"]],
                         "place_type": [max(features.items(), key=lambda x: x[1])[0]]})
    row["time"] = pd.to_datetime(row["time"])
    row['date_day'] = row['time'].dt.day
    row['date_month'] = row['time'].dt.month
    row['date_year'] = row['time'].dt.year
    row['date_hour'] = row['time'].dt.hour
    row = row.drop("time", axis=1)
    return row

def import_model(target: str):
    try:
        return load(f"C:\\Users\\User\\Desktop\\Профики\\MachineLearning\\Проект №6 (последний срез)\\{target}.joblib")
    except Exception as e:
        return f"Ошибка в загрузке модели: {e}"


@app.get("/dangerous/{lat}/{long}")
def get_dangerous(lat: float, lon: float):
    model = import_model("dangerous")
    row = row_created(lat, lon, time=None)
    print(model.predict(row))


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
