# Objetivo: Construir una API REST para gestionar usuarios.  

# Requisitos:  
#- GET /users → Listar usuarios.  
#- POST /users → Crear usuario (nombre, email).  
#- DELETE /users/:id → Eliminar usuario.  
#- Validar emails con formato correcto.  
#- Datos guardados en memoria (no BD necesaria).

from fastapi import FastAPI, HTTPException
from routers import users



app = FastAPI()
#Routers
app.include_router(users.router)




@app.get("/")
async def root():
    return "Hola a mi API"

