import tkinter as tk
from PIL import ImageTk, Image  
from gif import AnimatedGIF
import os,sys

from tkinter import font as tkFont

############Variables globales
pagina=0
############Variables globales

############Ventana
root= tk.Tk()
root.geometry("800x800")
root.resizable(0,0)
############Ventana

###############Fuente para el titulo
helv = tkFont.Font(family='Ink Free', size=20, weight='bold')
###############Fuente para el titulo

def resource_path(relative_path):     
    try:         # PyInstaller creates a temp folder and stores path in _MEIPASS         
        base_path = getattr(sys, '_MEIPASS', os.getcwd())     
    except Exception:         
        base_path = os.path.abspath(".")      
    return os.path.join(base_path, relative_path)

###########Imagenes
img=Image.open(resource_path("imagenes/caballete.jpg"))
img= img.resize((800,800),Image.ANTIALIAS)
fondoI=ImageTk.PhotoImage(img)  

img=Image.open(resource_path("imagenes/logo.png"))
img= img.resize((800,800),Image.ANTIALIAS)
imagenI=ImageTk.PhotoImage(img)  

img=Image.open(resource_path("imagenes/modelo.png"))
img= img.resize((800,800),Image.ANTIALIAS)
imagenModel=ImageTk.PhotoImage(img) 

img=Image.open(resource_path("imagenes/dominio.png"))
img= img.resize((720,640),Image.ANTIALIAS)
imagenD=ImageTk.PhotoImage(img)

img=Image.open(resource_path("imagenes/mallado.png"))
img= img.resize((720,640),Image.ANTIALIAS)
imagenMalla=ImageTk.PhotoImage(img)

img=Image.open(resource_path("imagenes/contornoconditions.png"))
img= img.resize((720,640),Image.ANTIALIAS)
imagenContorno=ImageTk.PhotoImage(img)

img=Image.open(resource_path("imagenes/conecttable.png"))
img= img.resize((800,800),Image.ANTIALIAS)
tablaC=ImageTk.PhotoImage(img)  

img=Image.open(resource_path("imagenes/paso1.png"))
img= img.resize((800,800),Image.ANTIALIAS)
imagenP1=ImageTk.PhotoImage(img)

img=Image.open(resource_path("imagenes/paso2.png"))
img= img.resize((800,800),Image.ANTIALIAS)
imagenP2=ImageTk.PhotoImage(img)

img=Image.open(resource_path("imagenes/paso3.png"))
img= img.resize((800,800),Image.ANTIALIAS)
imagenP3=ImageTk.PhotoImage(img)

img=Image.open(resource_path("imagenes/paso4.png"))
img= img.resize((800,800),Image.ANTIALIAS)
imagenP4=ImageTk.PhotoImage(img)

img=Image.open(resource_path("imagenes/paso5.png"))
img= img.resize((800,800),Image.ANTIALIAS)
imagenP5=ImageTk.PhotoImage(img)

img=Image.open(resource_path("imagenes/paso6.png"))
img= img.resize((800,800),Image.ANTIALIAS)
imagenP6=ImageTk.PhotoImage(img)

img=Image.open(resource_path("imagenes/matriza.png"))
img= img.resize((800,800),Image.ANTIALIAS)
matriza=ImageTk.PhotoImage(img)

img=Image.open(resource_path("imagenes/matrizk.png"))
img= img.resize((800,800),Image.ANTIALIAS)
matrizk=ImageTk.PhotoImage(img)

img=Image.open(resource_path("imagenes/matrizf.png"))
img= img.resize((800,800),Image.ANTIALIAS)
matrizf=ImageTk.PhotoImage(img)

img=Image.open(resource_path("imagenes/matrizj.png"))
img= img.resize((800,800),Image.ANTIALIAS)
matrizj=ImageTk.PhotoImage(img)

img=Image.open(resource_path("imagenes/matrize.png"))
img= img.resize((800,800),Image.ANTIALIAS)
matrize=ImageTk.PhotoImage(img)

img=Image.open(resource_path("imagenes/matrizg.png"))
img= img.resize((800,800),Image.ANTIALIAS)
matrizg=ImageTk.PhotoImage(img)

img=Image.open(resource_path("imagenes/icono derecha.png"))
img= img.resize((100,100),Image.ANTIALIAS)
boton1I=ImageTk.PhotoImage(img)  

img=Image.open(resource_path("imagenes/icono left.png"))
img= img.resize((100,100),Image.ANTIALIAS)
boton2I=ImageTk.PhotoImage(img)  

img=Image.open(resource_path("imagenes/finish.webp"))
img= img.resize((100,100),Image.ANTIALIAS)
boton3I=ImageTk.PhotoImage(img) 

###########Imagenes




###########Widgets
fondo = tk.Label(root,image=fondoI)
fondo.pack(fill="both")

sig=tk.Button(root,text='Siguiente',command=lambda:cambiarPagina(1),image=boton1I,border=0.5)
ant=tk.Button(root,text='anterior',command=lambda:cambiarPagina(2),image=boton2I,border=0.5)
iniciar=tk.Button(root,text='Iniciar',command=lambda:colocarBotones(),image=boton1I,border=0.5)
finalizar=tk.Button(root,text='Finalizar',command=lambda:root.destroy(),image=boton3I,border=0.5)



labelImagenes = tk.Label(root,borderwidth=4,relief="solid",image=imagenI)
labelImagenes.place(relx=0.05,rely=0.08,relheight=0.63,relwidth=0.9)

labelTitulo = tk.Label(root,borderwidth=4,relief="solid", text="          Bienvenida           ",font=helv)
labelTitulo.place(relx=0.3,rely=0.02,relheight=0.04)
###########Widgets

def setImagen(var,titulo):
    global labelImagenes
    labelImagenes.configure(image=var)
    labelImagenes.image = tablaC
    labelTitulo.configure(text=titulo)
    

def cambiaraBienvenida():
    setImagen(imagenI,"          Bienvenida           ")

def cambiarImagen():
    global pagina
    if(pagina==0):  
        setImagen(imagenI,"          Bienvenida           ")
    elif(pagina==1):  
        setImagen(imagenModel,"             Modelo             ")
    elif(pagina==2):
        setImagen(imagenD,"            Dominio            ")
    elif(pagina==3):
        setImagen(imagenMalla,"             Malla             ")
    elif(pagina==4):
        setImagen(imagenContorno,"Condiciones de Contorno")
    elif(pagina==5):
        setImagen(tablaC,"Tabla de Conectividades")
    elif(pagina==6):
        setImagen(imagenP1,"          Paso 1 MEF          ")
    elif(pagina==7):
        setImagen(imagenP2,"          Paso 2 MEF          ")
    elif(pagina==8):
        setImagen(imagenP3,"          Paso 3 MEF          ")
    elif(pagina==9):
        setImagen(imagenP4,"          Paso 4 MEF          ")
    elif(pagina==10):
        setImagen(imagenP5,"          Paso 5 MEF          ")
    elif(pagina==11):
        setImagen(imagenP6,"          Paso 6 MEF          ")
    elif(pagina==12):
        setImagen(matriza,"          Matriz a          ")
    elif(pagina==13):
        setImagen(matrizk,"          Matriz K          ")
    elif(pagina==14):
        setImagen(matrizf,"          Matriz f          ")
    elif(pagina==15):
        setImagen(matrizj,"          Matriz J          ")
    elif(pagina==16):
        setImagen(matrize,"          Matriz e          ")
    elif(pagina==17):
        setImagen(matrizg,"          Matriz g          ")
    elif(pagina==18):
        setImagen(matrizg,"         Ensamblaje         ")
        gifEnsamblaje=AnimatedGIF(root, resource_path("imagenes/ensamblaje.gif"))
        gifEnsamblaje.place(relx=0.05,rely=0.08,relheight=0.63,relwidth=0.9)

def colocarBotones():
    global iniciar,pagina
    iniciar.place_forget()
    sig.place(relx=0.85,rely=0.9,relheight=0.07,relwidth=0.1)
    ant.place(relx=0.05,rely=0.9,relheight=0.07,relwidth=0.1)
    cambiarPagina(1)
    pagina=1

def desaparecerBoton():
    global ant,sig,finalizar,pagina
    sig.place_forget()
    ant.place_forget()
    if(pagina<=0):
        pagina=0
        iniciar.place(relx=0.85,rely=0.9,relheight=0.07,relwidth=0.1)
    elif(pagina==18):
        finalizar.place(relx=0.85,rely=0.9,relheight=0.07,relwidth=0.1)


def cambiarPagina(opc):
    global pagina
    
    if(opc==1):
        pagina=pagina+1
    if(opc==2):
        pagina=pagina-1
    if(pagina==18 or pagina==0):
        desaparecerBoton()
    cambiarImagen()

iniciar.place(relx=0.85,rely=0.9,relheight=0.07,relwidth=0.1)

root.mainloop()