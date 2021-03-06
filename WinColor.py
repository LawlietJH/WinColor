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
#                                                                 1.2.2

import ctypes
import time
import sys
import os


BWC = r"""
                      ╦ ╦  ┬  ┌┐┌   ╔═╗ ┌─┐ ┬   ┌─┐ ┬─┐
                      ║║║  │  │││   ║   │ │ │   │ │ ├┬┘
                      ╚╩╝  ┴  ┘└┘   ╚═╝ └─┘ ┴─┘ └─┘ ┴└─
"""
# Fuente: Calvin S, Página: http://patorjk.com/software/taag

BA = r"""
                           ╦  ┌─┐┬ ┬┬  ┬┌─┐┌┬┐ ╦╦ ╦
                           ║  ├─┤││││  │├┤  │  ║╠═╣
                           ╩═╝┴ ┴└┴┘┴─┘┴└─┘ ┴ ╚╝╩ ╩
"""
# Fuente: Calvin S, Página: http://patorjk.com/software/taag


def Dat():
	
	Nombre = BWC
	Autor = BA
	Version = "\n\n\n{:^80}".format("v1.2.2")
	
	return os.system("cls"), WinSize(80,24),\
	       color("VC"), print("\n\n", BWC), time.sleep(0.1),\
	       color("AZC"), print("\n\n", Autor), time.sleep(0.1),\
	       color("RC"), print(Version), rest(),\
	       os.system("Pause>Nul"), exit(0)

#________________________________________________________________________
#________________________________________________________________________

# Constantes de la API de Windows.
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


# Función que reinicia al color original
def get_csbi_attributes(handle):
    #~ Basado en winconsole.py de IPython
    
    import struct
    
    csbi = ctypes.create_string_buffer(22)
    res = ctypes.windll.kernel32.GetConsoleScreenBufferInfo(handle, csbi)
    assert res

    (bufx, bufy, curx, cury, wattr, left, top, right, bottom, maxx, maxy) = struct.unpack("hhhhHhhhhhh", csbi.raw)
    return wattr


# Función Que Indica En Donde Iniciará El Color.
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
	elif ColorLetra == "xB" or ColorLetra == "aguamarina cl" or ColorLetra == "AGMC" :
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



# Función Que Indica En Donde Terminará El Color.
def rest():
	
	flush()
	
	reinicar = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, reset)
	
	return reinicar



# Variables que simplifican el nombre.
handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
reset = get_csbi_attributes(handle)



# Función que sirve para poder poner colores en la misma linea
def flush():
	return sys.stdout.flush()


	
# Función para mostrar recuadro [+], [-], [!], [¡], [*], [~], [#], [&], [?], [ ] con colores
def Mark(Simbolo = " ", Color2 = None, Color1 = None):
	
	if (Simbolo == "+") or (Simbolo == ">+"):
		
		if(Simbolo[0] == ">"):
			color("BB"), print(" ===> ", end="")
		
		if Color1 != None and Color2 != None:
			return print("["+color(Color1), end=""), print(Simbolo[-1]+color(Color2), end=""), print("]"+color(Color1), end="")
		elif Color1 != None and Color2 == None:
			return print("["+color(Color1), end=""), print(Simbolo[-1]+color("VC"), end=""), print("]"+ color(Color1), end="")
		elif Color1 == None and Color2 != None:
			return print("["+color("BB"), end=""), print(Simbolo[-1]+color(Color2), end=""), print("]"+color("BB"), end="")
		elif Color1 == None and Color2 == None:
			return print("["+color("BB"), end=""), print(Simbolo[-1]+color("VC"), end=""), print("]"+color("BB"), end="")

	
	elif (Simbolo == "-"):
		if Color1 != None and Color2 != None:
			return print("["+color(Color1), end=""), print(Simbolo+color(Color2), end=""), print("]"+color(Color1), end="")
		elif Color1 != None and Color2 == None:
			return print("["+color(Color1), end=""), print(Simbolo+color("AZC"), end=""), print("]"+color(Color1), end="")
		elif Color1 == None and Color2 != None:
			return print("["+color("BB"), end=""), print(Simbolo+color(Color2), end=""), print("]"+color("BB"), end="")
		elif Color1 == None and Color2 == None:
			return print("["+color("BB"), end=""), print(Simbolo+color("AZC"), end=""), print("]"+color("BB"), end="")
	
	elif (Simbolo == "!"):
		if Color1 != None and Color2 != None:
			return print("["+color(Color1), end=""), print(Simbolo+color(Color2), end=""), print("]"+color(Color1), end="")
		elif Color1 != None and Color2 == None:
			return print("["+color(Color1), end=""), print(Simbolo+color("RC"), end=""), print("]"+color(Color1), end="")
		elif Color1 == None and Color2 != None:
			return print("["+color("BB"), end=""), print(Simbolo+color(Color2), end=""), print("]"+color("BB"), end="")
		elif Color1 == None and Color2 == None:
			return print("["+color("BB"), end=""), print(Simbolo+color("RC"), end=""), print("]"+color("BB"), end="")
	
	elif (Simbolo == "¡"):
		if Color1 != None and Color2 != None:
			return print("["+color(Color1), end=""), print(Simbolo+color(Color2), end=""), print("]"+color(Color1), end="")
		elif Color1 != None and Color2 == None:
			return print("["+color(Color1), end=""), print(Simbolo+color("AMC"), end=""), print("]"+color(Color1), end="")
		elif Color1 == None and Color2 != None:
			return print("["+color("BB"), end=""), print(Simbolo+color(Color2), end=""), print("]"+color("BB"), end="")
		elif Color1 == None and Color2 == None:
			return print("["+color("BB"), end=""), print(Simbolo+color("AMC"), end=""), print("]"+color("BB"), end="")
	
	elif (Simbolo == "*"):
		if Color1 != None and Color2 != None:
			return print("["+color(Color1), end=""), print(Simbolo+color(Color2), end=""), print("]"+color(Color1), end="")
		elif Color1 != None and Color2 == None:
			return print("["+color(Color1), end=""), print(Simbolo+color("AGMC"), end=""), print("]"+color(Color1), end="")
		elif Color1 == None and Color2 != None:
			return print("["+color("BB"), end=""), print(Simbolo+color(Color2), end=""), print("]"+color("BB"), end="")
		elif Color1 == None and Color2 == None:
			return print("["+color("BB"), end=""), print(Simbolo+color("AGMC"), end=""), print("]"+color("BB"), end="")
	
	elif (Simbolo == "~"):
		if Color1 != None and Color2 != None:
			return print("["+color(Color1), end=""), print(Simbolo+color(Color2), end=""), print("]"+color(Color1), end="")
		elif Color1 != None and Color2 == None:
			return print("["+color(Color1), end=""), print(Simbolo+color("BB"), end=""), print("]"+color(Color1), end="")
		elif Color1 == None and Color2 != None:
			return print("["+color("VC"), end=""), print(Simbolo+color(Color2), end=""), print("]"+color("VC"), end="")
		elif Color1 == None and Color2 == None:
			return print("["+color("VC"), end=""), print(Simbolo+color("BB"), end=""), print("]"+color("VC"), end="")
	
	elif (Simbolo == "#"):
		if Color1 != None and Color2 != None:
			return print("["+color(Color1), end=""), print(Simbolo+color(Color2), end=""), print("]"+color(Color1), end="")
		elif Color1 != None and Color2 == None:
			return print("["+color(Color1), end=""), print(Simbolo+color("G"), end=""), print("]"+color(Color1), end="")
		elif Color1 == None and Color2 != None:
			return print("["+color("BB"), end=""), print(Simbolo+color(Color2), end=""), print("]"+color("BB"), end="")
		elif Color1 == None and Color2 == None:
			return print("["+color("BB"), end=""), print(Simbolo+color("G"), end=""), print("]"+color("BB"), end="")
	
	elif (Simbolo == "&"):
		if Color1 != None and Color2 != None:
			return print("["+color(Color1), end=""), print(Simbolo+color(Color2), end=""), print("]"+color(Color1), end="")
		elif Color1 != None and Color2 == None:
			return print("["+color(Color1), end=""), print(Simbolo+color("VC"), end=""), print("]"+color(Color1), end="")
		elif Color1 == None and Color2 != None:
			return print("["+color("AGMC"), end=""), print(Simbolo+color(Color2), end=""), print("]"+color("AGMC"), end="")
		elif Color1 == None and Color2 == None:
			return print("["+color("AGMC"), end=""), print(Simbolo+color("VC"), end=""), print("]"+color("AGMC"), end="")
	
	elif (Simbolo == "?"):
		if Color1 != None and Color2 != None:
			return print("["+color(Color1), end=""), print(Simbolo+color(Color2), end=""), print("]"+color(Color1), end="")
		elif Color1 != None and Color2 == None:
			return print("["+color(Color1), end=""), print(Simbolo+color("AMC"), end=""), print("]"+color(Color1), end="")
		elif Color1 == None and Color2 != None:
			return print("["+color("AGMC"), end=""), print(Simbolo+color(Color2), end=""), print("]"+color("AGMC"), end="")
		elif Color1 == None and Color2 == None:
			return print("["+color("AGMC"), end=""), print(Simbolo+color("AMC"), end=""), print("]"+color("AGMC"), end="")
	
	elif (Simbolo == " "):
		if Color1 != None and Color2 != None:
			return print("["+color(Color1), end=""), print(Simbolo+color(Color2), end=""), print("]"+color(Color1), end="")
		elif Color1 != None and Color2 == None:
			return print("["+color(Color1), end=""), print(Simbolo+color("N"), end=""), print("]"+color(Color1), end="")
		elif Color1 == None and Color2 != None:
			return print("["+color("BB"), end=""), print(Simbolo+color(Color2), end=""), print("]"+color("BB"), end="")
		elif Color1 == None and Color2 == None:
			return print("["+color("BB"), end=""), print(Simbolo+color("N"), end=""), print("]"+color("BB"), end="")
	
	else:
		if Color1 != None and Color2 != None:
			return print("["+color(Color1), end=""), print(Simbolo+color(Color2), end=""), print("]"+color(Color1), end="")
		elif Color1 != None and Color2 == None:
			return print("["+color(Color1), end=""), print(Simbolo+color("BB"), end=""), print("]"+color(Color1), end="")
		elif Color1 == None and Color2 != None:
			return print("["+color("BB"), end=""), print(Simbolo+color(Color2), end=""), print("]"+color("BB"), end="")
		elif Color1 == None and Color2 == None:
			return print("["+color("BB"), end=""), print(Simbolo+color("BB"), end=""), print("]"+color("BB"), end="")

#________________________________________________________________________
#                               By: LawlietJH
#________________________________________________________________________



###### ###### ##### ##### Funciones de Uso Extras ##### ##### ###### ######



# Función Que Comprueba si el SO es Windows, Devuelve TRUE/FALSE
def isWindows():
	
	osver = os.popen("ver").read()
	
	if osver.find("Windows") > 0: return True
	else: return False



# Función Que Comprueba si el SO es Linux, Devuelve TRUE/FALSE
def isLinux():
	
	osver = os.popen("ver").read()
	
	if osver.find("Linux") > 0: return True
	else: return False



# Función Que Comprueba si es Python Versión 2, Devuelve TRUE/FALSE
def isPyver2():
	
	xD=sys.version[0]
	
	if int(xD) == 2: return True
	else: return False



# Función Que Comprueba si es Python Versión 3, Devuelve TRUE/FALSE
def isPyver3():
	
	xD=sys.version[0]
	
	if int(xD) == 3: return True
	else: return False



# Función Que Permite Saber Si Se Tienen Permisos de Administrador.
def isAdmin():
	
	if isWindows():

		xD = ctypes.windll.shell32.IsUserAnAdmin()
		
		if xD == 1: return True
		else: return False
	
	elif isLinux():
		
		if os.geteuid() != 0: return False
		else: return True
	
	else:
		return "Desconocido"



# Función Que Permite Limpiar Pantalla Compatible Con Diferentes Sistemas Operativos (SO).
def Clear():
	
    if os.name == "nt" or os.name == "ce" or os.name == "dos": #~ Windows(nt)\Windows(ce)\DOS
        os.system("cls")
    elif os.name == "posix": #~ Unix/Linux/MacOS/BSD
        os.system("clear")	



# Función Que Permite Imprimir En Pantalla Compatible Con Python Versión 2 y 3, Devuelve Cadena
def inp(inp):
	
	if isPyver3(): return input(inp)
	elif isPyver2(): return raw_input(inp)



# Función Que Permite Cambiar el Tamaño de la Pantalla.
def WinSize(Ancho=82, Alto=55):
	
	os.system("mode con: cols={} lines={}".format(Ancho, Alto))



# Función Que Permite Checar Un Módulo.
def ChkMod(nombre):
	
	import pydoc
	import re

	pat=re.compile(nombre,re.IGNORECASE)
	resultados=[]
	
	print("\n\n    ", end=""), Mark("&"), print(" Módulo: "+color("BB"), end=""), print(nombre+color("AZC"), "\n")
	
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
	
	return resultados



# Función Que Permite Esconder El Texto de la Pantalla.
# Para escribrir por ejemplo contraseñas y evitar a los curiosos.
def Pass(Text=""):
	
	from getpass import getpass as pwd
	
	Pwd = pwd(Text)
	
	return Pwd



# Funcion Que pide escribir una contraseña y si Coincide con la Contraseña
# Que fue pasada a la función con los argumentos, devolvera True.
def Access(String="\n\n\t Pwd: ", Pwd = "xD"):
	
	Cadena = Pass(String)
	
	if Cadena == Pwd: return True
	else: return False



# Función Que Permite Esconder El Cursor de la Pantalla (La rayita que parpadea xD).
def HiddenCursor(imp="Hide"):
	
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
	
		
	if imp == "Hide": hide_cursor()
	elif imp =="Show": show_cursor()
	else: return
	
	# http://stackoverflow.com/questions/5174810/how-to-turn-off-blinking-cursor-in-command-window



# Función Que Limpia El Buffer (Hace Flush) Para Que los Input Aparescan En Limpio Siempre.
# Ya Que Si Se Escribe A La 'Nada' Antes De Un Input, Todo Lo Escrito Aparecera En El Input.
# Con Esta Función Se Evita Eso.
def Imp():	# Limpia El Buffer (Flush)
    
    try:
        
        import msvcrt
        
        while msvcrt.kbhit(): msvcrt.getch()
        
    except ImportError:
		
        import sys, termios
        
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)



def Progreso(x, Total):
	
	TamBar = 30
	Progreso = (x * 100) / Total
	Actual = x / Total
	
	TiempoTransc = int(time.clock()) + 1
	BarraAct = int(Actual * TamBar)
	
	bar = "\r Progreso: {:.2f}%".format(Progreso)
	bar += ' |' + '█'.join(['' for _ in range(BarraAct)])  # Imprimir Progreso.
	bar += ' '.join(['' for _ in range(int(TamBar - BarraAct))]) + '|'
	bar += " [" + Tiempo((Total - x) * (TiempoTransc / x))  + "] "	# Imprimir Tiempo Restante.
	
	sys.stdout.write(bar)



def Tiempo(sec):
	
	if sec >= 3600:  # Convierte a Horas
		return '{0:d} hora(s)'.format(int(sec / 3600))
	elif sec >= 60:  # Convierte a Minutos
		return '{0:d} minuto(s)'.format(int(sec / 60))
	else:            # Sin Conversión
		return '{0:d} segundo(s)'.format(int(sec))



# Abre Una Nueva Ventana Con Permisos De Administrador.
def runAsAdmin(Show="Show",cmdLine=None):
	
	import traceback, types
	
	if isAdmin() == False:
		
		#=======================================================================
	
		def Chk_Dep():
			
			try:
				import win32api
				
			except ModuleNotFoundError:
				print("\n\n\t[!] Instalando Dependencias...\n\n\t\t")
				os.system("Title Instalando pypiwin32 && pip install pypiwin32 > Nul && cls && Title Pandoraz.py            By: LawlietJH")
				
			except Exception as ex:
				print( type(ex).__name__ )		#Ver cuando ocurre un error y poder añadirlo a las ecepciones, y no cierre el programa.
		
		Chk_Dep()				#~ Se instala el módulo keyboard si este no esta instalado.
		try:
			import win32api, win32con, win32event, win32process	# Se Importan Módulos de pypiwin32.
			from win32com.shell.shell import ShellExecuteEx
			from win32com.shell import shellcon
		except:					# Si Hay Algún Error Significa Que No Se Instaló Correctamente.
			print("\n\n   No se pudo instalar correctamente el Módulo 'pypiwin32'.")
			print("\n   Revise Su Conexión o Instale El Módulo Manualmente Desde Consola Con:")
			print("\n\t 'pip install keyboard'   o   ' pip3 install keyboard'")
			
			try:
				os.system("Pause > Nul")
			except KeyboardInterrupt: pass
			
			Dat()
			Salir(0)
		
		#=======================================================================
		
		if os.name != 'nt': exit(0)
		
		if Show == "Hide": showCmd = win32con.SW_HIDE		# Abre El CMD en Modo Oculto.
		elif Show == "Show": showCmd = win32con.SW_SHOWNORMAL	# Abre El CMD Normal.
		else:
			print("\n\n\n\t [!] El Parámetro " + Show + " En runAsAdmin() No Se Reconoce." +\
				"\n\n\t     Usa 'Show' o 'Hide'." +\
				"\n\n\t     Si No Escribes Ningún Parámetro, Por defecto se Usara 'Show'.")
			exit(0)
		
		python_exe = sys.executable
		
		if cmdLine is None:
			cmdLine = [python_exe] + sys.argv
		elif type(cmdLine) not in (types.TupleType,types.ListType): exit(0)
		
		cmd = '"{}"'.format(cmdLine[0],)
		
		params = " ".join(['"{}"'.format(x,) for x in cmdLine[1:]])
		cmdDir = ''
		
		lpVerb = 'runas'  # Causa Elevación De Privilegios.
		
		# ShellExecute() no parece que nos permita obtener el PID o manejar el proceso,
		# por lo que no podemos obtener nada útil de él. Por lo tanto,
		# el más complejo ShellExecuteEx() debe ser utilizado.
		
		#================================================================================================================================
		# Método 1: Abrirá Una Ventana Con Permisos De Administrador
		#           y La Ventana Anterior Continuará La Ejecución Normal Sin Detenerse.
		
		# Ventana Con Permisos De Admin.
		#~ procHandle = win32api.ShellExecute(0, lpVerb, cmd, params, cmdDir, showCmd)
		#================================================================================================================================
		
		#================================================================================================================================
		# Método 2: Abrira Una Ventana Con Permisos De Administrador
		#           y Pausará La Ventana Anterior Hasta Que Se Cierre La Ventana
		#           Nueva Que Tiene Ya Permisos De Administrador.
		
		# Ventana Con Permisos De Admin.
		procInfo = ShellExecuteEx(nShow=showCmd, fMask=shellcon.SEE_MASK_NOCLOSEPROCESS, lpVerb=lpVerb, lpFile=cmd, lpParameters=params)
		#================================================================================================================================
		
		return False
	
	else: return True
	
	#~ http://pt.stackoverflow.com/questions/6929/como-rodar-um-subprocess-com-permiss%C3%A3o-de-administrador



#=======================================================================



# Abre Una Nueva Ventana Para Ejecutar Otro Script.
def Run(Programa=""):
	
	#=======================================================================
	
	def Chk_Dep():
		
		try:
			import win32api
			
		except ModuleNotFoundError:
			print("\n\n\t[!] Instalando Dependencias...\n\n\t\t")
			os.system("Title Instalando pypiwin32 && pip install pypiwin32 > Nul && cls && Title Pandoraz.py            By: LawlietJH")
			
		except Exception as ex:
			print( type(ex).__name__ )		#Ver cuando ocurre un error y poder añadirlo a las ecepciones, y no cierre el programa.
	
	Chk_Dep()				#~ Se instala el módulo keyboard si este no esta instalado.
	try:
		import win32api, win32con, win32event, win32process	# Se Importan Módulos de pypiwin32.
		from win32com.shell.shell import ShellExecuteEx
		from win32com.shell import shellcon
	except:					# Si Hay Algún Error Significa Que No Se Instaló Correctamente.
		print("\n\n   No se pudo instalar correctamente el Módulo 'pypiwin32'.")
		print("\n   Revise Su Conexión o Instale El Módulo Manualmente Desde Consola Con:")
		print("\n\t 'pip install keyboard'   o   ' pip3 install keyboard'")
		
		try:
			os.system("Pause > Nul")
		except KeyboardInterrupt: pass
		
		Dat()
		Salir(0)
	
	#=======================================================================
	
	import traceback, types
	
	showCmd = win32con.SW_SHOWNORMAL
	cmd = Programa
	params = ''
	cmdDir = ''
	lpVerb = ''
	
	procHandle = win32api.ShellExecute(0, lpVerb, cmd, params, cmdDir, showCmd)
	#~ procInfo = ShellExecuteEx(nShow=showCmd, fMask=shellcon.SEE_MASK_NOCLOSEPROCESS, lpVerb=lpVerb, lpFile=cmd, lpParameters=params)
	
	#~ http://pt.stackoverflow.com/questions/6929/como-rodar-um-subprocess-com-permiss%C3%A3o-de-administrador



#=======================================================================



# Datos De Prueba:
#~ if runAsAdmin("Show"):
	
	#~ print("\n\n\n\t [+] Tengo Permisos De Administrador B)")
	#~ os.system("Pause")
	#~ Dat()

#~ else:
	
	#~ print("\n\n\n\t [!] No Tengo Permisos De Administrador :/")
	#~ Run("Info.py")
	#~ os.system("Pause")
	#~ Dat()
