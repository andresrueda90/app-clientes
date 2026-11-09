# Clientes: Flask + PostgreSQL con Docker Compose

Dos contenedores:

- **app**: API en Python (Flask + Gunicorn), carpeta `app/`.
- **db**: PostgreSQL 16, carpeta `db/`, con volumen `datos_db`.

La app se conecta a la base de datos usando el **nombre del servicio** (`db`) dentro de la red `red_app`.

## Requisitos
Docker y Docker Compose.

## Cómo levantar
```bash
cp .env.example .env  
docker compose up --build
```

## Probar la comunicación (guardar y leer)
```bash
curl http://localhost:5000/health
curl -X POST http://localhost:5000/clientes -H "Content-Type: application/json" -d '{"identificacion":"1033650666","nombre":"Pedro","apellidos":"Perez"}'
curl http://localhost:5000/clientes
```


