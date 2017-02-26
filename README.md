# WinColor
## Pon Color A Tus Scripts de Python En Windows.

## Por: LawlietJH - v1.1.4

### Modo de Uso:

+ Tienes que importar el módulo WinColor a tu Script: __`import WinColor`__, esto te permitirá usar los métodos: __`WinColor.color()`, `WinColor.rest()`, `WinColor.Dat()`__, etc...
  
+ Para importar todo, se escribe de la siguiente manera y así se evitará escribir demasiado: __`from WinColor import *`__, de esta manera se podrá llamar a los métodos sin necesidad de especificar el nombre del módulo: __`WinColor.Dat()` ---> `Dat()`__

---

### Funciones Disponibles:

| Principales         | Interacción       | Parametros       | Extras     | Booleanas    |
|:-------------------:|:-----------------:|:----------------:|:----------:|:------------:|
| [`color()`](#color) | [`inp()`](#inp)   | `HiddenCursor()` | `Dat()`    | `isWindows()`|
| [`rest()`](#rest)   | [`Mark()`](#Mark) | `WinSize()`      | `Clear()`  | `isLinux()`  |
|                     | `Pass()`          | `ChkMod()`       | `flush()`  | `isPyver2()` |
|                     |                   |                  |            | `isPyver3()` |

---
<a name="color"/>
## color()

[\[Código Fuente\]](https://github.com/LawlietJH/WinColor/blob/master/WinColor.py#L89)

### La función `color()` requiere una serie de parámetros, puede ser cualquiera de la siguiente lista:

```python
#~ Ejemplos:
color("x0"), color("negro"), color("N")
```
    
+ Lista De Colores:

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
<a name="rest"/>  
## rest()

[\[Código Fuente\]](https://github.com/LawlietJH/WinColor/blob/master/WinColor.py#L135)

+ La función __`rest()`__ Restaura al color por defecto de la ventana.

---
<a name="inp"/>
## inp()

[\[Código Fuente\]](https://github.com/LawlietJH/WinColor/blob/master/WinColor.py#L338)

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

+ Esta simple y a su vez practica función, permite añadir cuadros con símbolos, __[+], [-], [!],__ etc., para poder imprimir en pantalla con colores personalizados de forma rápida y practica.
  
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

## Pass()

+ Permite escribir en pantalla de forma __oculta__, útil para escribir __contraseñas__.

#### Modo de Uso:

+ Con esto, se imprimirá en pantalla el texto que se le pase a la función ___(Por defecto, imprime una cadena vacia)___ y permitirá escribir una cadena de manera ___oculta (para evitar a los curiosos)___ y ésta, se almacenará en una variable para poder utilizarla en el programa.

```py
xD = Pass("Escribe la contraseña:")
```

---

## HiddenCursor()

+ __Oculta o Muestra el Puntero en Pantalla__.

#### Modo de Uso:

+ Por Defecto, __ocultará el Puntero__ con solo Mandar a llamar la función.
```python
HiddenCursor()
```

+ Para __Ocultar/Desocultar__ el Puntero puedes mandar a llamar la función de las siguientes maneras.
```python

#~ Para ocultar.
HiddenCursor("Hidden")

#~ Para mostrar.
HiddenCursor("Show")
```

---

## WinSize()

+ Cambia el tamaño de la ventana al antojo.

#### Modo de Uso:

+ Por Defecto pondra el tamaño de la ventana en __Ancho=82, Alto=55__
```python
WinSize()
```

+ Pondra el tamaño de la ventana en __Ancho=50, Alto=25__
```python
WinSize(50,25)
```

---

## ChkMod()

+ Mostrará Todos Método de Algún Módulo.

#### Modo de Uso:

+ Esto mostrará todas las funciones del __Módulo__: ___sys___
```python
ChkMod("sys")
```

+ Esto mostrará todas las funciones del __Módulo__: ___os___
```python
ChkMod("os")
```

---

## Dat()
 
+ La función __`Dat()`__ limpiará pantalla y mostrara el Nombre, Autor y Versión del Script y cerrará el programa.

---

## Clear()

+ Función que hace compatible __limpiar pantalla__ en cualquier Sistema Operativo (__Linux, Windows__, etc).

---

## flush()
 + La función __`flush()`__ es una función ___auxiliar___ que ayudará a limpiar el buffer y hacer que imprimirá los colores correctamente en dado caso de alguna falla al imprimir en pantalla con algún color.
  
 + Para usar esta función simplemente se tiene que colocar el nombre __`flush()`__ antes de la función __`color()`__ con la que se tenga problemas al imprimir el color (si es que llegara a suceder, pero en verdad, dudo que pase).

---

## isWindows()

+ Devuelve __True__ si el sistema operativo es __Windows__

---

## isLinux()

+ Devuelve __True__ si el sistema operativo es __Linux__

---

## isPyver2()

+ Devuelve __True__ si la versión de __Python__ es 2.X

---

## isPyver3()

+ Devuelve __True__ si la versión de __Python__ es 3.X
