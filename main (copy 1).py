from fastapi import FastAPI

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