from Conexion import *;

class CClientes():

    def ingresarClientes(nombre, proovedor, cantidad):

        try:
            conexion = CConexion.ConexionBaseDeDatos();
            cursor = conexion.cursor();
            sql = "INSERT INTO productos VALUES(null, %s, %s, %s);";

            # La variable valores '%' tiene que ser una TUPLA
            # Como minima expresion es: (valor, ), la coma hace que sea una tupla
            # LAS TUPLAS SON LISTAS INMUTABLES, eso quiere decir que no se pueden modificar

            valores = (nombre, proovedor, cantidad);
            cursor.execute(sql, valores);
            conexion.commit()
            print(cursor.rowcount, "!Registro realizado con exito¡");
            conexion.close()

        except mysql.connector.Error as error:
            print("\n¡ERROR! al conectarse a la base de datos {}".format(error));
    

    def modificarClientes(id, nombre, proovedor, cantidad):

        try:
            conexion = CConexion.ConexionBaseDeDatos();
            cursor = conexion.cursor();
            sql = "UPDATE productos SET productos.nombre = %s, productos.proovedor = %s, productos.cantidad = %s WHERE productos.id = %s;";

            valores = (nombre, proovedor, cantidad, id);
            cursor.execute(sql, valores);
            conexion.commit()
            print(cursor.rowcount, "!Registro actualizado con exito¡");
            conexion.close()

        except mysql.connector.Error as error:
            print("\n¡ERROR! al actualizar la base de datos {}".format(error));
    
    def eliminarClientes(id):

        try:
            conexion = CConexion.ConexionBaseDeDatos();
            cursor = conexion.cursor();
            sql = "DELETE FROM productos WHERE productos.id = %s;";

            valores = (id, );
            cursor.execute(sql, valores);
            conexion.commit()
            print(cursor.rowcount, "!Registro eliminado con exito¡");
            conexion.close()

        except mysql.connector.Error as error:
            print("\n¡ERROR! al eliminar registro de la base de datos {}".format(error));

    def mostrarClientes():
        try:
            conexion = CConexion.ConexionBaseDeDatos();
            cursor = conexion.cursor();
            cursor.execute("SELECT * FROM productos;");
            miResultado = cursor.fetchall()
            conexion.commit()
            conexion.close()
            return miResultado;
        except mysql.connector.Error as error:
            print("\n¡ERROR! no se pudieron mostrar los datos {}".format(error));
            