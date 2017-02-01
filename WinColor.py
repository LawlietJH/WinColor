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
#                                                                 1.0.2

import ctypes, os

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
	Version = "\n\n{:^80}".format("1.0.3")
	
	return os.system("cls"),\
	       ColorI("BB"), print("\n\n",Nombre),\
	       ColorI("AZ"), print("\n\n",Autor),\
	       ColorI("RC"), print(Version), ColorF(),\
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
	elif ColorLetra == "x9" or ColorLetra == "azul cl" or ColorLetra == "AC" :
		Color = x9
	elif ColorLetra == "xA" or ColorLetra == "verde cl" or ColorLetra == "VC" :
		Color = xA
	elif ColorLetra == "xB" or ColorLetra == "aguamarina cl" or ColorLetra == "AMC" :
		Color = xB
	elif ColorLetra == "xC" or ColorLetra == "rojo cl" or ColorLetra == "RC" :
		Color = xC
	elif ColorLetra == "xD" or ColorLetra == "purpura cl" or ColorLetra == "PC" :
		Color = xD
	elif ColorLetra == "xE" or ColorLetra == "amarillo cl" or ColorLetra == "AC" :
		Color = xE
	elif ColorLetra == "xF" or ColorLetra == "blanco br" or ColorLetra == "BB" :
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
