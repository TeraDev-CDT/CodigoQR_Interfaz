
# -> CDT-DEV <- {Rosnier Magallanes}#
from tkinter import *

#Prueba para retener informacion 

def btn_clicked():
    print("Button Clicked")
    depart = path_entry.get()
    equip = equip_entry.get()
    marc = marc_entry.get()
    state = state_entry.get()
    print ("Tu Producto es")
    print(depart + "-" + equip +"-" + marc + "-"+ state)



#-----------------------------------
window = Tk()
window.title("Sistema Inventario")
window.geometry("1000x600")
window.iconbitmap("Icon.ico")
#window.configure(bg = f"#7e24d8")



canvas = Canvas(
    window,
    bg = "#7e24d8", #3D2FDF Azulado moradito
    height = 600,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
#Imagen de Fondo 
canvas.place(x = 0, y = 0)
background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    500, 299,
    image=background_img)





 #Texboxes1---------------------------------------------------
path_entry_img = PhotoImage(file = f"img_textBox0.png")
path_entry_bg = canvas.create_image(
    238.0, 235.0, #Localization IMG X y Y = entra mas unidad, mas baja 
    image = path_entry_img)

path_entry =  Entry(
    bd = 0,
    bg = "#ececec",
    highlightthickness = 0)
path_entry.place(
        x = 138.0, y = 225,
        width = 200.0,
        height = 28)

canvas.create_text(
    238.0, 195.0,
    text = "Departamento",
    fill = "#9e9e9e",
    font = ("Roboto-Light", int(13.0)))

#Texboxes2-----------------------------------------------------
equip_entry_img = PhotoImage(file = f"img_textBox1.png")
equip_entry_bg = canvas.create_image(
    238.0, 315.0, #Localization IMG
    image = equip_entry_img)

equip_entry = Entry(
    bd = 0,
    bg = "#ececec",
    highlightthickness = 0)

equip_entry.place(
    x = 138.0, y = 300.0,  #Localization Text BOX
    width = 200.0,
    height = 28)

canvas.create_text(
    238.0, 275.0, #Localization Text 
    text = "Equipo",
    fill = "#9e9e9e",
    font = ("Roboto-Light", int(13.0)))

#Texboxes3-----------------------------------------------------
marc_entry_img = PhotoImage(file = f"img_textBox1.png")
marc_entry_bg = canvas.create_image(
    238.0, 400.0, #Localization IMG
    image = marc_entry_img)

marc_entry = Entry(
    bd = 0,
    bg = "#ececec",
    highlightthickness = 0)

marc_entry.place(
    x = 138.0, y = 380.0,  #Localization Text BOX
    width = 200.0,
    height = 28)

canvas.create_text(
    238.0, 355.0, #Localization Text 
    text = "Marca",
    fill = "#9e9e9e",
    font = ("Roboto-Light", int(13.0)))
#Texboxes4-----------------------------------------------------
state_entry_img = PhotoImage(file = f"img_textBox1.png")
state_entry_bg = canvas.create_image(
    238.0, 480.0, #Localization IMG
    image = state_entry_img)

state_entry = Entry(
    bd = 0,
    bg = "#ececec",
    highlightthickness = 0)

state_entry.place(
    x = 138.0, y = 465.0,  #Localization Text BOX
    width = 200.0,
    height = 28)

canvas.create_text(
    238.0, 435.0, #Localization Text 
    text = "Estado",
    fill = "#9e9e9e",
    font = ("Roboto-Light", int(13.0)))

#Botones 
img0 = PhotoImage(file = f"img0.png")
b0 = Button(image=img0, borderwidth=0, highlightthickness=0, command=btn_clicked, relief="flat")

b0.place(
    x = 100, y = 510,
    width = 142,
    height = 48)

#Botones 
img1 = PhotoImage(file = f"img2.png")
b1 = Button(image=img1, borderwidth=0, highlightthickness=0, command=btn_clicked, relief="flat")

b1.place(
    x = 250, y = 510,
    width = 142,
    height = 48)

window.resizable(False, False)
window.mainloop()
