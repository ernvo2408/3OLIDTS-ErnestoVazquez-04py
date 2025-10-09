#3OLIDTS-ErnestoVazquez-03py
#formulario de reistro almacenamiento en txt sin validacion
import tkinter as tk
from tkinter import messagebox
import re
import mysql.connector

def insertarRegistro(nombres, apellidos, edad, estatura, telefono, genero):
    try:
        conexion = mysql.connector.Connect(
            host = "localhost",  #127.0.0.1
            user = "root",
            password = "",
            database = "programacionavanzada",
            port = "3306"
            )
        cursor = conexion.cursor()

        StringQuery = "INSERT INTO registros (Nombre, Apellidos, Edad, Estatura, Telefono, Genero) VALUES (%s,%s,%s,%s,%s,%s)"
        valores = nombres, apellidos, edad, estatura, telefono, genero
        cursor.execute(StringQuery, valores)
        conexion.commit()
        cursor.close()
        conexion.close()
        messagebox.showinfo("Insercion correcta", "Datos insertados correctamente en la base de datos")
    except mysql.connector.Error as err:
        messagebox.showerror("Error en la conexion de la base de datos", f"Error al insertar datos: {err}")

def guardar_datos():
    # Obtener los datos de los campos
    nombres = tbNombre.get()
    apellidos = tbApellidos.get()
    edad = tbEdad.get()
    estatura = tbEstatura.get()
    telefono = tbTelefono.get()

    # Obtener el género seleccionado
    genero = ""
    if var_genero.get() == 1:
        genero = "Hombre"
    elif var_genero.get() == 2:
        genero = "Mujer"

    # Validar que los campos tengan el formato correcto
    if (es_entero_valido(edad) and es_decimal_valido(estatura) and
        es_entero_valido_de_10_digitos(telefono) and es_texto_valido(nombres)
        and es_texto_valido(apellidos)):

        insertarRegistro(nombres, apellidos, edad, estatura, telefono, genero)
        
        # Crear una cadena con los datos
        datos = ("Nombres: " + nombres + "\n" + "Apellidos: " + apellidos + "\n" + "Edad: " + edad + " años\n"
                 + "Estatura: " + estatura + " cm\n" + "Telefono: " + telefono + "\n" + "Genero: " + genero)
        #datos = f"Nombres: {nombres}\nApellidos: {apellidos}\nEdad: {edad} años\nEstatura: {estatura} cm\nTeléfono: {telefono}\nGénero: {genero}"

        # Guardar los datos en un archivo de texto
        with open("datos01-10-25.txt", "a") as archivo:
            archivo.write(datos + "\n\n")

        # Mostrar un mensaje con los datos capturados
        messagebox.showinfo("Información", "Datos guardados con éxito:\n\n" + datos)

        # Limpiar los controles después de guardar
        limpiar_campos()
    else:
        messagebox.showerror("Error", "Por favor, ingrese datos válidos en los campos.")

#---------------------------definicion de funciones-------------------------------
def limpiar_campos():
    tbNombre.delete(0, tk.END)
    tbApellidos.delete(0, tk.END)
    tbEdad.delete(0, tk.END)
    tbEstatura.delete(0, tk.END)
    tbTelefono.delete(0, tk.END)
    var_genero.set(0)
def borrar_fun():
    limpiar_campos()

def es_entero_valido(valor):
    try:
        int(valor)
        return True
    except ValueError:
        return False

def es_decimal_valido(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False

def es_entero_valido_de_10_digitos(valor):
    return valor.isdigit() and len(valor) == 10

def es_texto_valido(valor):
    return bool(re.match("^[a-zA-Z\s]+$", valor))

#-------------------Creacion de ventanas-----------------------------------
ventana = tk.Tk()
ventana.geometry("520x500")
ventana.title("Formulario Vr.01")
#---------------------Crear variable para el RadioButton---------------------
var_genero = tk.IntVar()
#----------------------Creacion de etiquetas y campos de entrada-----------------
lbNombre=tk.Label(ventana, text= "Nombres: ")
lbNombre.pack()
tbNombre=tk.Entry()
tbNombre.pack()
lbApellidos = tk.Label(ventana, text="Apellidos: ")
lbApellidos.pack()
tbApellidos=tk.Entry()
tbApellidos.pack()
lbTelefono=tk.Label(ventana, text="Telefono: ")
lbTelefono.pack()
tbTelefono=tk.Entry()
tbTelefono.pack()
lbEdad=tk.Label(ventana, text = "Edad: ")
lbEdad.pack()
tbEdad=tk.Entry()
tbEdad.pack()
lbEstatura= tk.Label(ventana, text="Estatura: ")
lbEstatura.pack()
tbEstatura=tk.Entry()
tbEstatura.pack()
lbGenero=tk.Label(ventana, text="Genero: ")
lbGenero.pack()
rbHombre=tk.Radiobutton(ventana, text= "Hombre", variable=var_genero, value=1)
rbHombre.pack()
rbMujer=tk.Radiobutton(ventana, text = "Mujer", variable=var_genero, value=2)
rbMujer.pack()
#--------------------Creacion de botones--------------------------------
btnBorrar= tk.Button(ventana, text="Borrar valores", command = borrar_fun)
btnBorrar.pack()
btnGuardar=tk.Button(ventana, text="Guardar valores", command = guardar_datos)
btnGuardar.pack()
#---------------------------------------Ejecucion de ventana------------------------------
ventana.mainloop()
