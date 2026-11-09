import os
import time

import psycopg2
from flask import Flask, jsonify, request

app = Flask(__name__)

DB_CONFIG = {
    "host": os.environ.get("DB_HOST", "db"),
    "port": os.environ.get("DB_PORT", "5432"),
    "dbname": os.environ["POSTGRES_DB"],
    "user": os.environ["POSTGRES_USER"],
    "password": os.environ["POSTGRES_PASSWORD"],
}


def get_conn(retries=10, delay=2):
    for intento in range(retries):
        try:
            return psycopg2.connect(**DB_CONFIG)
        except psycopg2.OperationalError:
            if intento == retries - 1:
                raise
            time.sleep(delay)


@app.get("/health")
def health():
    return jsonify(status="ok")


@app.post("/clientes")
def crear_cliente():
    data = request.get_json(silent=True) or {}
    identificacion = data.get("identificacion", "").strip()
    nombre = data.get("nombre", "").strip()
    apellidos = data.get("apellidos", "").strip()
    
    if not identificacion or not nombre or not apellidos:
        return jsonify(error="Falta el campos para usar el recurso"), 400
    conn = get_conn()
    try:
        with conn, conn.cursor() as cur:
            cur.execute(
                "INSERT INTO clientes (identificacion, nombre, apellidos) VALUES (%s,%s,%s) RETURNING id", (identificacion, nombre, apellidos)
            )
            nuevo_id = cur.fetchone()[0]
    finally:
        conn.close()
    return jsonify(id=nuevo_id, identificacion=identificacion), 201


@app.get("/clientes")
def listar_clientes():
    conn = get_conn()
    try:
        with conn, conn.cursor() as cur:
            cur.execute("SELECT id, identificacion, nombre, apellidos FROM clientes ORDER BY id")
            filas = cur.fetchall()
    finally:
        conn.close()
    return jsonify(
        [{"id": f[0], "identificacion": f[1], "nombre": f[2], "apellidos": f[3], } for f in filas]
    )
