# WinColor
## Pon Color A Tus Scripts de Python En Windows.

### Modo de Uso:

+ Tienes que importar el módulo WinColor a tu Script: `import WinColor`, esto te permitirá usar los métodos: `WinColor.color()`, `WinColor.rest()`, `WinColor.Dat()`, etc...
  
+ Para importar todo, se escribe de la siguiente manera y así se evitará escribir demasiado: `from WinColor import *`, de esta manera se podrá llamar a los métodos sin necesidad de especificar el nombre del módulo: `WinColor.Dat()` ---> `Dat()`

---

### Funciones Disponibles:

+ `Dat()`
+ `color()`
+ `rest()`
+ `flush()`
+ `Mark()`
+ `isWindows()`
+ `isLinux()`
+ `isPyver2()`
+ `isPyver3()`
+ `Clear()`
+ `inp()`
+ `WinSize()`
+ `ChkMod()`
+ `HiddenCursor()`

---

## color()

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
  
## rest()

+ La función `rest()` Restaura al color por defecto de la ventana.

---

## Dat()
 
+ La función `Dat()` limpiará pantalla y mostrara el Nombre, Autor y Versión del Script y cerrará el programa.

---

## flush()
 + La función `flush()` es una función ___auxiliar___ que ayudará a limpiar el buffer y hacer que imprimirá los colores correctamente en dado caso de alguna falla al imprimir en pantalla con algún color.
  
 + Para usar esta función simplemente se tiene que colocar el nombre `flush()` antes de la función `color()` con la que se tenga problemas al imprimir el color (si es que llegara a suceder, pero en verdad, dudo que pase).

---

## Mark()

+ Esta simple y a su vez practica función, permite añadir cuadros con símbolos, [+], [-], [!], etc., para poder imprimir en pantalla con colores personalizados de forma rápida y practica.
  
#### Modo de uso:
  
+ Por defecto: `Mark()`.
  Llamar la función de esta manera, por defecto imprimirá en pantalla: `[ ]` 
  La cual tendra Corchetes color Blanco Brillante y sin ningun Símbolo.
   
+ Lista De Usos Por defecto:
  
   
| Función    |Símbolo |Color de Flecha   |Color de Símbolo  |Color de Corchetes|En Pantalla|
|:-----------|:------:|:----------------:|:----------------:|:----------------:|:---------:|
|`Mark()`    |Espacio |                  | Negro            | Blanco Brillante |`[ ]`      |
|`Mark("+")` | +      |                  | Verde Claro      | Blanco Brillante | `[+]`     |
|`Mark(">+")`| ---> + | Blanco Brillante | Verde Claro      | Blanco Brillante | `---> [+]`|
|`Mark("-")` | -      |                  | Azul Claro       | Blanco Brillante | `[-]`     |
|`Mark("!")` | !      |                  | Rojo Claro       | Blanco Brillante | `[!]`     |
|`Mark("¡")` | ¡      |                  | Amarillo Claro   | Blanco Brillante | `[¡]`     |
|`Mark("*")` | *      |                  | Aguamarina Claro | Blanco Brillante | `[*]`     |
|`Mark("~")` | ~      |                  | Blanco Brillante | Verde Claro      | `[~]`     |
|`Mark("#")` | #      |                  | Gris             | Blanco Brillante | `[#]`     |
|`Mark("&")` | &      |                  | Verde Claro      | Aguamarina Claro | `[&]`     |
|`Mark("?")` | ?      |                  | Amarillo Claro   | Aguamarina Claro | `[?]`     |

+ Ejemplos:
  
  ```python
   #~ Siempre se tiene que añadir fuera del print()
  
  print("\n\n\t", end=""), Mark(), print(" Hey!")
  print("\n\t", end=""), Mark("!","VC","BB"), print(" Hola Mundo!")
  ```
+ En Pantalla:
  
####~ Imagen Pendiente. xD

---

## isWindows()

+ Devuelve True si el sistema operativo es Windows

---

## isLinux()

+ Devuelve True si el sistema operativo es Linux

---

## isPyver2()

+ Devuelve True si la versión de Python es 2.X

---

## isPyver3()

+ Devuelve True si la versión de Python es 3.X

---

## Clear()

+ Limpia pantalla, compatible con cualquier Sistema Operativo.

---

## inp()

+ Permite escribir en pantalla, compatible con cualquier Versión de Python.

#### Modo de uso:

+ Se le pasa la cadena que se imprimir en pantalla para pedir datos.

+ Se usa de la misma manera en que se usaria ___raw_input()___ en Python 2 o ___input()___ en python 3.

```python
xD = inp("Escribe Algo: ")
``` 

---

## WinSize()

+ Cambia el tamaño de la ventana al antojo.

#### Modo de Uso:

+ Por Defecto pondra el tamaño de la ventana en __Ancho=82__, __Alto=55__
```python
WinSize()
```

+ Pondra el tamaño de la ventana en __Ancho=50__, __Alto=25__
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

## HiddenCursor()

+ Oculta o Muestra el Cursor en Pantalla.

#### Modo de Uso:

+ Por Defecto, ocultará el Cursor solo Mandando a llamar la función.
```python
HiddenCursor()
```

+ Para Ocultar/Desocultar el Cursor puedes mandar a llamar la función de las sigueintes maneras.
```python

#~ Para ocultar.
HiddenCursor("Hidden")

#~ Para mostrar.
HiddenCursor("Show")
```
