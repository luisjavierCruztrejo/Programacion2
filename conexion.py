import mysql.connector;

class CConexion():
    def __init__(self):
        pass

    def ConexionBaseDeDatos():
        try:
            conexion = mysql.connector.connect(
                    host='127.0.0.1',
                    port=3306,
                    user='root',
                    database='clientes',
                    auth_plugin='mysql_native_password'
                )
            print("\n¡Conexion exitosa!")
            return conexion;
        except mysql.connector.Error as error:
            print("\n¡ERROR!, No se pudo conectar a la base de datos {}".format(error));

# CConexion.ConexionBaseDeDatos();