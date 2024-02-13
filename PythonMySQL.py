import tkinter as tk;

# Modulos restantes de tkinter
from tkinter import *;
from tkinter import ttk;
from tkinter import messagebox;
from Clientes import *;
from Conexion import *;

class FormularioClientes():

    global texBoxId;
    texBoxId = None;
    
    global texBoxNombre;
    texBoxNombre = None;

    global texBoxProovedor;
    texBoxProovedor = None;

    global groupBox;
    groupBox = None;

    global tree;
    tree = None;

    global texBoxCantidad;
    texBoxCantidad = None;

    global base;
    base = None;

# Para la interfaz
def FormularioClientes():

    global texBoxId;
    global texBoxNombre;
    global texBoxProovedor;
    global texBoxCantidad;
    global base;
    global groupBox;
    global tree;

    # Manejamos excepciones
    try:
        base = Tk();
        base.geometry("1260x360"); # Tamaño de la ventana
        base.title("Inventario de plaza de la tecnologia"); # Titulo a la ventana
        base.configure(bg="#fff");

        groupBox = LabelFrame(base, text="Datos generales", font=("arial", 14, "bold"), padx=5, pady=5);
        groupBox.grid(row=0, column=0, padx=10, pady=10);
        
        labelId = Label(groupBox, text="Id:", width=13, font=("arial", 12)).grid(row=0, column=0)
        texBoxId = Entry(groupBox);
        texBoxId.grid(row=0, column=1);

        labelNombre = Label(groupBox, text="Nombre:", width=13, font=("arial", 12)).grid(row=1, column=0)
        texBoxNombre = Entry(groupBox);
        texBoxNombre.grid(row=1, column=1);

        labelProovedor = Label(groupBox, text="Proovedor:", width=13, font=("arial", 12)).grid(row=2, column=0)
        texBoxProovedor = Entry(groupBox);
        texBoxProovedor.grid(row=2, column=1);

        labelCantidad = Label(groupBox, text="Cantidad:", width=13, font=("arial", 12)).grid(row=3, column=0)
        texBoxCantidad = Entry(groupBox);
        texBoxCantidad.grid(row=3, column=1);

        Button(groupBox, text="Guardar", width=10, bg="#66FF79", fg="#171717", command=guardarRegistros).grid(row=4, column=0);
        Button(groupBox, text="Modificar", width=10, bg="#66FF79", fg="#171717", command=modificarRegistros).grid(row=4, column=1);
        Button(groupBox, text="Eliminar", width=10, bg="#F62817", fg="#171717", command=eliminarRegistros).grid(row=4, column=2);

        groupBox = LabelFrame(base, text="Lista", font=("arial", 14, "bold"), padx=15, pady=15);
        groupBox.grid(row=0, column=1, padx=15, pady=15);

        # Crear un TreeViews (tabla para mostrar registros)

        # Configurar las columnas
        tree = ttk.Treeview(groupBox,columns=("Id", "Nombre", "Proovedor", "Cantidad"),show='headings', height=5,);
        tree.column("# 1", anchor=CENTER);
        tree.heading("# 1", text="Id");

        tree.column("# 2", anchor=CENTER);
        tree.heading("# 2", text="Nombre");

        tree.column("# 3", anchor=CENTER);
        tree.heading("# 3", text="Proovedor");

        tree.column("# 4", anchor=CENTER);
        tree.heading("# 4", text="Cantidad");

        # AGREGAR LOS DATOS A LA TABLA
        # MOSTRAR LA TABLA

        # Bucle para mostrar los datos
        for row in CClientes.mostrarClientes():
            tree.insert("", "end", values=row);
        

        # Ejecutar la funcion al hacer click y mostrar el resultado en los widgest entry
        tree.bind("<<TreeviewSelect>>", seleccionarRegistro);

        tree.pack();

        base.mainloop() # Para que se pueda cerrar la ventana
    except ValueError as error:
        print("\n¡ERROR!, No se puede mostrar la interfaz: {}".format(error));

def guardarRegistros():

    global texBoxId, texBoxNombre, texBoxProovedor, texBoxCantidad, groupBox;

    try:

        # Verificar si los widgets estan inicializados
        if texBoxNombre is None or texBoxProovedor is None or texBoxCantidad is None:
            print("\n¡ERROR!, Los widgest no estan inicializados")
            return
        
        nombre = texBoxNombre.get();
        proovedor = texBoxProovedor.get();
        cantidad = texBoxCantidad.get();
    
        CClientes.ingresarClientes(nombre, proovedor, cantidad);
        messagebox.showinfo("Informacion", "Los datos fueron guardados");
    
        actualizarTreeView();

        # Limpiamos los campos
        texBoxId.delete(0, END);
        texBoxNombre.delete(0, END);
        texBoxProovedor.delete(0, END);
        texBoxCantidad.delete(0, END);
    except ValueError as error:
        print("\n¡ERROR! el ingresar los datos {}".format(error));

def modificarRegistros():

    global textBoxId, textBoxNombre, textBoxApellido, combo, groupBox;

    try:

        # Verificar si los widgets estan inicializados
        if texBoxId is None or texBoxNombre is None or texBoxProovedor is None or texBoxCantidad is None:
            print("\n¡ERROR!, Los widgest no estan inicializados")
            return
        
        id = texBoxId.get();
        nombre = texBoxNombre.get();
        apellido = texBoxProovedor.get();
        cantidad = texBoxCantidad.get();
    
        CClientes.modificarClientes(id, nombre, apellido, cantidad);
        messagebox.showinfo("Informacion", "Los datos fueron actualizados");
    
        actualizarTreeView();

        # Limpiamos los campos
        texBoxId.delete(0, END);
        texBoxNombre.delete(0, END);
        texBoxProovedor.delete(0, END);
        texBoxCantidad.delete(0, END);
    
    except ValueError as error:
        print("\n¡ERROR! el modificar los datos {}".format(error));

def eliminarRegistros():

    global texBoxId, texBoxNombre, texBoxProovedor, texBoxCantidad, groupBox;

    try:

        # Verificar si los widgets estan inicializados
        if texBoxId is None:
            print("\n¡ERROR!, Los widgest no estan inicializados")
            return
        
        id = texBoxId.get();
    
        CClientes.eliminarClientes(id);
        messagebox.showinfo("Informacion", "Los datos fueron eliminados");
    
        actualizarTreeView();

        # Limpiamos los campos
        texBoxId.delete(0, END);
        texBoxNombre.delete(0, END);
        texBoxProovedor.delete(0, END);
        texBoxCantidad.delete(0, END);
    
    except ValueError as error:
        print("\n¡ERROR! el modificar los datos {}".format(error));

def actualizarTreeView():
    global tree;

    try:
        # Borrar todos los elementos actuales del TreeView
        tree.delete(*tree.get_children());
    
        # Obtener los nuevos datos que deseamos mostrar
        datos = CClientes.mostrarClientes();
    
        # Insertar los nuevos datos en el TreeView
        
        # Bucle para mostrar los datos
        for row in CClientes.mostrarClientes():
            tree.insert("", "end", values=row);
    
    except ValueError as error:
        print("\n¡ERROR! al actualizar tabla {}".format(error))

def seleccionarRegistro(event):
    try:
        
        # Obtener el ID del elemento seleccionado
        itemSeleccionado = tree.focus();
    
        if itemSeleccionado:

            # Obtener los valores por columna
            values = tree.item(itemSeleccionado)['values'];

            # Estableces los valores en los widgets entry
            texBoxId.delete(0, END);
            texBoxId.insert(0, values[0]);
    
            texBoxNombre.delete(0, END);
            texBoxNombre.insert(0, values[1]);
    
            texBoxProovedor.delete(0, END);
            texBoxProovedor.insert(0, values[2])

            texBoxCantidad.delete(0, END);
            texBoxCantidad.insert(0, values[3]);
    except ValueError as error:
        print("\n¡ERROR! al seleccionar registro {}".format(error));

FormularioClientes();