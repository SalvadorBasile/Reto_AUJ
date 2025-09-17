#Creamos la entidad usuario y todo el CRUD para nuetra API

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, EmailStr

router = APIRouter(prefix='/users',
                   tags=['users'],# Para tenerlos agrupados en la docs de swagger
                   responses={404: {"message": "No encotrado"}})

#Entidad user
class User(BaseModel):
    id: int
    name: str
    email: EmailStr #Validacion de email con pydantic


class UserUpdate(BaseModel):
    name: str
    email: EmailStr #Validacion de email con pydantic

#Simulamos una base de datos con una lista de usuarios
user_list = [User(id= 1, name= 'Salvador', email= 'salvador@gmail.com'),
             User(id= 2, name= 'Donatto', email= 'donatto@gmail.com'),
             User(id= 3, name= 'Cayetano', email= 'cayetano@gmail.com')]


#Funcion para buscar usuario
def user_search(id: int):
    for user in user_list:
        if user.id == id:
            return user
    return None


#Traemos todos los usuarios
@router.get('/')
async def users():
    return user_list 


#Traemos un usuario por su id (Path)
@router.get('/{id}')
async def user(id: int):
    found_user = user_search(id)
    if not found_user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado!")
    return found_user

#Agregamos un usuario nuevo
@router.post('/')
async def add_user(new_user: User):

    found_user = user_search(new_user.id)

    if found_user:
        #Si el usuario existe, lanzamos un error
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"El usuario con ID {new_user.id} ya existe!")
    
    #Si no existe, lo agregamos a la lista
    user_list.append(new_user)

    return new_user  #Mostramos el usuario agregado
 

#Update de un usuario existente
@router.put('/{id}')
async def update_user(id: int, update_user: UserUpdate):
    for index, user in enumerate(user_list):
        if user.id == id:
            #Actualizamos el usuario
            user_list[index] = User(
                id=id,
                name=update_user.name,
                email=update_user.email
            )
            return user_list[index] #Mostramos el user updateado
        
    raise HTTPException(status_code=404, detail="Usuario no encontrado!")


#Delete de un usuario
@router.delete('/{id}')
async def delete_user(id: int):
    for index, user in enumerate(user_list):
        if user.id == id:
            del user_list[index]
            return {"message": "El usuario ha sido eliminado!"}
        
    raise HTTPException(status_code=404, detail="El usuario no se ha encontrado!")