from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
  return {'message': "¡Hola FastAPI!" }

@app.get("/url")
async def url():
  return {"url": "https://arisdev.com/python"}

# Inicia  el servidor en localhost:8000
# Detener el servidor: Ctrl+C

# Documentación con Swagger: http://127.0.0.1:8000/docs
# Documentación con Swagger: http://127.0.0.1:8000/redoc
