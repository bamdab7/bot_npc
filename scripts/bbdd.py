import pymysql

def inferno(user):
    password = '1Super-Password'
    host = '193.144.42.124'
    port = 33306
    database = 'inferno'
    
    connection = pymysql.connect(
    user=user,
    password=password,
    host=host,
    port=port,
    database=database
    )
    
    cursor = connection.cursor()

    mensaje = ""
    
    query = f"SELECT * FROM admision WHERE nome LIKE '{user}'"
    cursor.execute(query)

    resultado = cursor.fetchall()
    
    if len(resultado) == 0:
        mensaje = "Tienes suerte, no estas en el infierno"
    else:   
        for fila in resultado:
            mensaje +=f"Hola {fila[1]}. Has ido al infierno por {fila[3]}"

    cursor.close()
    connection.close()
    
    return mensaje

