import mysql.connector
import sys

try:
    cone = mysql.connector.connect(
        host="localhost",  # 127.0.0.1
        user="root",
        password="123456",
        database="dbprueba", 
        port="3307"
    )

    cursor = cone.cursor()  ## asi creamos el cursor q es un metodo q interpreta las consultas hechas en python asi una base de datos


    #######################
    # SELECT CON PYTHON
    ######################
    sql = "SELECT idseccion, nombre, descripcion FROM tblseccion"
    cursor.execute(sql)
    result = cursor.fetchall()  ## fetchall para listar
    for value in result:
        print(value[1], value[2])

    #######################
    # INSERT CON PYTHON
    ######################
    # sql = "INSERT INTO tblseccion (nombre, descripcion) VALUES \
    # (%s, %s)"
    # val = ('E', 'Alumnos que no obtuvieron nota' )
    
    # cursor.execute(sql,val)
    # cone.commit()
    # print(cursor)

    #######################
    # INSERT MULTIPLE CON PYTHON
    ######################
    # sql = "INSERT INTO tblseccion (nombre, descripcion) VALUES \
    # (%s, %s)"
    # val = [('F', 'Alumnos que vienen de colegio nacional'), ('G', 'Alumnos que vienen de colegio particular')]

    # cursor.executemany(sql,val)
    # cone.commit()
    # print(cursor)
    #######################
    # UPDATE CON PYTHON
    ######################
    # sql = "UPDATE tblseccion SET \
    #         nombre = %s, descripcion =%s \
    #         WHERE idseccion = %s"
    # val = ('H', 'Alumnos que no se presentaron al examen', '4' )
    
    # cursor.execute(sql,val)
    # cone.commit()

    #######################
    # DELETE CON PYTHON
    ######################

    # sql = "DELETE FROM tblseccion WHERE idseccion = %s"
    # val = ('4',)  # IMPORTANTE poner la coma , despues del valor
    # cursor.execute(sql, val)
    # cone.commit()

except:
    print("No se puede conectar a la base de datos")
    sys.exit()  ## mata todo el proceso de conexion cuando se ha producido error

finally: ## para matar la conexion cuando no se produce error
    if cone.is_connected(): # si estamos conectados
        cursor.close()   # cierro el cursor
        cone.close()    # cierro cone
        print("Conexion finalizada")
