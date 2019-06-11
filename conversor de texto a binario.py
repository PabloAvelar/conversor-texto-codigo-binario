from tkinter import *
from PIL import Image
from PIL import ImageTk
import webbrowser

#Archivo: conversor de texto a binario.py
# Autor: Pablo Avlear Armenta
# Fecha de creación: 27/05/19
# Fecha de la última modificación: 31/05/19
# Versión de Python: 3.7
#Descripción: Un programa que convierte texto humano a código binario, que también puede convertirlo al revés

__author__ = "Pablo Avelar Armenta"
fondo = "#39B702"
fondo_campo ="#298700"
binario = []
texto_ascii = []
color_twitter = "#55acee"
color_youtube ="#cd201f"
color_twitch = "#6441a5"

def mi_twitter():
	webbrowser.open_new("https://twitter.com/_PabloAvelar")
def mi_twitch():
	webbrowser.open_new("https://twitch.tv/PablitoAvelar")
def mi_youtube():
	webbrowser.open_new("https://youtube.com/c/PabloAvelarYT")


def limpiar():
	campo.delete(1.0, END)

def invertir():
	limpiar()
	texto_binario = 0
	contenido = texto.get()
	separar = [contenido[i:i+8] for i in range(0, len(contenido), 8)]
	#print(separar)

	for elemento in separar:
		if elemento[0] == "1":
			texto_binario+=128

		if elemento[1] == "1":
			texto_binario+=64

		if elemento[2] == "1":
			texto_binario+=32
		if elemento[3] == "1":
			texto_binario+=16
		if elemento[4] == "1":
			texto_binario+=8
		if elemento[5] == "1":
			texto_binario+=4
		if elemento[6] == "1":
			texto_binario+=2
		if elemento[7] == "1":
			texto_binario+=1

		txt_ascii = chr(texto_binario)
		texto_ascii.append(txt_ascii)
		#print(texto_binario, txt_ascii)
		texto_binario = 0

	#print("".join(texto_ascii))
	campo.insert(0.0, "".join(texto_ascii))
	del texto_ascii[:]

def convertir_k(en):
	convertir()

def convertir():
	limpiar()
	contenido = texto.get()

	for letra in contenido:
		codigo_ascii = ord(letra)

		codigo_ascii -= 128
		if codigo_ascii < 0:
			codigo_ascii+=128
			binario.append("0")
		else:
			binario.append("1")

		codigo_ascii -=64
		if codigo_ascii < 0:
			binario.append("0")
			codigo_ascii+=64
		else:
			binario.append("1")

		codigo_ascii -= 32
		if codigo_ascii < 0:
			binario.append("0")
			codigo_ascii+=32
		else:
			binario.append("1")

		codigo_ascii -= 16
		if codigo_ascii < 0:
			binario.append("0")
			codigo_ascii+=16
		else:
			binario.append("1")

		codigo_ascii -= 8
		if codigo_ascii < 0:
			binario.append("0")
			codigo_ascii+=8
		else:
			binario.append("1")

		codigo_ascii -= 4
		if codigo_ascii < 0:
			binario.append("0")
			codigo_ascii+=4
		else:
			binario.append("1")

		codigo_ascii -= 2
		if codigo_ascii < 0:
			binario.append("0")
			codigo_ascii+=2
		else:
			binario.append("1")

		codigo_ascii -= 1
		if codigo_ascii < 0:
			binario.append("0")
			codigo_ascii += 1	
		else:
			binario.append("1")

	campo.insert(0.0, "".join(binario))
	##print("".join(binario))
	del binario[:]

raiz = Tk()

twitch = Image.open("imagenes/twitch.png")
twitter = Image.open("imagenes/twitter.png")
youtube = Image.open("imagenes/youtube.png")

twitch = twitch.resize((35,35), Image.ANTIALIAS)
twitter = twitter.resize((35,35), Image.ANTIALIAS)
youtube = youtube.resize((35,35), Image.ANTIALIAS)

twitter = ImageTk.PhotoImage(twitter)
twitch = ImageTk.PhotoImage(twitch)
youtube = ImageTk.PhotoImage(youtube)

Label(image=twitter, bg=fondo).place(x=230,y=117)
Label(image=twitch, bg=fondo).place(x=73,y=117)
Label(image=youtube, bg=fondo).place(x=370,y=117)

raiz.title("Conversor de texto a binario. Creado por: {}".format(__author__))
raiz.iconbitmap('imagenes/logo.ico')
raiz.geometry("500x500")
raiz.resizable(False, False)
raiz.config(bg=fondo)

Label(raiz, text="MANDA MD A MI TWITTER SI LEES ESTO", bg=fondo, fg=fondo, font=("Arial", 15, "bold")).pack()
Label(raiz, text="CONVERSOR DE TEXTO A CÓDIGO BINARIO", bg="#E20000", fg="#fff", font=("Arial", 15, "bold"), height=2).place(x=35, y=10)

twitter_boton = Button(raiz, text="@_PabloAvelar", bg=color_twitter, fg="#fff", font=("Helvetica", 9, "bold"), command=mi_twitter).pack(pady=50)
twitch_boton = Button(raiz, text="PablitoAvelar", bg=color_twitch, fg="#fff", font=("Helvetica", 9, "bold"), command=mi_twitch).place(x=50, y=80)
youtube_boton = Button(raiz, text="PabloAvelar", bg=color_youtube, fg="#fff", font=("Helvetica", 9, "bold"), command=mi_youtube).place(x=350, y=80)

texto = Entry(raiz)
texto.config(width=80)
texto.pack(pady=20)

boton = Button(raiz, text="Convertir", font=("Arial", 10, "bold"), command=convertir)
boton.config(bg="#A90300", fg="#fff", width=10)
boton.pack(pady=5)

limpiar_boton = Button(raiz, text="Limpiar campo", font=("Arial", 10, "bold"), command=limpiar)
limpiar_boton.config(bg="#E17400", fg="#fff")
limpiar_boton.place(x=363, y=220)

invertir_boton = Button(raiz, text="Invertir", font=("Arial", 10, "bold"), command=invertir)
invertir_boton.config(bg="#10D5DE", fg="#fff", width=10)
invertir_boton.place(x=35, y=220)

scroll = Scrollbar(raiz, orient=VERTICAL)
scroll.pack(side=RIGHT, fill=Y)

campo = Text(raiz, yscrollcommand = scroll.set)
campo.config(width=60, height=15, bg=fondo_campo, fg="#fff")
campo.pack(side=LEFT, fill=BOTH)

scroll.config(command=campo.yview)

texto.bind('<Return>', convertir_k)

raiz.mainloop()