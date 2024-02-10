import pymysql

import pymysql

def inferno(username):
    
    # Capitalizar la primera letra del nombre de usuario
    username = username.capitalize()
    
    password = '1Super-Password'
    host = '193.144.42.124'
    port = 33306
    database = 'inferno'

    try:
        connection = pymysql.connect(
            user=username,
            password=password,
            host=host,
            port=port,
            database=database
        )
    except pymysql.MySQLError:
        error_message = f"Tienes suerte, no estás en el infierno 🤗"
        return error_message
    
    cursor = connection.cursor()
    mensaje = ""

    try:
        query = f"SELECT * FROM admision WHERE nome LIKE '{username}'"
        cursor.execute(query)

        resultado = cursor.fetchall()

        if len(resultado) == 0:
            mensaje = "Tienes suerte, no estás en el infierno 🤗"
        else:
            for fila in resultado:
                mensaje += f"Hola {fila[1]}.\n Has ido al infierno por {fila[3]} 🔥"
    except pymysql.MySQLError as e:
        error_message = f"Ups... hubo un error en la consulta 💀 :{e}"
        return error_message
    finally:
        cursor.close()
        connection.close()

    return mensaje


