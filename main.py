from fastapi import FastAPI, HTTPException


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
    df = pd.read_csv('mock-employees.csv')

    # 2. UBAH DATAFRAME -> JSON
    df = df.to_dict(orient='records')           #parameter orien, dengan value nya recortds, dan ada value lainnya(index,list,dll)

    # 3. RETURN JSON
    return {
        "data" : df
    }

# endpoint -> get data by id (filter)
@app.get("/data/{id}")     #{id} ini paramenter dalam url
def handleFilter(id: int):        #namanya mesti sama parameter, id akan menjadi int
        # 1. baca dat csv
        df = pd.read_csv('mock-employees.csv')

        # 2. filter data col: id
        df = df[ df["id"] == id ]        #ini boolean indexing,ada lagi menggunakan query

# kalo id=100, datanya kosong, tapi tetap muncul status 200
#maka perlu error handling
        # 2.1 error handling : ketika hasil filter = kosong
        # -> tampilkan pesan error
        if df.empty == True:
             raise HTTPException(status_code=404, detail="data tidak ditemukan!")
             #pake raise, untuk respon error di api ,ubah import menjadi (from fastapi import FastAPI, HTTPException)
             #raise fungsi mirip return ato break
        
        # 3. ubah dataframe -> json
        df = df.to_dict(orient="records")

        # 4. return json
        return {"data":df}



#untuk DEPLOY
#  perlu 3 file,package.json,requirements.txt,vercel.json

#BIKI REPO DI github 
# contoh https://github.com/basobox/api-exercise