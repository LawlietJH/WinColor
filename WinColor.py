# -*- coding: utf-8 -*-
#
#
#
#    ██╗    ██╗██╗███╗   ██╗ ██████╗ ██████╗ ██╗      ██████╗ ██████╗ 
#    ██║    ██║██║████╗  ██║██╔════╝██╔═══██╗██║     ██╔═══██╗██╔══██╗
#    ██║ █╗ ██║██║██╔██╗ ██║██║     ██║   ██║██║     ██║   ██║██████╔╝
#    ██║███╗██║██║██║╚██╗██║██║     ██║   ██║██║     ██║   ██║██╔══██╗
#    ╚███╔███╔╝██║██║ ╚████║╚██████╗╚██████╔╝███████╗╚██████╔╝██║  ██║
#     ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═╝
#                                                                     
#                                                         By: LawlietJH
#                                                                 1.1.0

import ctypes
import time
import sys
import os


BWC = r"""
                      ╦ ╦  ┬  ┌┐┌   ╔═╗ ┌─┐ ┬   ┌─┐ ┬─┐
                      ║║║  │  │││   ║   │ │ │   │ │ ├┬┘
                      ╚╩╝  ┴  ┘└┘   ╚═╝ └─┘ ┴─┘ └─┘ ┴└─
"""
#~ Fuente: Calvin S, Página: http://patorjk.com/software/taag

BA = r"""
                           ╦  ┌─┐┬ ┬┬  ┬┌─┐┌┬┐ ╦╦ ╦
                           ║  ├─┤││││  │├┤  │  ║╠═╣
                           ╩═╝┴ ┴└┴┘┴─┘┴└─┘ ┴ ╚╝╩ ╩
"""
#~ Fuente: Calvin S, Página: http://patorjk.com/software/taag


def Dat():
	
	Nombre = BWC
	Autor = BA
	Version = "\n\n\n{:^80}".format("1.1.0")
	
	return os.system("cls"), winsize(80,22),\
	       color("VC"), print("\n\n", BWC), time.sleep(0.1),\
	       color("AZC"), print("\n\n", Autor), time.sleep(0.1),\
	       color("RC"), print(Version), rest(),\
	       os.system("Pause>Nul"), exit(0)

#________________________________________________________________________
#________________________________________________________________________

#~ Constantes de la API de Windows.
STD_OUTPUT_HANDLE = -11

#_______________ Colores _______________

x0   = 0x0000   # Color Negro.
x1   = 0x0001   # Color Azul.
x2   = 0x0002   # Color Verde.
x3   = 0x0003   # Color Aguamarina.
x4   = 0x0004   # Color Rojo.
x5   = 0x0005   # Color Púrpura.
x6   = 0x0006   # Color Amarillo.
x7   = 0x0007   # Color Blanco.
x8   = 0x0008   # Color Gris.
x9   = 0x0009   # Color Azul Claro.
xA   = 0x000A   # Color Verde Claro.
xB   = 0x000B   # Color Aguamarina Claro.
xC   = 0x000C   # Color Rojo Claro.
xD   = 0x000D   # Color Púrpura Claro.
xE   = 0x000E   # Color Amarillo Claro.
xF   = 0x000F   # Color Blanco Brillante.
#~ _______________________________________


#~ Función que reinicia al color original
def get_csbi_attributes(handle):
    #~ Basado en winconsole.py de IPython
    
    import struct
    
    csbi = ctypes.create_string_buffer(22)
    res = ctypes.windll.kernel32.GetConsoleScreenBufferInfo(handle, csbi)
    assert res

    (bufx, bufy, curx, cury, wattr, left, top, right, bottom, maxx, maxy) = struct.unpack("hhhhHhhhhhh", csbi.raw)
    return wattr


#~ Función Que Indica En Donde Iniciará El Color.
def color(ColorLetra):
	
	flush()
	
	if ColorLetra == "x0" or ColorLetra == "negro" or ColorLetra == "N" :
		Color = x0
	elif ColorLetra == "x1" or ColorLetra == "azul" or ColorLetra == "AZ" :
		Color = x1
	elif ColorLetra == "x2" or ColorLetra == "verde" or ColorLetra == "V" :
		Color = x2
	elif ColorLetra == "x3" or ColorLetra == "aguamarina" or ColorLetra == "AG" :
		Color = x3
	elif ColorLetra == "x4" or ColorLetra == "rojo" or ColorLetra == "R" :
		Color = x4
	elif ColorLetra == "x5" or ColorLetra == "purpura" or ColorLetra == "P" :
		Color = x5
	elif ColorLetra == "x6" or ColorLetra == "amarillo" or ColorLetra == "AM" :
		Color = x6
	elif ColorLetra == "x7" or ColorLetra == "blanco" or ColorLetra == "B" :
		Color = x7
	elif ColorLetra == "x8" or ColorLetra == "gris" or ColorLetra == "G" :
		Color = x8
	elif ColorLetra == "x9" or ColorLetra == "azul cl" or ColorLetra == "AZC" :
		Color = x9
	elif ColorLetra == "xA" or ColorLetra == "verde cl" or ColorLetra == "VC" :
		Color = xA
	elif ColorLetra == "xB" or ColorLetra == "aguamarina cl" or ColorLetra == "AGC" :
		Color = xB
	elif ColorLetra == "xC" or ColorLetra == "rojo cl" or ColorLetra == "RC" :
		Color = xC
	elif ColorLetra == "xD" or ColorLetra == "purpura cl" or ColorLetra == "PC" :
		Color = xD
	elif ColorLetra == "xE" or ColorLetra == "amarillo cl" or ColorLetra == "AMC" :
		Color = xE
	elif ColorLetra == "xF" or ColorLetra == "blanco br" or ColorLetra == "BB" :
		Color = xF
	else:
		Color = reset

	colorI = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, Color)
	
	return ""



#~ Función Que Indica En Donde Terminará El Color.
def rest():
	
	flush()
	
	reinicar = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, reset)
	
	return reinicar



#~ Variables que simplifican el nombre.
handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
reset = get_csbi_attributes(handle)



#~ Función que sirve para poder poner colores en la misma linea
def flush():
	return sys.stdout.flush()


	
#~ Función para mostrar recuadro [+], [-], [!], [¡], [*], [~], [#], [&], [ ] con colores
def Mark(Simbolo = " ", Color2 = None, Color1 = None):
	
	if (Simbolo == "+") or (Simbolo == ">+"):
		
		if(Simbolo[0] == ">"):
			color("BB"), print(" ===> ", end="")
		
		if Color1 != None and Color2 != None:
			return color(Color1), print("[", end=""), color(Color2), print(Simbolo[-1], end=""), color(Color1), print("]", end="")
		elif Color1 != None and Color2 == None:
			return color(Color1), print("[", end=""), color("VC"), print(Simbolo[-1], end=""), color(Color1), print("]", end="")
		elif Color1 == None and Color2 != None:
			return color("BB"), print("[", end=""), color(Color2), print(Simbolo[-1], end=""), color("BB"), print("]", end="")
		elif Color1 == None and Color2 == None:
			return color("BB"), print("[", end=""), color("VC"), print(Simbolo[-1], end=""), color("BB"), print("]", end="")

	
	elif (Simbolo == "-"):
		if Color1 != None and Color2 != None:
			return color(Color1), print("[", end=""), color(Color2), print(Simbolo, end=""), color(Color1), print("]", end="")
		elif Color1 != None and Color2 == None:
			return color(Color1), print("[", end=""), color("AZC"), print(Simbolo, end=""), color(Color1), print("]", end="")
		elif Color1 == None and Color2 != None:
			return color("BB"), print("[", end=""), color(Color2), print(Simbolo, end=""), color("BB"), print("]", end="")
		elif Color1 == None and Color2 == None:
			return color("BB"), print("[", end=""), color("AZC"), print(Simbolo, end=""), color("BB"), print("]", end="")
	
	elif (Simbolo == "!"):
		if Color1 != None and Color2 != None:
			return color(Color1), print("[", end=""), color(Color2), print(Simbolo, end=""), color(Color1), print("]", end="")
		elif Color1 != None and Color2 == None:
			return color(Color1), print("[", end=""), color("RC"), print(Simbolo, end=""), color(Color1), print("]", end="")
		elif Color1 == None and Color2 != None:
			return color("BB"), print("[", end=""), color(Color2), print(Simbolo, end=""), color("BB"), print("]", end="")
		elif Color1 == None and Color2 == None:
			return color("BB"), print("[", end=""), color("RC"), print(Simbolo, end=""), color("BB"), print("]", end="")
	
	elif (Simbolo == "¡"):
		if Color1 != None and Color2 != None:
			return color(Color1), print("[", end=""), color(Color2), print(Simbolo, end=""), color(Color1), print("]", end="")
		elif Color1 != None and Color2 == None:
			return color(Color1), print("[", end=""), color("AMC"), print(Simbolo, end=""), color(Color1), print("]", end="")
		elif Color1 == None and Color2 != None:
			return color("BB"), print("[", end=""), color(Color2), print(Simbolo, end=""), color("BB"), print("]", end="")
		elif Color1 == None and Color2 == None:
			return color("BB"), print("[", end=""), color("AMC"), print(Simbolo, end=""), color("BB"), print("]", end="")
	
	elif (Simbolo == "*"):
		if Color1 != None and Color2 != None:
			return color(Color1), print("[", end=""), color(Color2), print(Simbolo, end=""), color(Color1), print("]", end="")
		elif Color1 != None and Color2 == None:
			return color(Color1), print("[", end=""), color("PC"), print(Simbolo, end=""), color(Color1), print("]", end="")
		elif Color1 == None and Color2 != None:
			return color("BB"), print("[", end=""), color(Color2), print(Simbolo, end=""), color("BB"), print("]", end="")
		elif Color1 == None and Color2 == None:
			return color("BB"), print("[", end=""), color("PC"), print(Simbolo, end=""), color("BB"), print("]", end="")
	
	elif (Simbolo == "~"):
		if Color1 != None and Color2 != None:
			return color(Color1), print("[", end=""), color(Color2), print(Simbolo, end=""), color(Color1), print("]", end="")
		elif Color1 != None and Color2 == None:
			return color(Color1), print("[", end=""), color("BB"), print(Simbolo, end=""), color(Color1), print("]", end="")
		elif Color1 == None and Color2 != None:
			return color("VC"), print("[", end=""), color(Color2), print(Simbolo, end=""), color("VC"), print("]", end="")
		elif Color1 == None and Color2 == None:
			return color("VC"), print("[", end=""), color("BB"), print(Simbolo, end=""), color("VC"), print("]", end="")
	
	elif (Simbolo == "#"):
		if Color1 != None and Color2 != None:
			return color(Color1), print("[", end=""), color(Color2), print(Simbolo, end=""), color(Color1), print("]", end="")
		elif Color1 != None and Color2 == None:
			return color(Color1), print("[", end=""), color("G"), print(Simbolo, end=""), color(Color1), print("]", end="")
		elif Color1 == None and Color2 != None:
			return color("BB"), print("[", end=""), color(Color2), print(Simbolo, end=""), color("BB"), print("]", end="")
		elif Color1 == None and Color2 == None:
			return color("BB"), print("[", end=""), color("G"), print(Simbolo, end=""), color("BB"), print("]", end="")
	
	elif (Simbolo == "&"):
		if Color1 != None and Color2 != None:
			return color(Color1), print("[", end=""), color(Color2), print(Simbolo, end=""), color(Color1), print("]", end="")
		elif Color1 != None and Color2 == None:
			return color(Color1), print("[", end=""), color("RC"), print(Simbolo, end=""), color(Color1), print("]", end="")
		elif Color1 == None and Color2 != None:
			return color("VC"), print("[", end=""), color(Color2), print(Simbolo, end=""), color("VC"), print("]", end="")
		elif Color1 == None and Color2 == None:
			return color("VC"), print("[", end=""), color("RC"), print(Simbolo, end=""), color("VC"), print("]", end="")
	
	elif (Simbolo == "?"):
		if Color1 != None and Color2 != None:
			return color(Color1), print("[", end=""), color(Color2), print(Simbolo, end=""), color(Color1), print("]", end="")
		elif Color1 != None and Color2 == None:
			return color(Color1), print("[", end=""), color("AGMC"), print(Simbolo, end=""), color(Color1), print("]", end="")
		elif Color1 == None and Color2 != None:
			return color("AMC"), print("[", end=""), color(Color2), print(Simbolo, end=""), color("AMC"), print("]", end="")
		elif Color1 == None and Color2 == None:
			return color("AMC"), print("[", end=""), color("AGMC"), print(Simbolo, end=""), color("AMC"), print("]", end="")
	
	elif (Simbolo == " "):
		if Color1 != None and Color2 != None:
			return color(Color1), print("[", end=""), color(Color2), print(Simbolo, end=""), color(Color1), print("]", end="")
		elif Color1 != None and Color2 == None:
			return color(Color1), print("[", end=""), color("N"), print(Simbolo, end=""), color(Color1), print("]", end="")
		elif Color1 == None and Color2 != None:
			return color("BB"), print("[", end=""), color(Color2), print(Simbolo, end=""), color("BB"), print("]", end="")
		elif Color1 == None and Color2 == None:
			return color("BB"), print("[", end=""), color("N"), print(Simbolo, end=""), color("BB"), print("]", end="")
	

#________________________________________________________________________
#                               By: LawlietJH
#________________________________________________________________________



###### ###### ##### ##### Funciones de Uso Extras ##### ##### ###### ######



def iswindows():
	
	osver = os.popen("ver").read()
	
	if osver.find("Windows") > 0:
		return True
	else:
		return False


def islinux():
	
	osver = os.popen("ver").read()
	
	if osver.find("Linux") > 0:
		return True
	else:
		return False


def ispyver2():
	
	xD=sys.version[0]
	
	if int(xD) == 2:
		return True
	else:
		return False


def ispyver3():
	
	xD=sys.version[0]
	
	if int(xD) == 3:
		return True
	else:
		return False

print(ispyver2())
os.system("Pause>Nul")

def Clear():
	
    if os.name == "nt" or os.name == "ce" or os.name == "dos": #~ Windows(nt)\Windows(ce)\DOS
        os.system("cls")
    elif os.name == "posix": #~ Unix/Linux/MacOS/BSD
        os.system("clear")	


def inp(inp):
	
	if ispyver3():
		return input(inp)
	else:
		return raw_input(inp)


def WinSize(Ancho=82, Alto=55):
	
	os.system("mode con: cols={} lines={}".format(Ancho, Alto))


def ChkMod(nombre):
	
	import pydoc
	import re

	pat=re.compile(nombre,re.IGNORECASE)
	resultados=[]
	
	print("\n\n    ", end=""), Mark("&"), color("BB"), print(" Módulo:", end=""), color("AZC"), print("",nombre, "\n")
	
	def callback(p,n,d):
		if n.endswith(".__init__"):
			n=n[-9:]
		if pat.search(n):
			if n == nombre:
				print("      ", end=""), Mark(">+","VC"), color("VC"), print("", n)
			else:
				print("\t    ", end=""), Mark("+","VC"), color("VC"), print("", n)
			resultados.append( (n, p) )
            
	pydoc.ModuleScanner().run(callback)
	
	#~ return resultados


def HiddenCursor(imp="Hidden"):
	
	#~ imp = imp.title()		#Devuelve la cadena solo con la primera letra de cada palabra en mayuscula
	imp = imp.capitalize()		#Devuelve la cadena solo con la primera letra de la primer palabra en mayuscula

	if os.name == 'nt':
		import msvcrt
		import ctypes

		class _CursorInfo(ctypes.Structure):
			_fields_ = [("size", ctypes.c_int),
						("visible", ctypes.c_byte)]
	
	def hide_cursor():
		if os.name == 'nt':
			ci = _CursorInfo()
			handle = ctypes.windll.kernel32.GetStdHandle(-11)
			ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
			ci.visible = False
			ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))
		elif os.name == 'posix':
			sys.stdout.write("\033[?25l")
			sys.stdout.flush()

	def show_cursor():
		if os.name == 'nt':
			ci = _CursorInfo()
			handle = ctypes.windll.kernel32.GetStdHandle(-11)
			ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
			ci.visible = True
			ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))
		elif os.name == 'posix':
			sys.stdout.write("\033[?25h")
			sys.stdout.flush()
			
	if imp == "Hidden":
		hide_cursor()
	elif imp =="Show":
		show_cursor()
	else:
		return #print("\n\n\t\t Escribe: Show | Hidden\n\n\n\tEjemplo: Cursor(\"Hidden\")")

