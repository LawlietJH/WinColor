# -*- coding: utf-8 -*-
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

import ctypes

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


#~ Método que reinicia al color original
def get_csbi_attributes(handle):
    #~ Basado en winconsole.py de IPython
    
    import struct
    
    csbi = ctypes.create_string_buffer(22)
    res = ctypes.windll.kernel32.GetConsoleScreenBufferInfo(handle, csbi)
    assert res

    (bufx, bufy, curx, cury, wattr, left, top, right, bottom, maxx, maxy) = struct.unpack("hhhhHhhhhhh", csbi.raw)
    return wattr


#~ Método Que Indica En Donde Iniciará El Color.
def ColorI(ColorLetra):
	
	if ColorLetra == "xA" or ColorLetra == xA :
		Color = xA
	elif ColorLetra == "xB" or ColorLetra == xB :
		Color = xB
	elif ColorLetra == "xC" or ColorLetra == xC :
		Color = xC
	elif ColorLetra == "xD" or ColorLetra == xD :
		Color = xD
	elif ColorLetra == "xE" or ColorLetra == xE :
		Color = xE
	elif ColorLetra == "xF" or ColorLetra == xF :
		Color = xF
	else:
		Color = reset

	colorI = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, Color)
	return colorI


#~ Método Que Indica En Donde Terminará El Color.
def ColorF():
	colorF = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, reset)
	return colorF


#~ Métodos en variables que simplifican el nombre.
handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
reset = get_csbi_attributes(handle)

#________________________________________________________________________
#                               By: LawlietJH
#________________________________________________________________________


xD = input("Color: ")

ColorI(xA)
print("\n\n\t Texto De Ejemplo.")
ColorF()
