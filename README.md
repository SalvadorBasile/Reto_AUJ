# API REST de Gestión de Usuarios

API REST construida con FastAPI para gestionar usuarios con validación de emails y almacenamiento en memoria.

## 🚀 Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone <tu-repo-url>
cd Reto_AUJ
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3. Ejecutar la aplicación

```bash
uvicorn main:app --reload
```

La API estará disponible en: `http://localhost:8000`

**Documentación interactiva:** `http://localhost:8000/docs`

## 📋 Endpoints disponibles

### GET /users

Lista todos los usuarios registrados.

**Ejemplo con cURL:**

```bash
curl -X GET "http://localhost:8000/users"
```

**Respuesta:**

```json
[
  {
    "id": 1,
    "name": "Salvador",
    "email": "salvador@gmail.com"
  },
  {
    "id": 2,
    "name": "Donatto",
    "email": "donatto@gmail.com"
  },
  {
    "id": 3,
    "name": "Cayetano",
    "email": "cayetano@gmail.com"
  }
]
```

### GET /users/{id}

Obtiene un usuario específico por su ID.

**Ejemplo con cURL:**

```bash
curl -X GET "http://localhost:8000/users/1"
```

### POST /users

Crea un nuevo usuario. Requiere ID, nombre y email.

**Ejemplo con cURL:**

```bash
curl -X POST "http://localhost:8000/users" \
  -H "Content-Type: application/json" \
  -d '{
    "id": 4,
    "name": "Ana García",
    "email": "ana@ejemplo.com"
  }'
```

**Ejemplo con Postman:**

- **Method:** POST
- **URL:** `http://localhost:8000/users`
- **Headers:** `Content-Type: application/json`
- **Body:**

```json
{
  "id": 5,
  "name": "Juan Pérez",
  "email": "juan@ejemplo.com"
}
```

**Respuesta exitosa:**

```json
{
  "id": 4,
  "name": "Ana García",
  "email": "ana@ejemplo.com"
}
```

### PUT /users/{id}

Actualiza un usuario existente.

**Ejemplo con cURL:**

```bash
curl -X PUT "http://localhost:8000/users/1" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Salvador Actualizado",
    "email": "salvador.nuevo@gmail.com"
  }'
```

### DELETE /users/{id}

Elimina un usuario por su ID.

**Ejemplo con cURL:**

```bash
curl -X DELETE "http://localhost:8000/users/1"
```

**Ejemplo con Postman:**

- **Method:** DELETE
- **URL:** `http://localhost:8000/users/1`

**Respuesta exitosa:**

```json
{
  "message": "El usuario ha sido eliminado!"
}
```

## ✨ Características

- ✅ Validación automática de formato de email con Pydantic
- ✅ Prevención de IDs duplicados
- ✅ CRUD completo (Create, Read, Update, Delete)
- ✅ Documentación automática con Swagger UI
- ✅ Manejo de errores HTTP apropiados
- ✅ Almacenamiento en memoria (datos de prueba incluidos)

## 🏗️ Estructura del proyecto

```
Reto_AUJ/
├── main.py              # Aplicación principal FastAPI
├── routers/
│   └── users.py         # Router con endpoints de usuarios
├── requirements.txt     # Dependencias del proyecto
└── README.md           # Esta documentación
```

## 🔧 Modelos de datos

### User

Modelo completo de usuario:

```python
{
  "id": int,
  "name": str,
  "email": EmailStr
}
```

### UserUpdate

Modelo para actualizaciones (sin ID):

```python
{
  "name": str,
  "email": EmailStr
}
```

## 📝 Notas técnicas

- Los datos se almacenan en memoria usando una lista Python
- Se incluyen 3 usuarios de prueba al iniciar la aplicación
- La validación de email utiliza `EmailStr` de Pydantic
- Los endpoints están agrupados bajo el tag "users" en la documentación

## Mejoras futuras

- Persistencia: migrar la lista en memoria a SQLite para mantener datos entre reinicios.
- Tests: agregar pruebas con `pytest` y `fastapi.testclient`.
- Validaciones: evitar emails duplicados al crear usuarios.

## 👨‍💻 Desarrollado por

**Salvador** - Argentina
