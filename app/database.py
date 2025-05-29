import oracledb

def get_conexion():
    conexion = oracledb.connect(
        user="FERREMAS",
        password="FERREMAS",
        dsn="localhost:1521/orcl"
    )
    return conexion