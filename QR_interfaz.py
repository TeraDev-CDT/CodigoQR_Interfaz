from tkinter import*
from tkinter import messagebox
import qrcode
from PIL import Image,ImageTk
from resizeimage import resizeimage
from typing import Collection
from pymongo import MongoClient, collection

#Objeto codigo QR
qr = qrcode.QRCode(
	version=1,
	error_correction=qrcode.constants.ERROR_CORRECT_H,
	box_size=10,
	border=4
)

#Conexiones a la base de datos

mongo_conex = 'mongodb://localhost'
mongo_puerto = "27017"
mongo_cadena = mongo_conex+':'+mongo_puerto+'/'



cliente = MongoClient(mongo_conex)
cliente.server_info()
print("Conexion exitosa a la base de datos")

db = cliente['primerbase']
coleccion = db['productos']


class Qr_Generador:
    def __init__(self, root):
        
        self.root = root
        #Dimensiones Interfaz
        self.root.geometry("900x500+200+50")
        #Color Fondo Interfaz
        root.configure(background='#F6F3F1')
        
        #Titulo de la Interfaz Grafica
        self.root.title("Generador QR de Inventario")
        self.root.resizable(False,False)
        
        titulo = Label(self.root,text="Club de Desarrollo Tecnológico UAH",font=("arial",30),bg="#102C54",fg="white").place(x=0,y=0,relwidth=1)
        
        
        #Variables de entrada de los campos
        
        self.var_emp_descripcion = StringVar()
        self.var_marca = StringVar()
        self.var_modelo = StringVar()
        self.var_cantidad = StringVar()
        self.var_serial = StringVar()
        self.var_COD_CDT = StringVar()
        self.var_observacion = StringVar()
        
        
        #Dimensiones de la seccion de los Datos del Producto
        
        emp_seccion = Frame(self.root,bd=2,relief=RIDGE,bg="white")
        emp_seccion.place(x=50,y=90,width=500,height=380)
        
        #Definicion de atributos de las variables de la interfaz
        
        emp_titulo = Label(emp_seccion,text="Datos del Producto",font=("arial",20),bg="#102C54",fg="white").place(x=0,y=0,relwidth=1)
        
        etiqueta_emp_descripcion = Label(emp_seccion,text="DESCRIPCIÓN",font=("arial",10,"bold"),bg="white").place(x=120,y=60)
        etiqueta_emp_marca = Label(emp_seccion,text="MARCA",font=("arial",10,"bold"),bg="white").place(x=165,y=90)
        etiqueta_emp_modelo = Label(emp_seccion,text="MODELO",font=("arial",10,"bold"),bg="white").place(x=160,y=120)
        etiqueta_emp_cantidad = Label(emp_seccion,text="CANTIDAD",font=("arial",10,"bold"),bg="white").place(x=150,y=150)
        etiqueta_emp_serial = Label(emp_seccion,text="SERIAL",font=("arial",10,"bold"),bg="white").place(x=170,y=180)
        etiqueta_emp_COD_CDT = Label(emp_seccion,text="COD_CDT",font=("arial",10,"bold"),bg="white").place(x=155,y=210)
        etiqueta_emp_observaciones = Label(emp_seccion,text="OBSERVACIONES",font=("arial",10,"bold"),bg="white").place(x=102,y=240)
        
        texto_emp_descripcion = Entry(emp_seccion,font=("arial",10,"bold"),textvariable=self.var_emp_descripcion,bg="#E4F4FD").place(x=250,y=60)
        texto_emp_marca = Entry(emp_seccion,font=("arial",10,"bold"),textvariable=self.var_marca,bg="#E4F4FD").place(x=250,y=90)
        texto_emp_modelo = Entry(emp_seccion,font=("arial",10,"bold"),textvariable=self.var_modelo,bg="#E4F4FD").place(x=250,y=120)
        texto_emp_cantidad = Entry(emp_seccion,font=("arial",10,"bold"),textvariable=self.var_cantidad,bg="#E4F4FD").place(x=250,y=150)
        texto_emp_serial = Entry(emp_seccion,font=("arial",10,"bold"),textvariable=self.var_serial,bg="#E4F4FD").place(x=250,y=180)
        texto_emp_COD_CDT = Entry(emp_seccion,font=("arial",10,"bold"),textvariable=self.var_COD_CDT,bg="#E4F4FD").place(x=250,y=210)
        texto_emp_observaciones = Entry(emp_seccion,font=("arial",10,"bold"),textvariable=self.var_observacion,bg="#E4F4FD").place(x=250,y=240)
        
        
        
        boton_registro = Button(emp_seccion,text="Registrar",font=("arial",12,"bold"),command=self.generar,bg="#102C54",fg="white").place(x=61,y=330,width=200,height=30)
        boton_limpiar = Button(emp_seccion,text="Limpiar",command=self.limpiar,font=("arial",12,"bold"),bg="#9B9B9B",fg="white").place(x=310,y=330,width=120,height=30)
        
        #Mensaje Limpio al borrar campos
        
        self.mensaje = ""
        self.etiqueta_mensaje = Label(emp_seccion,text=self.mensaje,font=("arial",20,"bold"),bg="white",fg="#00BB2D")
        self.etiqueta_mensaje.place(x=0,y=280,relwidth=1)
        
        #Dimensiones de la seccion de Codigo QR
        
        qr_seccion = Frame(self.root,bd=2,relief=RIDGE,bg="white")
        qr_seccion.place(x=600,y=90,width=250,height=380)
        
        #Ubicacion ruta de la imagen del logo del club
        
        #imagenlogo=PhotoImage("/home/jesus/Documentos/Programa/Python/Interfaz/logo.png")
        
        #Titulo Codigo QR
        
        emp_titulo = Label(qr_seccion,text="Código QR",font=("arial",20),bg="#102C54",fg="white").place(x=0,y=0,relwidth=1)
        
        #Imagen del Logo de Club arriba de Codigo QR
        
        #qr_logo = Label(qr_seccion,image=imagenlogo).place(x=75,y=50,width=100,height=100)
    
        #Mensaje de Codigo QR Inactivo
        
        self.qr_codigo = Label(qr_seccion,text="Código QR\nInactivo",font=("arial",15),bg="#EEEEEE",fg="#DDDDDD",bd=1,relief=RIDGE)
        self.qr_codigo.place(x=35,y=113,width=180,height=180)
     
     
     #Funcion que indica limpiar y/o borrar los campos de la GUI
     
    def limpiar(self):   
        
        self.var_emp_descripcion.set("")
        self.var_marca.set("")
        self.var_modelo.set("")
        self.var_cantidad.set("")
        self.var_serial.set("")
        self.var_COD_CDT.set("")
        self.var_observacion.set("")
        self.mensaje = ""
        self.etiqueta_mensaje.config(text=self.mensaje)
        self.qr_codigo.config(image="")
        
    #Funcion para generar el codigo QR al registrar datos en los campos
    
    def generar(self):
        
        #Declaracion de variables auxiliares de variables con objetos
        
        c1 = self.var_emp_descripcion.get()
        c2 = self.var_marca.get()
        c3 = self.var_modelo.get()
        c5 = self.var_serial.get()
        
        
        #Definicion de la variable cantidad bajo la condicion del serial
        if c5=="N/T" or c5 =="S/D":
            c4 = self.var_cantidad.get() 
        else:
            c4 = self.var_cantidad.set("1")
            
        c6 = self.var_COD_CDT.get()
        c7 = self.var_observacion.get()
        
        
        
        #Condicion para generar Codigo QR al registrar datos
        if c1=="" or c2== "" or c3== "" or c4 == "" or c5== "" or c6== "" or c7== "":
            self.mensaje = "Complete los campos correctamente!!!"
            self.etiqueta_mensaje.config(text=self.mensaje,fg="red")
        else:
            
            #Definir un documento por el cual seran registrados los datos 
            # que se ingresen en el programa con sus respectivos campos
            
            link = {
                
                "DESCRIPCION": self.var_emp_descripcion.get(),
                "MARCA": self.var_marca.get(),
                "MODELO": self.var_modelo.get(),
                "CANTIDAD": self.var_cantidad.get(),
                "SERIAL": self.var_serial.get(),
                "COD_CDT": self.var_COD_CDT.get(),
                "OBSERVACIONES": self.var_observacion.get()
                
            }
            
            #Agregar datos a la BD Inventario
            coleccion.insert_one(link)
            qr.add_data(link)
            
            #Contador/Iterados de productos del inventario
            contador = coleccion.count_documents({"DESCRIPCION": self.var_emp_descripcion.get()})
            print(self.var_emp_descripcion.get()+" --> "+"{}".format(contador))
            
            #Informacion que va a mostrar el QR
            qr_datos=(f"DESCRIPCIÓN:{self.var_emp_descripcion.get()}\nMARCA:{self.var_marca.get()}\nMODELO:{self.var_modelo.get()}\nCANTIDAD:{self.var_cantidad.get()}\nSERIAL:{self.var_serial.get()}\nCOD_CDT:{self.var_COD_CDT.get()}\nOBSERVACIONES:{self.var_observacion.get()}")
            qr_code=qrcode.make(qr_datos)
            
            #Dimensiones de la imagen de QR que se muestra en el programa
            qr_code=resizeimage.resize_cover(qr_code,[180,180])
            
            #Definir el nombre del formato de imagen del codigo QR con el 
            # identificador codigo que se le asigna al producto registrado
            qr_code.save("./"+self.var_COD_CDT.get()+".png")
            
            #Definir el nombre del codigo QR del producto registrado va a ser guardado
            self.im=ImageTk.PhotoImage(file="./"+str(self.var_COD_CDT.get())+".png")
            
            #Establecer el formato imagen del codigo QR por el objeto instanciado de la imagen
            self.qr_codigo.config(image=self.im)
            
            #Mostrar mensaje de aviso al generar el codigo QR y registro del producto
            self.mensaje = "QR Generado Exitosamente!!!"
            self.etiqueta_mensaje.config(text=self.mensaje,fg="#00BB2D")
            
            
                          
root = Tk()
objeto = Qr_Generador(root)
root.mainloop()



