import mysql.connector
import sys

try:
    cone = mysql.connector.connect(
        host="localhost",  # 127.0.0.1
        user="root",
        password="123456",
        database="dbmatricula", 
        port="3307"
    )

    cursor = cone.cursor()

    #######################
    # SELECT TABLA ESTUDIANTE
    ######################
    # sql = "SELECT idEstudiantes, Apellidos, Nombres,  FROM estudiantes"
    # cursor.execute(sql)
    # result = cursor.fetchall() 
    # for value in result:
    #     print(value[1], value[2])

    #######################
    # INSERT TABLA ESTUDIANTE
    ######################
    sql = "INSERT INTO `dbmatricula`.`estudiantes` (Apellidos, Nombres) VALUES \
        (%s, %s,)"
    val = ('Pereira Diaz', 'Christian Manuel')
    
    cursor.execute(sql,val)
    cone.commit()
    print(cursor)


     #######################
    # SELECT TABLA CLASES
    ######################
    # sql = "SELECT idClases, Titulo, Descrpicion,  FROM clases"
    # cursor.execute(sql)
    # result = cursor.fetchall()  ## fetchall para listar
    # for value in result:
    #     print(value[1], value[2])

    #######################
    # INSERT TABLA CLASES
    ######################
    # sql = "INSERT INTO `dbmatricula`.`clases` (Titulo, Descrpicion) VALUES \
    #     (%s, %s,)"
    # val = ('Física', 'Curso de Física')
    
    # cursor.execute(sql,val)
    # cone.commit()
    # print(cursor)


except:
    print("No se puede conectar a la base de datos")
    sys.exit()  

finally: 
    if cone.is_connected(): 
        cursor.close()  
        cone.close()   
        print("Conexion finalizada")