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
    # sql = "SELECT idpersona, nombre, apellido, tipo_doc, num_docu, direccion, telefono, fec_nacimiento, genero, estado FROM tblpersona"
    # cursor.execute(sql)
    # result = cursor.fetchall()  ## fetchall para listar
    # for value in result:
    #     print(value[1], value[2])

    #######################
    # INSERT CON PYTHON
    ######################
    # sql = "INSERT INTO `dbprueba`.`tblpersona` (`nombre`, `apellido`, `tipo_doc`, `num_docu`, `direccion`, `telefono`, `fec_nacimiento`, `genero`, `estado`) VALUES \
    #     (%s, %s, %s, %s, %s, %s,%s, %s, %s)"
    # val = ('Roberto', 'Torres', '1', '87654331', 'Direccion 11', '987654331', '1995-09-01', 'M', '1' )
    
    # cursor.execute(sql,val)
    # cone.commit()
    # print(cursor)

    #######################
    # INSERT MULTIPLE CON PYTHON
    ######################
    # sql = "INSERT INTO `dbprueba`.`tblpersona` (`nombre`, `apellido`, `tipo_doc`, `num_docu`, `direccion`, `telefono`, `fec_nacimiento`, `genero`, `estado`) VALUES \
    #     (%s, %s, %s, %s, %s, %s,%s, %s, %s)"
    # val = [('Roberto', 'Torres', '1', '87654331', 'Direccion 11', '987654331', '1995-09-01', 'M', '1' ),
    # ('Roberto2', 'Torres2', '1', '87654331', 'Direccion 11', '987654331', '1995-09-01', 'M', '1' )]
    
    # cursor.executemany(sql,val)
    # cone.commit()
    # print(cursor)
    #######################
    # UPDATE CON PYTHON
    ######################
    # sql = "UPDATE tblpersona SET \
    #         nombre = %s, apellido =%s, genero =%s \
    #         WHERE idpersona = %s"
    # val = ('Karen', 'Quispe', 'F', '28' )
    
    # cursor.execute(sql,val)
    # cone.commit()


    #######################
    # DELETE CON PYTHON
    ######################

    # sql = "DELETE FROM tblpersona WHERE idpersona = %s"
    # val = ('29',)
    # cursor.execute(sql, val)
    # cone.commit()

    #######################
    # SELECT PROCEDURE
    ######################

    # cursor.callproc('sp_persona_select')
    # result = cursor.stored_results()
    # print(result)
    # for value in result:
    #     for row in value.fetchall():
    #         print(row[1], row[2])

#   #######################
    # INSERT PROCEDURE
    ########################
    # cursor.callproc('sp_persona_insert', ['Sofia', 'Martinez', '1', '87654334', 'Direccion 14', '987654334', '1995-08-21', 'F', '1'])
    # cone.commit()
    

  
except:
    print("No se puede conectar a la base de datos")
    sys.exit()  ## mata todo el proceso de conexion cuando se ha producido error

finally: ## para matar la conexion cuando no se produce error
    if cone.is_connected(): # si estamos conectados
        cursor.close()   # cierro el cursor
        cone.close()    # cierro cone
        print("Conexion finalizada")


