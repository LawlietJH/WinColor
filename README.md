# WinColor
## Pon Color A Tus Scripts de Python En Windows.

### Modo de Uso:

Tienes que importar el modulo WinColor a tu Script: `import WinColor`, esto te permitira usar los metodos: `WinColor.Color()`,`WinColor.Rest()`, `WinColor.Dat()`
  
//Importar de la siguiente manera evitará escribir demasiado: `from WinColor import Color, Reset, Dat`, el metodo Dat es opcional.
De esta manera podras llamar a los metodos sin necesidad de especificar antes el modulo: `WinColor.Dat()` ---> `Dat()`
  + La funcion `ColorI()` requiere una serie de parametros, puede ser cualquiera de la sguiente lista:

    + Ejemplo: `Color("x0")`, `Color("negro")` o `Color("N")`
    
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
  
  + El metodo `Reset()` Restaura los color por defecto de la ventana
  
  + El método `Dat()` limpiará pantalla y mostrara el Nombre, Autor y Versión del Script y cerrará el programa.
  
  Ejemplos de uso:
  
  ```[Python]
  from WinColor import Color, Reset, Dat
  
  Color("azul cl")
  print("\n\n\t Esto es un texto en Azul Claro")
  
  Color("rojo cl")
  print("\n\n\t Ahora Esta linea es de color Rojo Claro"
  
  Reset()
  print("\n\n\t Esta linea tiene ahora el color por defecto de la ventana de comandos")
  ```
  
  
  
