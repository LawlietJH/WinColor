# WinColor
## Pon Color A Tus Scripts de Python En Windows.

### Modo de Uso:

Tienes que importar el modulo WinColor a tu Script: `import WinColor`
, esto te permitira usar los metodos: `WinColor.color()`, `WinColor.rest()`, `WinColor.Dat()`, etc...
  
//Importar de la siguiente manera evitará escribir demasiado: `from WinColor import *`.
De esta manera podras llamar a los métodos sin necesidad de especificar antes el modulo: `WinColor.Dat()` ---> `Dat()`


### Funciones Disponibles:

```python
WinColor.Dat()
WinColor.color()
WinColor.rest()
WinColor.flush()
WinColor.Mark()
WinColor.isWindows()
WinColor.isLinux()
WinColor.isPyver2()
WinColor.isPyver3()
WinColor.Clear()
WinColor.inp()
WinColor.WinSize()
WinColor.ChkMod()
WinColor.HiddenCursor()
```


  + La funcion `color()` requiere una serie de parametros, puede ser cualquiera de la sguiente lista:

    
    ```python
    #~ Ejemplos:
    color("x0"), color("negro"), color("N")
    ```
    
      + Lista De Colores:
        * Negro             = x0,   negro,          N
        * Azul              = x1,   azul,           AZ
        * Verde             = x2,   verde,          V
        * Aguamarina        = x3,   aguamarina,     AG
        * Rojo              = x4,   rojo,           R
        * Púrpura           = x5,   purpura,        P
        * Amarillo          = x6,   amarillo,       AM 
        * Blanco            = x7,   blanco,         B
        * Gris              = x8,   gris,           G
        * Azul Claro        = x9,   azul cl,        AZC
        * Verde Claro       = xA,   verde cl        VC
        * Aguamarina Claro  = xB,   aguamarina cl,  AGC
        * Rojo Claro        = xC,   rojo cl,        RC
        * Púrpura Claro     = xD,   purpura cl,     PC
        * Amarillo Claro    = xE,   amarillo cl,    AMC
        * Blanco Brillante  = xF,   blanco br,      BB
  
  + El metodo `rest()` Restaura al color por defecto de la ventana.
  
  + El método `Dat()` limpiará pantalla y mostrara el Nombre, Autor y Versión del Script y cerrará el programa.
  
  Ejemplos de uso:
  
  ```python
  from WinColor import *
  
  color("azul cl")
  print("\n\n\t Esto es un texto en Azul Claro")
  
  color("rojo cl")
  print("\n\n\t Ahora Esta linea es de color Rojo Claro"
  
  reset()
  print("\n\n\t Esta linea tiene ahora el color por defecto de la ventana de comandos")
  ```
  
  
  
