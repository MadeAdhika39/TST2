from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

data_mahasiswa = {
    18220003: {"Nama": "Made Adhika Wiwardhana"
    }
}

class skema_data_mahasiswa(BaseModel):
    nama    : str

@app.get("/", tags=["Root"])
async def read_root():
    return ("Selamat Datang di API Mahasiswa")

@app.get("/search-nim/{nim}", tags=["Data Mahasiswa"])
async def get_mahasiswa(nim: int):
    if nim in data_mahasiswa:
            return data_mahasiswa[nim]
    return {"Data" : "Gak ada datanya oi"}

@app.post("/add/{nim}", tags=["Data Mahasiswa"])
async def add_data_mahasiswa(nim:int, data_baru:skema_data_mahasiswa):
    if nim in data_mahasiswa:
            return {"Error": "Udah ada datanya oi"}
    
    data_mahasiswa[nim] = {'nama': data_baru.nama}
    return data_mahasiswa[nim]