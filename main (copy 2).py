from fastapi import FastAPI

import pandas as pd # untuk bisa import file csv

# create object FastAPI
app = FastAPI()         # INI LANGKAH PERTAMA MEMBUAT API

# endpoint -> get data halaman utama
@app.get("/")           #@ ini decorator #halaman utama pake / pake fungsi get()

#untuk memproses -> buat fungsi #ini fungsi custom namanya bebas spt hancleGetData
def handleGetData():
    # .... ada proses yang berjalan

    return{
        "message" : "hello!"

    }

# endpoint -> get data from csv
@app.get("/data")
def handleCSV():
    # 1. BACA DATA DARI CSV

    # 2. UBAH DATAFRAME -> JSON

    # 3. RETURN JSON