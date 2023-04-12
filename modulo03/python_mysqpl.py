import mysql.connector
import sys

try:
    cone = mysql.connector.connect(
        host="localhost", # 127.0.0.1 - 192.168.0.100
        user="root",
        password="123456",
        database="dbprueba",
        port="3306"
    )

    cursor = cone.cursor()
    ########################
    # SELECT CON PYTHON
    ########################
    # sql = "SELECT idpersona, nombre, apellido, tipo_doc, num_docu, direccion, telefono, fec_nacimiento, genero, estado \
    #         FROM tblpersona"
    # cursor.execute(sql)
    # result = cursor.fetchall()
    # for row in result:
    #     print(row[1], row[2])

    ########################
    # INSERT CON PYTHON
    ########################
    # sql = "INSERT INTO tblpersona \
    #         (nombre, apellido, tipo_doc, num_docu, direccion, telefono, fec_nacimiento, genero, estado) \
    #         VALUES \
    #         (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    # val = ('Roberto', 'Torres', '1', '87654331', 'Direccion 11', '987654331', '1995-09-01', 'M', '1')
    # cursor.execute(sql, val)
    # cone.commit()

    #############################
    # INSERT MULTIPLE CON PYTHON
    #############################
    # sql = "INSERT INTO tblpersona \
    #         (nombre, apellido, tipo_doc, num_docu, direccion, telefono, fec_nacimiento, genero, estado) \
    #         VALUES \
    #         (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    # val = [('Roberto2', 'Torres2', '1', '87654331', 'Direccion 11', '987654331', '1995-09-01', 'M', '1'),
    #        ('Roberto3', 'Torres3', '1', '87654331', 'Direccion 11', '987654331', '1995-09-01', 'M', '1')]
    # cursor.executemany(sql, val)
    # cone.commit()

    ########################
    # UPDATE CON PYTHON
    ########################
    # sql = "UPDATE tblpersona SET \
    #         nombre = %s, apellido = %s, genero = %s \
    #         WHERE idpersona = %s"
    # val = ('Karen', 'Quispe', 'F', '16')
    # cursor.execute(sql, val)
    # cone.commit()

    ########################
    # DELETE CON PYTHON
    ########################
    # sql = "DELETE FROM tblpersona WHERE idpersona = %s"
    # val = ('16',)
    # cursor.execute(sql, val)
    # cone.commit()

    ########################
    # SELECT PROCEDURE
    ########################
    # cursor.callproc('sp_persona_select')
    # result = cursor.stored_results()
    # for value in result:
    #     for row in value.fetchall():
    #         print(row[1], row[2])

    ########################
    # INSERT PROCEDURE
    ########################
    cursor.callproc('sp_persona_insert', ['Sofia', 'Martinez', '1', '87654334', 'Direccion 14', '987654334', '1995-08-21', 'F', '1'])
    cone.commit()

except:
    print("No se puede conectar a la base de datos")
    sys.exit()
finally:
    if cone.is_connected():
        cursor.close()
        cone.close()
        print("Conexión finalizada.")



# Script de todo lo aprendido en python y MySQL para la tabla tblSeccion.
# Fecha ultima entrega: 04-04-2023
# ASUNTO: [Python03-042023] - APELLIDOS Y NOMBRES
# Nombre Archivo: APELLIDOS_NOMBRES.py