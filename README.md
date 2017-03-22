# WinColor
## Pon Color A Tus Scripts de Python En Windows.

- - -


      ██╗    ██╗██╗███╗   ██╗ ██████╗ ██████╗ ██╗      ██████╗ ██████╗ 
      ██║    ██║██║████╗  ██║██╔════╝██╔═══██╗██║     ██╔═══██╗██╔══██╗
      ██║ █╗ ██║██║██╔██╗ ██║██║     ██║   ██║██║     ██║   ██║██████╔╝
      ██║███╗██║██║██║╚██╗██║██║     ██║   ██║██║     ██║   ██║██╔══██╗
      ╚███╔███╔╝██║██║ ╚████║╚██████╗╚██████╔╝███████╗╚██████╔╝██║  ██║
       ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═╝

                           ╦  ┌─┐┬ ┬┬  ┬┌─┐┌┬┐ ╦╦ ╦
                           ║  ├─┤││││  │├┤  │  ║╠═╣
                           ╩═╝┴ ┴└┴┘┴─┘┴└─┘ ┴ ╚╝╩ ╩

                                     v1.1.7

- - -

### Modo de Uso:

+ Tienes que importar el módulo ___WinColor a tu Script___: __`import WinColor`__, esto te permitirá usar las ___funciones___: __`WinColor.color()`, `WinColor.rest()`, `WinColor.Dat()`__, etc...
  
+ Para importar todo, se escribe de la siguiente manera y así se evitará escribir demasiado: __`from WinColor import *`__, de esta manera se podrá llamar las funciones sin necesidad de especificar el nombre del ___módulo___, osea: __`WinColor.Dat()` ---> `Dat()`__

---

### Funciones Disponibles:

| Principales         | Interacción           | Parametros		        | Extras              | Booleanas             |
|:-------------------:|:---------------------:|:-------------------------:|:-------------------:|:---------------------:|
| [`color()`](#Color) | [`inp()`](#Inp)       | [`HiddenCursor()`](#HiCu) | [`Dat()`](#Dat)     | [`isWindows()`](#isW) |
| [`rest()`](#Rest)   | [`Mark()`](#Mark)     | [`WinSize()`](#WinSize)   | [`Clear()`](#Clear) | [`isLinux()`](#isL)   |
|                     | [`Pass()`](#Pass)     | [`ChkMod()`](#ChkMod)     | [`flush()`](#Flush) | [`isPyver2()`](#isP2) |
|                     | [`Access()`](#Access) |                           |                     | [`isPyver3()`](#isP3) |
|                     |                       |                           |                     | [`isAdmin()`](#isA)   |

---
<a name="Color"/>

## color()

[\[Código Fuente\]](https://github.com/LawlietJH/WinColor/blob/master/WinColor.py#L90)

### La función `color()` requiere una serie de parámetros, puede ser cualquiera de la siguiente lista:

```python
#~ Ejemplos:
color("x0"), color("negro"), color("N")
```
    
+ ___Lista De Colores___:

| Color            | Hex | Nombre        | Índice |
|:-----------------|:---:|:-------------:|:------:|
| Negro            | x0  | negro         | N      |
| Azul             | x1  | azul          | AZ     |
| Verde            | x2  | verde         | V      |
| Aguamarina       | x3  | aguamarina    | AG     |
| Rojo             | x4  | rojo          | R      |
| Púrpura          | x5  | purpura       | P      |
| Amarillo         | x6  | amarillo      | AM     |
| Blanco           | x7  | blanco        | B      |
| Gris             | x8  | gris          | G      |
| Azul Claro       | x9  | azul cl       | AZC    |
| Verde Claro      | xA  | verde cl      | VC     |
| Aguamarina Claro | xB  | aguamarina cl | AGMC   |   
| Rojo Claro       | xC  | rojo cl       | RC     |
| Púrpura Claro    | xD  | purpura cl    | PC     |
| Amarillo Claro   | xE  | amarillo cl   | AMC    |
| Blanco Brillante | xF  | blanco br     | BB     |

+ Ejemplos de uso:
  
  ```python
  
  from WinColor import *
  
  #~ Llamada a la función en lineas separadas.
  
  color("azul cl")
  print("\n\n\t Esto es un texto en Azul Claro")
  
  #~ Llamada a la función en una misma linea.
  
  color("xC"), print("\n\n\t Ahora Esta linea es de color Rojo Claro")
  
  #~ Poner colores en una sola linea.
  #~ Añadiendo end="" al final, remplazará el salto de linea que se hace por defecto en cada print() por
  #~ una cadena vacía, esto hará que se unan los 2 print() en una sola linea.
  #~ Se puede añadir la cadena que se desee en el end="Hola" y se añadirá entre ambos print().
  
  color("VC"), print("\n\n\t Texto color Verde Claro", end="")
  color("BB"), print("--->", end="")
  color("RC"), print("Texto color Rojo Claro")
  
  #~ Sabiendo usar 'end' podrías simplificar lo anterior de la siguiente manera,
  #~ pero esto provocara que la flecha se mantenga con el mismo color que en el texto en ese mismo print()
  
  color("xA"), print("Texto Verde Claro", end=" ---> ")
  color("xD"), print("Texto color Púrpura Claro")
  
  #~ Se puede añadir también de la siguiente manera, incluyendo la llamada a la función dentro del print()
  #~ pero sumandola despues de la cadena.
  #~ Es recomendable que por cada color nuevo que se desee agregar se use en diferentes print() ya que si
  #~ se colocan dos llamadas a una función en el mismo print(), se pondrá la linea con el color de la última
  #~ llamada a función.
  
  print("\n\n\t Texto colo Blanco Brillante"+color("xF"), end="")
  print(" Texto color Verde Claro"+color("VC"))
  
  ```
  
---
<a name="Rest"/>

## rest()

[\[Código Fuente\]](https://github.com/LawlietJH/WinColor/blob/master/WinColor.py#L136)

+ La función __`rest()`__ ___Restaura al color por defecto___ de la ventana.

---
<a name="Inp"/>

## inp()

[\[Código Fuente\]](https://github.com/LawlietJH/WinColor/blob/master/WinColor.py#L357)

+ Función que hace compatible __escribir en pantalla en cualquier Versión de Python__.

#### Modo de uso:

+ Se le pasa la cadena que se imprimir en pantalla para pedir datos.

+ Se usa de la misma manera en que se usaria ___raw_input()___ en Python 2 o ___input()___ en python 3.

```python
xD = inp("Escribe Algo: ")
``` 

---
<a name="Mark"/>

## Mark()

[\[Código Fuente\]](https://github.com/LawlietJH/WinColor/blob/master/WinColor.py#L159)

+ Esta simple y a su vez practica función, permite añadir cuadros con ___símbolos___, __[+], [-], [!],__ etc., para poder imprimir en pantalla con colores personalizados de forma ___rápida y practica___.
  
#### Modo de uso:
  
+ Por defecto: __`Mark()`__.
  Llamar la función de esta manera, por defecto imprimirá en pantalla: __`[ ]`__ 
  La cual tendra __Corchetes color Blanco Brillante y sin ningun Símbolo__.
   
+ Lista De Usos Por defecto:
  
   
| Función        |Símbolo |Color de Flecha   |Color de Símbolo  |Color de Corchetes|En Pantalla|
|:---------------|:------:|:----------------:|:----------------:|:----------------:|:---------:|
| `Mark()`       |Espacio |                  | Negro            | Blanco Brillante |`[ ]`      |
| `Mark("+")`    | +      |                  | Verde Claro      | Blanco Brillante | `[+]`     |
| `Mark(">+")`   | ---> + | Blanco Brillante | Verde Claro      | Blanco Brillante | `---> [+]`|
| `Mark("-")`    | -      |                  | Azul Claro       | Blanco Brillante | `[-]`     |
| `Mark("!")`    | !      |                  | Rojo Claro       | Blanco Brillante | `[!]`     |
| `Mark("¡")`    | ¡      |                  | Amarillo Claro   | Blanco Brillante | `[¡]`     |
| `Mark("*")`    | *      |                  | Aguamarina Claro | Blanco Brillante | `[*]`     |
| `Mark("~")`    | ~      |                  | Blanco Brillante | Verde Claro      | `[~]`     |
| `Mark("#")`    | #      |                  | Gris             | Blanco Brillante | `[#]`     |
| `Mark("&")`    | &      |                  | Verde Claro      | Aguamarina Claro | `[&]`     |
| `Mark("?")`    | ?      |                  | Amarillo Claro   | Aguamarina Claro | `[?]`     |
| `Mark("Hola")` | Hola   |                  | Blanco Brillante | Blanco Brillante | `[Hola]`  |
| `Mark(123)`    | 123    |                  | Blanco Brillante | Blanco Brillante | `[123]`   |

+ Ejemplos:
  
  ```python
   #~ Siempre se tiene que añadir fuera del print()
  
  print("\n\n\t", end=""), Mark(), print(" Hey!")
  print("\n\t", end=""), Mark("!","VC","BB"), print(" Hola Mundo!")
  
  print("\n\n\t Año: ", end=""), Mark(1995)
  
  #~ Se le puede pasar una variable a lafunción
  xD = "2017"
  print("\n\t Hola Mundo! en el año "), Mark(xD, "VC", "AGMC")
  
  #~ Mostraria: Hola Mundo! en el año [2017]
  #~ Con los colores Verde Claro para el número y Aguamarina Claro para los corchetes. 
  ```
  
---

<a name="Pass"/>

## Pass()

[\[Código Fuente\]](https://github.com/LawlietJH/WinColor/blob/master/WinColor.py#L400)

+ Permite ___escribir en pantalla___ de forma __oculta__, útil para escribir __contraseñas__.

#### Modo de Uso:

+ Con esto, se imprimirá en pantalla el texto que se le pase a la función ___(Por defecto, imprime una cadena vacia)___ y permitirá escribir una cadena de manera ___oculta (para evitar a los curiosos)___ y ésta, se almacenará en una variable para poder utilizarla en el ___Script___.

```py
xD = Pass("Escribe la contraseña:")
```

---
<a name="Access"/>

## Access()

[\[Código Fuente\]](https://github.com/LawlietJH/WinColor/blob/master/WinColor.py#L412)

+ Pide Una Contraseña y Devuelve __True__ Si la Contraseña que escriba el Usuario
 Coincide Con la Indicada Que se le paso a la Función.
+ La Contraseña se Escribe de manera Oculta usando la funcion Pass()

#### Modo de Uso:

+ Por defecto:

    + Impresion en Pantalla: \n\n\t Pwd:
    + Contraseña: xD
   
```
Bool = Access()
```

+ Pasando Una Cadena y una Contraseña en los argumentos para Imprimir en Pantalla:

```
# Pedirá una contraseña y si es la misma devolvera True.

Pwd = "Dat"
Bool = Access("\n\n\t Escribe La Contraseña: ", Pwd)

```

+ Ejemplo:

```
Pwd = "Pass"

while True:
	
	Acceso = Access("\n\n\t Contraseña: ", Pwd)

	if Acceso == True:
		print("\n\n\t [*] Contraseña Correcta.")
		exit(0)
	else:
		print("\n\n\t [!] Contraseña Incorrecta!")
```

---
<a name="HiCu"/>

## HiddenCursor()

[\[Código Fuente\]](https://github.com/LawlietJH/WinColor/blob/master/WinColor.py#L422)

+ __Oculta o Muestra el Puntero en Pantalla__.

#### Modo de Uso:

+ Por Defecto, __ocultará el Puntero__ con solo Mandar a llamar la función.
```python
HiddenCursor()
```

+ Para __Ocultar/Desocultar__ el Puntero puedes mandar a llamar la función de las siguientes maneras.
```python

#~ Para ocultar.
HiddenCursor("Hide")

#~ Para mostrar.
HiddenCursor("Show")
```

---
<a name="WinSize"/>

## WinSize()

[\[Código Fuente\]](https://github.com/LawlietJH/WinColor/blob/master/WinColor.py#L365)

+ Cambia el ___tamaño de la ventana___ al antojo.

#### Modo de Uso:

+ Por Defecto pondra el ___tamaño de la ventana___ en __Ancho=82, Alto=55__
```python
WinSize()
```

+ Pondra el ___tamaño de la ventana___ en __Ancho=50, Alto=25__
```python
WinSize(50,25)
```

---
<a name="ChkMod"/>

## ChkMod()

[\[Código Fuente\]](https://github.com/LawlietJH/WinColor/blob/master/WinColor.py#L372)

+ Mostrará Todos los ___Archivos___ Contenidos en Algún Módulo.

#### Modo de Uso:

+ Esto mostrará todos los ___archivos___ del __Módulo__: ___sys___
```python
ChkMod("sys")
```

+ Esto mostrará todos los ___archivos___ del __Módulo__: ___os___
```python
ChkMod("os")
```

---
<a name="Dat"/>

## Dat()

[\[Código Fuente\]](https://github.com/LawlietJH/WinColor/blob/master/WinColor.py#L36)
 
+ La función __`Dat()`__ limpiará pantalla y mostrara el ___Nombre, Autor y Versión del Script___ y cerrará el programa.

---
<a name="Clear"/>

## Clear()

[\[Código Fuente\]](https://github.com/LawlietJH/WinColor/blob/master/WinColor.py#L342)

+ Función que hace compatible __limpiar pantalla__ en cualquier ___Sistema Operativo___ (__Linux, Windows__, etc).

---
<a name="Flush"/>

## flush()

[\[Código Fuente\]](https://github.com/LawlietJH/WinColor/blob/master/WinColor.py#L153)

 + La función __`flush()`__ es una función ___auxiliar___ que ayudará a limpiar el buffer y hacer que imprimirá los colores correctamente en dado caso de alguna falla al imprimir en pantalla con algún color.
  
 + Para usar esta función simplemente se tiene que colocar el nombre __`flush()`__ antes de la función __`color()`__ con la que se tenga problemas al imprimir el color (si es que llegara a suceder, pero en verdad, dudo que pase).

---
<a name="isW"/>

## isWindows()

[\[Código Fuente\]](https://github.com/LawlietJH/WinColor/blob/master/WinColor.py#L287)

+ Devuelve __True__ si el ___sistema operativo___ es __Windows__

---
<a name="isL"/>

## isLinux()

[\[Código Fuente\]](https://github.com/LawlietJH/WinColor/blob/master/WinColor.py#L297)

+ Devuelve __True__ si el ___sistema operativo___ es __Linux__

---
<a name="isP2"/>

## isPyver2()

[\[Código Fuente\]](https://github.com/LawlietJH/WinColor/blob/master/WinColor.py#L307)

+ Devuelve __True__ si la ___versión___ de __Python__ es 2.X

---
<a name="isP3"/>

## isPyver3()

[\[Código Fuente\]](https://github.com/LawlietJH/WinColor/blob/master/WinColor.py#L317)

+ Devuelve __True__ si la ___versión___ de __Python__ es 3.X

---
<a name="isA"/>

## isAdmin()

[\[Código Fuente\]](https://github.com/LawlietJH/WinColor/blob/master/WinColor.py#L327)

+ Devuelve __True__ si el ___Script___ se está ejecutando con _Permisos de Administrador_.
