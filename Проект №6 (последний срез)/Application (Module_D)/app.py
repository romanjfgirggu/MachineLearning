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
from tqdm import tqdm

# Инициализация Dash-приложения с поддержкой асинхронности
app = Dash(use_async=True)

# Загрузка данные из базы данных
con = sqlite3.connect(r"C:\Users\User\Prfiki\test.db")
df = pd.read_sql("SELECT * FROM clear_data_№2", con)


def track_count(df: pd.DataFrame):
    """
    Создает список маршрутов для выпадающего списка
    """
    list_choose = []
    for i in range(len(df["track_id"].unique())):
        list_choose.append(f"Маршрут №{i + 1}")
    return list_choose


def gpx_parse(gpx_file):
    """
    Парсит GPX-файл и извлекает точки маршрута
    """
    gpx = gpxpy.parse(gpx_file)
    point_list = []
    point_id = 0
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                point_list.append((point.latitude, point.longitude))
                point_id += 1
    return point_list


# Определение макета приложения
app.layout = [
    html.H1(children='Определение уровня опасности точки по координате и дате', style={'textAlign': 'center',
                                                                                       'display': 'block'}),
    dcc.Upload(id='get_gpx_file', children=html.Div(["Drag and Drop или ", html.A("выбери GPX")]), multiple=False),
    dcc.DatePickerSingle(display_format="YYYY.DD.MM", date=date(2023, 10, 15),
                         style={'display': 'block', "alignItems": "center"}, id="input_date"),
    html.Iframe(id="out_api_1", style={"width": "100%", "height": "600px", "border": "none"}),
    html.H1(children='Прогноз пожарной опасности или затоплений на заданный период, оценка сложности эвакуации.',
            style={'textAlign': 'center', 'display': 'block'}),
    dcc.DatePickerRange(display_format="YYYY", style={'display': 'block'},
                        id="input_range_date"),
    dcc.Dropdown(track_count(df), style={'display': 'block'}, id="input_track_id"),
    html.Div(id="loading_bar", style={'white-space': 'pre-line', "font-size": "20px"}),
    html.Iframe(id="out_api_2", style={"width": "100%", "height": "600px", "border": "none"})
]


@app.callback(Output("out_api_1", "srcDoc"),
              Input("get_gpx_file", "contents"),
              State("get_gpx_file", "filename"),
              Input("input_date", "date"),
              prevent_initial_call=True)
def api_1(contents, filename, date):
    """
    Обрабатывает GPX файл и получает прогноз уровня опасности для каждой точки, визуализируя все на карте
    """
    _, content_string = contents.split(",", 1)
    decoded = base64.b64decode(content_string)
    text = decoded.decode("utf-8", errors="replace")
    point_list = gpx_parse(io.StringIO(text))
    points = []
    count = 0
    for i in tqdm(point_list):
        data = {
            "longitude": i[0],
            "latitude": i[1],
            "date": date
        }
        response = requests.post("http://127.0.0.1:8000/predict/danger_level", json=data)
        points.append({"name": f"Точка №{count}", "coords": (i[1], i[0]),
                       f"info": f"Уровень опасности на точке: {response.json()["Danger_Level_Predict"]}"})
        count += 1

    m = folium.Map(location=points[0]["coords"], zoom_start=12)
    folium.PolyLine(
        locations=[p['coords'] for p in points],
        color='blue',
        weight=3,
        opacity=0.7
    ).add_to(m)
    for point in points:
        folium.Marker(
            location=point['coords'],
            popup=f"<b>{point['name']}</b><br>{point['info']}",
            tooltip=point['name'],
            icon=folium.Icon(color='red', icon='info-sign')
        ).add_to(m)
    return m.get_root().render()


@app.callback(Output("out_api_2", "srcDoc"),
              Input("input_range_date", "start_date"),
              Input("input_range_date", "end_date"),
              Input("input_track_id", "value"),
              prevent_initial_call=True,
              running=[Output("loading_bar", "children"), "Загрузка", ""], )
def api_2(start_date, end_date, track_id):
    """
    Обрабатывает GPX файл и получает прогноз сложности эвакуации, пажароопасности и опасности затопления для каждой
    точки на заданный период, визуализируя все на карте
    """
    if start_date is None or end_date is None or track_id is None:
        return dash.no_update
    if datetime.datetime.strptime(end_date, "%Y-%m-%d") - datetime.timedelta(days=365) < datetime.datetime.strptime(
            start_date, "%Y-%m-%d"):
        return "Разница между началом и концом должна быть год или больше"
    track_id = int(track_id[9:])

    data = {
        "start_time": start_date,
        "end_time": end_date,
        "track_id": track_id
    }

    response = requests.post("http://127.0.0.1:8000/predict/track_pred", json=data)
    track_list = df[df["track_id"] == track_id]
    points = []
    for k, v in response.json().items():
        row = track_list.iloc[int(k.split("_")[1])]
        lat = row["latitude"]
        lon = row["longitude"]
        for dangerous in v:
            points.append({'coords': [lat, lon], 'name': f'Точка №{k.split("_")[1]}',
                           'info': f'Изменение пажароопасности: {dangerous["fire_predictions"]}\n'
                                   f'Изменение опасности затопления {dangerous["flooding_predictions"]}\n'
                                   f'Изменение сложности эвакуации: {dangerous["evacuation_predictions"]}'})
    m = folium.Map(location=points[0]["coords"], zoom_start=12)
    folium.PolyLine(
        locations=[p['coords'] for p in points],
        color='blue',
        weight=3,
        opacity=0.7
    ).add_to(m)
    for point in points:
        folium.Marker(
            location=point['coords'],
            popup=f"<b>{point['name']}</b><br>{point['info']}",
            tooltip=point['name'],
            icon=folium.Icon(color='red', icon='info-sign')
        ).add_to(m)
    return m.get_root().render()


if __name__ == '__main__':
    app.run(debug=True)