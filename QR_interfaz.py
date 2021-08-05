from tkinter import*
import qrcode
from PIL import Image,ImageTk
from resizeimage import resizeimage


class Qr_Generador:
    def __init__(self, root):
        
        self.root = root
        #Dimensiones Interfaz
        self.root.geometry("900x500+200+50")
        #Color Fondo Interfaz
        root.configure(background='#51D1F6')
        
        #Titulo de la Interfaz Grafica
        self.root.title("Generador QR de Inventario")
        self.root.resizable(False,False)
        
        titulo = Label(self.root,text="Club de Desarrollo Tecnológico UAH",font=("arial",30),bg="#102C54",fg="white").place(x=0,y=0,relwidth=1)
        
        
        #Variables de entrada de los campos
        
        self.var_emp_departamento = StringVar()
        self.var_equipo = StringVar()
        self.var_estado = StringVar()
        self.var_marca = StringVar()
        
    
        
        #Dimensiones de la seccion de los Datos del Producto
        
        emp_seccion = Frame(self.root,bd=2,relief=RIDGE,bg="white")
        emp_seccion.place(x=50,y=90,width=500,height=380)
        
        #Definicion de atributos de las variables de la interfaz
        
        emp_titulo = Label(emp_seccion,text="Datos del Producto",font=("arial",20),bg="#102C54",fg="white").place(x=0,y=0,relwidth=1)
        
        etiqueta_emp_departamento = Label(emp_seccion,text="Departamento",font=("arial",15,"bold"),bg="white").place(x=20,y=60)
        etiqueta_emp_equipo = Label(emp_seccion,text="Equipo",font=("arial",15,"bold"),bg="white").place(x=87,y=100)
        etiqueta_emp_estado = Label(emp_seccion,text="Estado",font=("arial",15,"bold"),bg="white").place(x=87,y=140)
        etiqueta_emp_marca = Label(emp_seccion,text="Marca",font=("arial",15,"bold"),bg="white").place(x=94,y=180)
        
        texto_emp_departamento = Entry(emp_seccion,font=("arial",14,"bold"),textvariable=self.var_emp_departamento,bg="#E4F4FD").place(x=200,y=60)
        texto_emp_equipo = Entry(emp_seccion,font=("arial",14,"bold"),textvariable=self.var_equipo,bg="#E4F4FD").place(x=200,y=100)
        texto_emp_estado = Entry(emp_seccion,font=("arial",14,"bold"),textvariable=self.var_estado,bg="#E4F4FD").place(x=200,y=140)
        texto_emp_marca = Entry(emp_seccion,font=("arial",14,"bold"),textvariable=self.var_marca,bg="#E4F4FD").place(x=200,y=180)
        
        boton_registro = Button(emp_seccion,text="Registrar",font=("arial",18,"bold"),command=self.generar,bg="#102C54",fg="white").place(x=61,y=250,width=200,height=30)
        boton_limpiar = Button(emp_seccion,text="Limpiar",command=self.limpiar,font=("arial",18,"bold"),bg="#9B9B9B",fg="white").place(x=310,y=250,width=120,height=30)
        
        #Mensaje Limpio al borrar campos
        
        self.mensaje = ""
        self.etiqueta_mensaje = Label(emp_seccion,text=self.mensaje,font=("arial",20,"bold"),bg="white",fg="#00BB2D")
        self.etiqueta_mensaje.place(x=0,y=320,relwidth=1)
        
        #Dimensiones de la seccion de Codigo QR
        
        qr_seccion = Frame(self.root,bd=2,relief=RIDGE,bg="white")
        qr_seccion.place(x=600,y=90,width=250,height=380)
        
        #Ubicacion ruta de la imagen del logo del club
        
        imagenlogo=PhotoImage("/home/jesus/Documentos/Programa/Python/Interfaz/logo.png")
        
        #Titulo Codigo QR
        
        emp_titulo = Label(qr_seccion,text="Código QR",font=("arial",20),bg="#102C54",fg="white").place(x=0,y=0,relwidth=1)
        
        #Imagen del Logo de Club arriba de Codigo QR
        
        qr_logo = Label(qr_seccion,image=imagenlogo).place(x=75,y=50,width=100,height=100)
    
        #Mensaje de Codigo QR Inactivo
        
        self.qr_codigo = Label(qr_seccion,text="Código QR\nInactivo",font=("arial",15),bg="#EEEEEE",fg="#DDDDDD",bd=1,relief=RIDGE)
        self.qr_codigo.place(x=35,y=165,width=180,height=180)
     
     
     #Funcion que indica limpiar y/o borrar los campos de la GUI
     
    def limpiar(self):   
        
        self.var_emp_departamento.set("")
        self.var_equipo.set("")
        self.var_estado.set("")
        self.var_marca.set("")
        self.mensaje = ""
        self.etiqueta_mensaje.config(text=self.mensaje)
        self.qr_codigo.config(image="")
        
    #Funcion para generar el codigo QR al registrar datos en los campos
    
    def generar(self):
        
        #Declaracion de variables auxiliares de variables con objetos
        
        c1 = self.var_emp_departamento
        c2 = self.var_equipo
        c3 = self.var_estado
        c4 = self.var_marca
        
        #Condicion para generar Codigo QR al registrar datos
        
        if c1.get()=="" or c2.get()=="" or c3.get()=="" or c4.get() == "":
            self.mensaje = "Complete los campos correctamente!!!"
            self.etiqueta_mensaje.config(text=self.mensaje,fg="red")
        else:
            qr_datos=(f"Departamento:{self.var_emp_departamento.get()}\nEquipo:{self.var_equipo.get()}\nEstado:{self.var_estado.get()}\nMarca:{self.var_marca.get()}")
            qr_code=qrcode.make(qr_datos)
            #print(qr_code)
            qr_code=resizeimage.resize_cover(qr_code,[180,180])
            qr_code.save("./"+str(self.var_emp_departamento.get())+".png")
            
            self.im=ImageTk.PhotoImage(file="./"+str(self.var_emp_departamento.get())+".png")
            self.qr_codigo.config(image=self.im)
            self.mensaje = "QR Generado Exitosamente!!!"
            self.etiqueta_mensaje.config(text=self.mensaje,fg="#00BB2D")
            
                          
root = Tk()
objeto = Qr_Generador(root)
root.mainloop()



