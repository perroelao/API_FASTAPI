from fastapi import APIRouter,HTTPException
from app.database import get_conexion

#variable de las rutas:
router = APIRouter(
    prefix="/usuarios",
    tags=["usuarios"]
)

#endpoints GET, GET1, POST, PUT, DELETE, PATCH
@router.get("/")
def obtener_usuarios():
    try:
        cone = get_conexion()
        cursor = cone.cursor()
        cursor.execute("""SELECT 
                       id_usuario,
                       rut,
                       nombre,
                       apellido_p,
                       apellido_m,
                       snombre,
                       email,
                       fono,
                       direccion,
                       password,
                       rol_id 
                       FROM USUARIO""")
        usuarios = []
        for (id_usuario, rut, nombre, apellido_p, apellido_m, snombre, email, fono, direccion, password, rol_id) in cursor:
            usuarios.append({
            "id_usuario": id_usuario,
            "rut": rut,
            "nombre": nombre,
            "apellido_p": apellido_p,
            "apellido_m": apellido_m,
            "snombre": snombre,
            "email": email,
            "fono": fono,
            "direccion": direccion,
            "password": password,
            "rol_id": rol_id
            })
        cursor.close()
        cone.close()
        return usuarios
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))

@router.get("/{id_buscar}")
def obtener_usuario(id_buscar: int):
    try:
        cone = get_conexion()
        cursor = cone.cursor()
        cursor.execute("""SELECT 
                       id_usuario,
                       rut,
                       nombre,
                       apellido_p,
                       apellido_m,
                       snombre,
                       email,
                       fono,
                       direccion,
                       password,
                       rol_id 
                       FROM USUARIO WHERE id_usuario = :id_usuario""", {"id_usuario": id_buscar})
        usuario = cursor.fetchone()
        cursor.close()
        cone.close()
        if not usuario:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        return {
            "id_usuario": id_buscar,
            "rut": usuario[1],
            "nombre": usuario[2],
            "apellido_p": usuario[3],
            "apellido_m": usuario[4],
            "snombre": usuario[5],
            "email": usuario[6],
            "fono": usuario[7],
            "direccion": usuario[8],
            "password": usuario[9],
            "rol_id": usuario[10]
        }
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))

@router.post("/")
def agregar_usuario(id_usuario:int, rut:str, nombre:str, apellido_p:str, apellido_m:str, snombre:str, email:str, fono:str, direccion:str, password:str, rol_id:int):
    try:
        cone = get_conexion()
        cursor = cone.cursor()
        cursor.execute("""INSERT INTO USUARIO 
                       VALUES 
                       (:id_usuario, 
                       :rut, 
                       :nombre, 
                       :apellido_p, 
                       :apellido_m, 
                       :snombre, 
                       :email, 
                       :fono, 
                       :direccion, 
                       :password, 
                       :rol_id)""",{
                           "id_usuario": id_usuario,
                           "rut": rut,
                           "nombre": nombre,
                           "apellido_p": apellido_p,
                           "apellido_m": apellido_m,
                           "snombre": snombre,
                           "email": email,
                           "fono": fono,
                           "direccion": direccion,
                           "password": password,
                           "rol_id": rol_id,
                       })
        cone.commit()
        cursor.close()
        cone.close()
        return {"mensaje": "Uusuario agregado correctamente"}
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))
    
@router.put("/{id_actualizar}")
def actualizar_usuario():
    try:
        pass
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))
    
@router.delete("/{id_eliminar}")
def eliminar_usuario():
    try:
        pass
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))

@router.patch("/{id_actualizar}")
def actualizar_patch():
    try:
        pass
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))
    
