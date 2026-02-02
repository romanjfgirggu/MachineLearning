# Импорт нужных библиотек
import datetime
import io
import sqlite3
from datetime import date
import requests
import base64, io
from dash import Dash, html, dcc, callback, Output, Input, dash, State
import dash_leaflet as dl
import folium
import gpxpy
import plotly.express as px
import pandas as pd
import tqdm
from joblib import dump, load
from statsmodels.tsa.arima.model import ARIMA
import openmeteo_requests
from datetime import date


# Инициализация Dash-приложения
app = Dash(use_async=True)

year_options = [{"label": str(y), "value": y} for y in range(2027, 2099)]

# Загрузка данные из базы данных
con = sqlite3.connect(r"C:\Users\demoexam\Desktop\Гурбанов\MachineLearning\Проект №6 (последний срез)\clear_data.db")
data = pd.read_sql("SELECT * FROM Clear_data", con)
try:
    # Удаление не нужных в обучении колонок
    data = data.drop(["level_0", "index"], axis=1)
    data = data.drop(["country", "cluster_2", "point_id", "steps"], axis=1)
    # Подготовка колонки со временем, а именно разделение ее на
    # отдельные колонки (date_day, date_month, date_year, date_hour)
    data["time"] = pd.to_datetime(data["time"])
    data['date_day'] = data['time'].dt.day
    data['date_month'] = data['time'].dt.month
    data['date_year'] = data['time'].dt.year
    data['date_hour'] = data['time'].dt.hour
    data = data.drop("time", axis=1)
except Exception as e:
    print(f"Ошибка в оптимизации данных: {e}")

def track_count(df: pd.DataFrame):
    """
    Создает список маршрутов для выпадающего списка.
    Args:
        df (pd.DataFrame): Датасет, в котором содержаться все маршруты
    """

    list_choose = []
    for i in range(len(df["track_id"].unique())):
        list_choose.append(f"Маршрут №{i + 1}")
    return list_choose

def temperature_forecast(row):
    """
    С помощью API запроса получается температуру в определенной точке в определенную дату
    Args:
        row(pd.Series): Колонка со всей информацией
    """

    params = {
        "latitude": row["latitude"],
        "longitude": row["longitude"],
        "start_date": str(
            pd.to_datetime(f"{int(row["date_year"])}-{int(row["date_month"])}-{int(row["date_day"])}").strftime(
                "%Y-%m-%d")),
        "end_date": str(
            pd.to_datetime(f"{int(row["date_year"])}-{int(row["date_month"])}-{int(row["date_day"])}").strftime(
                "%Y-%m-%d")),
        "hourly": ["temperature_2m"]
    }

    try:
        openmeteo = openmeteo_requests.Client()
        responses = openmeteo.weather_api("https://archive-api.open-meteo.com/v1/archive", params=params)
        response = responses[0]
        current = response.Hourly()
        temperatures = current.Variables(0).ValuesAsNumpy()
        return float(temperatures.mean())
    except Exception as e:
        return f"Ошибка получения температуры на точке: {(row["latitude"], row["longitude"])}\n{e}"


def get_predictions(target: str, year: int, track: int):
    """
    Получение предсказание модели, на определенный срок вперед.
    Args:
        target(str): Колонка, которую будет предсказывать модель
        year(date): Дата, в которую будет предсказана опасность
        track(int): Номер трека, по которому будет предсказывание
    """
    sort_data = data[data["track_id"] == track]
    # Для проверки
    sort_data = sort_data[:10]
    if int(date(year, 1, 1).year) > int(date.today().year):
        points_predictions = {}
        period = year - int(date.today().year)
        # Сортировка данных под выбранный маршрут
        # Проверка наличие сохраненной модели, обученной под этот таргет
        try:
            model = load(f"C:\\Users\\demoexam\\Desktop\\Гурбанов\\MachineLearning\\Проект №6 (последний срез)\\{target}.joblib")
        except Exception as e:
            return "Модели, обученной под этот target не было найдено!"
        for i in tqdm.tqdm(range(len(sort_data.index.tolist()))):
            time_column = []
            temperature_column = []
            temperature_range = pd.DataFrame()

            predictions = []
            row = sort_data.iloc[i]
            for k in range(4):
                row["date_year"] -= 1
                time_column.append(str(pd.to_datetime(
                    f"{int(row["date_year"])}-{int(row["date_month"])}-{int(row["date_day"])}").strftime(
                    "%Y-%m-%d")))
                temperature_column.append(temperature_forecast(row))
            temperature_range = pd.concat([temperature_range, pd.Series(temperature_column, name="temperature")],
                                          axis=1)
            temperature_range = pd.concat([temperature_range, pd.Series(time_column, name="time")], axis=1)
            temperature_range["time"] = pd.to_datetime(temperature_range["time"])
            temperature_range = temperature_range.set_index("time")
            temperature_range = temperature_range.iloc[::-1]
            model = ARIMA(temperature_range, order=(1, 1, 1))
            model_fit = model.fit()
            arima_predictions = model_fit.forecast(steps=period).iloc[-1]

            row = sort_data.iloc[i]
            row["date_year"] = year
            row["temperature"] = arima_predictions
            model = load(f"C:\\Users\\demoexam\\Desktop\\Гурбанов\\MachineLearning\\Проект №6 (последний срез)\\{target}.joblib")
            predict = model.predict(pd.DataFrame(row).T.drop([target, "evacuation", "flood", "fire", "cluster", "place_type", "track_id"], axis=1))
            predictions.append(int(predict))
            points_predictions[f"point_{i}"] = predictions
    else:
        ...

    # Создание словаря с точками для их визуализации на карте
    points = {"info": [], "latitude": [], "longitude": [], "danger": []}
    for i in range(len(sort_data.index.tolist())):
        row = sort_data.iloc[i]
        info = []
        info.append(f"Точка №{i}: {points_predictions[f"point_{i}"]}")
        points["info"].append(info)
        points["latitude"].append(row["latitude"])
        points["longitude"].append(row["longitude"])
    for i in points_predictions:
        points["danger"].append(points_predictions[i][0])

    # Создание самой карты и ее визуализация
    fig = px.line_mapbox(
        pd.DataFrame(points),
        lat='latitude',
        lon='longitude',
        color="danger",
        color_discrete_sequence=["green", "yellow", "red"],
        zoom=10,
        height=600,
        title='Визуализация маршрута',
        text="info",
    )
    fig.update_layout(mapbox_style="open-street-map")
    return fig


# Определение макета приложения
app.layout = [
    html.H1(children='Определение уровня опасности точки по координате и дате', style={'textAlign': 'center',
                                                                                       'display': 'block'}),
    html.H2(children='Ниже представлен набор функий, позволяющий предсказывать опасность на маршрутах.'
                     ' Ниже выберите дату и номер маршрута и ждите результата, визуализированного на карте.'
                     'На легенде карты будут видны цифры - уровни опасности. Чем выше, тем опаснее на точке.'),
    html.H3(children='Выберите маршрут из имеющихся:'),
    dcc.Dropdown(track_count(data), id="track_id"),
    html.H3(children='Выберите запланированную дату его прохождения:'),
    dcc.Dropdown(id="track_year", options=year_options, placeholder="Выберите год"),
    dcc.Loading( id="loading-map", type="circle", children=dcc.Graph(id="map"))
]

@app.callback(Output("map", "figure"),
              Input("track_year", "value"),
              Input("track_id", "value"),
              prevent_initial_call=True)
def predictions(d, track_id):
    if d == None or track_id == None:
        return None
    else:
        print(d)
        track_id = int(track_id.split("№")[1]) - 1
        print(track_id)
        return get_predictions(target="dangerous", year=d, track=track_id)

if __name__ == '__main__':
    app.run(debug=True)