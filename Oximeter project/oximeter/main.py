from fastapi import FastAPI, HTTPException
import csv

app = FastAPI()

# Load data from CSV file
def load_data(file_name: str):
    data = []
    try:
        with open(file_name, mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                data.append({
                    "user_spo2": int(row["user_spo2"]),
                    "user_heart_rate": int(row["user_heart_rate"]),
                    "ppg_waveform": float(row["ppg_waveform"])  # Ensure the column name matches your CSV file
                })
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading CSV file: {str(e)}")
    return data

data = load_data('sample_dataset.csv')

@app.get("/data")
def get_all_data():
    return {"data": data}

@app.get("/data/{index}")
def get_data_by_index(index: int):
    if index < 0 or index >= len(data):
        raise HTTPException(status_code=404, detail="Index out of range")
    return data[index]
