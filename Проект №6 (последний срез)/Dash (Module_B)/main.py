import pandas as pd # Работа с табличными данными
import plotly.graph_objs as go # Создание графиков
from dash import Dash, html, dcc, callback, Output, Input  # Создание веб-дашбордов
import plotly.express as px # Интерактивные графики
import sqlite3 # Работа с БД

# Загрузка базы данных
try:
    con = sqlite3.connect(r"C:\Users\demoexam\Cross_sections_modules\Number_1\clear_data.db")
    df = pd.read_sql("SELECT * FROM Clear_data", con=con)
except Exception as e:
    print(f"Ошибка в загрузке базы данных: {e}")

# Создание графика со связью высоты маршрута частотой шагов
fig = go.Figure()
fig.add_trace(go.Scatter(x=df["point_id"], y=df["elevation"], name="elevation"))
fig.add_trace(go.Scatter(x=df["point_id"], y=df["steps"], name="steps"))

def get_route():
    """
    Возвращает все маршруты в базе данных.
    """

    tracks = []
    numbers_tracks = df["track_id"].unique()
    for number in numbers_tracks:
        tracks.append(f"Маршрут №{number}")
    return tracks

# Создание экземпляра класса Dash()
app = Dash()
# Структура дашборда
app.layout = [
html.H1(children='Аналитический дашборд', style={'textAlign': 'center'}),
html.H2(children='Средняя частота шагов по сезонам', style={'textAlign': 'center'}),
dcc.Dropdown(["Зима", "Весна", "Лето", "Осень"], id="season_selector"),
html.Div(id='season_output'),
html.H2(children='Зависимость температуры от времени суток', style={'textAlign': 'center'}),
dcc.Dropdown(["Утро", "День", "Вечер", "Ночь"], id="time_selector"),
dcc.Graph(id="time_temp_graph"),
html.H2(children="Зависимость высоты и частоты шагов"),
dcc.Graph(id="ele_steps_graph", figure=fig),
html.H2(children='Визуализация маршрутов', style={'textAlign': 'center'}),
dcc.Dropdown(options=get_route() ,id="route_selector"),
dcc.Graph(id="route_map")
]

@callback(Output("season_output", "children"), Input("season_selector", "value"))
def analyze_season(selected_season):
    """
    Анализ данных по выбранному сезону.

    :arg:
        Selected_season (str): Название выбранного сезона
    """

    df_datetime = pd.to_datetime(df["time"])
    if selected_season == "Зима":
        filtered_data = df[df_datetime.dt.month.isin([12, 1, 2])]
    elif selected_season == "Весна":
        filtered_data = df[df_datetime.dt.month.isin([3, 4, 5])]
    elif selected_season == "Лето":
        filtered_data = df[df_datetime.dt.month.isin([6, 7, 8])]
    elif selected_season == "Осень":
        filtered_data = df[df_datetime.dt.month.isin([9, 10, 11])]
    return f"Средние значения: {filtered_data['steps'].mean():.2f}"

@callback(Output("time_temp_graph", "figure"), Input("time_selector", "value"))
def analyze_time_period(selected_period):
    """
    Анализ данных по времени суток.

    :arg:
        selected_period (str): Выбранное время суток
    """

    df_datetime = pd.to_datetime(df["time"])
    if selected_period == "Утро":
        hours = [6, 7, 8, 9, 10, 11, 12]
    elif selected_period == "День":
        hours = [13, 14, 15, 16]
    elif selected_period == "Вечер":
        hours = [17, 18, 19, 20, 21, 22, 23, 24]
    elif selected_period == "Ночь":
        hours = [1, 2, 3, 4, 5]
    filtered_data = df[df_datetime.dt.hour.isin(hours)]
    filtered_data["hour"] = pd.to_datetime(filtered_data["time"]).dt.hour
    hourly_stats = filtered_data.groupby('hour')['temperature'].mean().reset_index()
    return px.line(hourly_stats, x="hour", y="temperature", title=f"Температура - {selected_period}")

@callback(Output("route_map", "figure"), Input("route_selector", "value"))
def track_visualization(track):
    """
    Визуализация маршрутов на интерактивной карте.
    :arg:
        track (str): Выбранный маршрут

    """

    points = {"name": [], "latitude": [], "longitude": []}
    track = int(track.split("№")[1])
    track_data = df[df["track_id"] == track]
    for i in range(len(track_data.index.tolist())):
        row = track_data.iloc[i]
        points["name"].append(f"point №{i}")
        points["latitude"].append(row["latitude"])
        points["longitude"].append(row["longitude"])
    fig = px.line_map(
    points,
    lat='latitude',
    lon='longitude',
    color_discrete_sequence=['red'],
    zoom=10,
    height=600,
    title='Визуализация маршрута',
    text="name"
    )
    return fig


if __name__ == "__main__":
    app.run(debug=True)

