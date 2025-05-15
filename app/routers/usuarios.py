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

@router.patch("/{id_buscar}")
def obtener_usuario():
    try:
        pass
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))

@router.post("/")
def agregar_usuario():
    try:
        pass
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
    
