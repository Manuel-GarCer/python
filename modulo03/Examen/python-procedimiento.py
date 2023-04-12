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
    # SELECT PROCEDURE
    ######################

    cursor.callproc('sp_matriculas_select')
    result = cursor.stored_results()
    print(result)
    for value in result:
        for row in value.fetchall():
            print(row[1], row[2])


except:
    print("No se puede conectar a la base de datos")
    sys.exit()  

finally: 
    if cone.is_connected(): 
        cursor.close()  
        cone.close()   
        print("Conexion finalizada")
