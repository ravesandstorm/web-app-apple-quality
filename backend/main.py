from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
import getinfo

app = FastAPI()

# Enable CORS for all origins (you can restrict this to specific domains as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins. Change this to specific domains if needed
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

class AppleInputData(BaseModel):
    size: float
    weight: float
    sweetness: float
    crunchiness: float
    juiciness: float
    ripeness: float
    acidity: float

@app.post("/table1/")
def getTable1(): return getinfo.table1()
@app.post("/table2/")
def getTable2(): return getinfo.table2()
@app.post("/table3/")
def getTable3(): return getinfo.table3()


@app.post("/predict/")
def predict(): return getinfo.getPred()

@app.post("/input/")
def process_input(apple_data: AppleInputData):
    try:
        prediction_result = getinfo.input([
            apple_data.size,
            apple_data.weight,
            apple_data.sweetness,
            apple_data.crunchiness,
            apple_data.juiciness,
            apple_data.ripeness,
            apple_data.acidity
        ])
        return {"prediction": prediction_result}
    except Exception as e:
        print(f"Error in prediction: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")

@app.get("/")
def read_root(): return {"message": "Welcome to the FastAPI application!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)