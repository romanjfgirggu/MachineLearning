from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/dangerous/{lat}/{long}")
def get_dangerous(lat: float, lon: float):
    

    return 0

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)