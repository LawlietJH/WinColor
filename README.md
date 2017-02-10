# WinColor
## Pon Color A Tus Scripts de Python En Windows.

### Modo de Uso:

Tienes que importar el módulo WinColor a tu Script: `import WinColor`, esto te permitirá usar los métodos: `WinColor.color()`, `WinColor.rest()`, `WinColor.Dat()`, etc...
  
Para importar todo, se escribe de la siguiente manera y así se evitará escribir demasiado: `from WinColor import *`, de esta manera se podrá llamar a los métodos sin necesidad de especificar el nombre del módulo: `WinColor.Dat()` ---> `Dat()`


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


## color()

### La función `color()` requiere una serie de parámetros, puede ser cualquiera de la siguiente lista:

```python
#~ Ejemplos:
color("x0"), color("negro"), color("N")
```
    
Lista De Colores:

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
| Aguamarina Claro | xB  | aguamarina cl | AGC    |   
| Rojo Claro       | xC  | rojo cl       | RC     |
| Púrpura Claro    | xD  | purpura cl    | PC     |
| Amarillo Claro   | xE  | amarillo cl   | AMC    |
| Blanco Brillante | xF  | blanco br     | BB     |

  Ejemplos de uso:
  
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
  
## rest()
  La función `rest()` Restaura al color por defecto de la ventana.
  
## Dat()
  La función `Dat()` limpiará pantalla y mostrara el Nombre, Autor y Versión del Script y cerrará el programa.
  
## flush()
  La función `flush()` es una función ___auxiliar___ que ayudará a limpiar el buffer y hacer que imprimirá los colores correctamente en dado caso de alguna falla al imprimir en pantalla con algún color.
  Para usar esta función simplemente se tiene que colocar el nombre `flush()` antes de la función `color()` con la que se tenga problemas al imprimir el color (si es que llegara a suceder, pero en verdad, dudo que pase).
  
