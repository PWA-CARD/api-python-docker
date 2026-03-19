from fastapi import FastAPI
import mysql.connector

app = FastAPI()

def conectar_db():
        return mysql.connector.connect(
               host="db",
               user="appuser",
               password="apppass",
               database="testdb"
        )

@app.get("/")
def hello():
  return {"mensaje":"Hello World!"}

@app.get("/db")
def test_db():
    try:
        conn = conectar_db()
        cursor = conn.cursor()
        cursor.execute("SELECT 1")
        resultado = cursor.fetchone()
        conn.close()
        return {"db": resultado[0]}
    except Exception as e:
        return {"error": str(e)}
