#3OLIDTS-ErnestoVazquez-03py
#formulario de reistro almacenamiento en txt sin validacion
import tkinter as tk
from tkinter import messagebox

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
def guardar_valores():
    #-----------------obtener valores de los entrys----------------------
    nombres=tbNombre.get()
    apellidos=tbApellidos.get()
    edad=tbEdad.get()
    estatura=tbEstatura.get()
    telefono=tbTelefono.get()
    #--------------------obtener el genero de los radiobuttons--------------------
    genero=""
    if var_genero.get() == 1:
        genero= "Hombre"
    elif var_genero.get() ==2:
        genero="Mujer"
    #-------------------Generar la cadena de caracteres--------------------------
    datos = "Nombres: "+nombres+"\n"+ "Apellidos: "+apellidos+"\n"+"Edad: "+edad+" anos"+"\n"+"Estatura: "+"\n"+"Estatura: "+estatura+"\n"+"Telefono: "+telefono+"\n"+"Genero: "+genero+"\n"
    with open("250904Datos.txt", "a") as archivo:
        archivo.write(datos+"\n\n")
    #-------------------Mostrar mensaje de confirmacion---------------------------
    messagebox.showinfo("informacion", "Datos guardados con exito: \n\n"+datos)
    tbNombre.delete(0, tk.END)
    tbApellidos.delete(0, tk.END)
    tbEdad.delete(0, tk.END)
    tbEstatura.delete(0, tk.END)
    tbTelefono.delete(0, tk.END)
    var_genero.set(0)

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
btnGuardar=tk.Button(ventana, text="Guardar valores", command = guardar_valores)
btnGuardar.pack()
#---------------------------------------Ejecucion de ventana------------------------------
ventana.mainloop()
