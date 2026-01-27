from fastapi import FastAPI

app = FastAPI()

@app.get("/dangerous/{lat}/{long}")
def get_dangerous(lat: float, lon: float):
    