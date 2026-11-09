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
# Registro de Clientes: Flask + PostgreSQL con Docker Compose

Aplicación web contenedorizada compuesta por dos servicios que se comunican mediante una red interna de Docker (`red_app`) utilizando resolución DNS por nombre de servicio[cite: 1, 2].

## Arquitectura y Servicios

- **`app` (`clientes_app`)**: API REST desarrollada en Python 3.12 (Flask + Gunicorn) ubicada en `./app/`. Expone el puerto `5000` hacia el host y se conecta a la base de datos apuntando al host `db`[cite: 2].
- **`db` (`clientes_db`)**: Base de datos PostgreSQL 16.4 Alpine ubicada en `./db/`. Utiliza un `healthcheck` (`pg_isready`) para asegurar disponibilidad antes de iniciar la API y persiste los datos mediante el volumen `datos_db`[cite: 2].

## Estructura del Proyecto

```text
├── .github/workflows/ci.yml   # Pipeline de Integración Continua (GitHub Actions)
├── app/                       # Código fuente de la API Flask, requirements.txt y Dockerfile
├── db/                        # Script init.sql de inicialización y Dockerfile de PostgreSQL
├── .dockerignore              # Exclusiones para optimizar la construcción de imágenes
├── .env.example               # Plantilla de variables de entorno requeridas
├── .gitignore                 # Exclusiones del repositorio (incluye el archivo .env)
└── docker-compose.yml         # Orquestación de servicios, red red_app y volumen datos_db
```[cite: 1, 2, 3]


