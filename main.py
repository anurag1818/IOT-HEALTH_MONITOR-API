from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from supabase import create_client, Client

app = FastAPI()

# Supabase configuration
SUPABASE_URL = "https://ixmqccagbxshbwcbdsfn.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Iml4bXFjY2FnYnhzaGJ3Y2Jkc2ZuIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc2MTEzMDMxNSwiZXhwIjoyMDc2NzA2MzE1fQ.ShIfmhCPcUjMjk-m08ej7sRZXL7cEcxan-YLvE7MqBQ"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# ------ Data Models ------
class patientData(BaseModel):
    name: str
    age: int
    sex: str
    blood_group: str
    height: float
    weight: float
    known_conditions: str
    body_temp: float
    
@app.post('/upload-patient-data')
def upload_patient_data(data: patientData):
    try:
        response = supabase.table('patients').insert({
            'name': data.name,
            'age': data.age,
            'sex': data.sex,
            'blood_group': data.blood_group,
            'height': data.height,
            'weight': data.weight,
            'known_conditions': data.known_conditions,
            'body_temp': data.body_temp
        }).execute()
        
        return {"message": "Patient data uploaded successfully", "data": response.data}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

        

