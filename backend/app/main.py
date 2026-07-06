from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


@app.get("/api/route/test")
async def get_test_route():
    return {
        "type": "Feature",
        "properties": {
            "name": "MRT Line 6",
            "color": "#10b981"
        },
        "geometry": {
            "type": "LineString",
            "coordinates": [
                [90.3697, 23.8068], # Mirpur 10
                [90.3732, 23.8005], # Kazipara
                [90.3776, 23.7788], # Agargaon
                [90.3892, 23.7621], # Farmgate
                [90.3952, 23.7421], # Shahbagh
                [90.4172, 23.7261]  # Motijheel
            ]
        }
    }